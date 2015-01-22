"""Adds a Sphinx directive to generate a list of projects"""

import functools

import docutils.nodes
import docutils.parsers.rst

import table


loaded_packages = []


def badge(function):
    @functools.wraps(function)
    def wrapper(package, *args, **kwargs):
        info = function(package, *args, **kwargs)

        for k, v in info.items():
            info[k] = v.format(name=package.name, **package.options)

        if 'img.shields.io' in info['img']:
            info['img'] += '?style=flat-square'

        # Wraps the image in a link
        ref = docutils.nodes.reference(refuri=info['url'])
        ref.append(docutils.nodes.image(uri=info['img'], alt=info['alt']))
        return ref
    return wrapper


def link(function):
    @functools.wraps(function)
    def wrapper(package, *args, **kwargs):
        text, url = function(package, *args, **kwargs)

        text = text.format(name=package.name, **package.options)
        url = url.format(name=package.name, **package.options)

        link = docutils.nodes.reference(text=text, refuri=url)
        return docutils.nodes.paragraph('', '', link)
    return wrapper


class Project(object):
    @classmethod
    def from_line(cls, line):
        info = line.split()
        return cls(name=info[0], options=dict(s.split('=') for s in info[1:]))

    def __init__(self, name, options):
        self.name = name
        self.options = options
        self.options.setdefault('repo', 'borntyping/{}'.format(name))
        self.options.setdefault('docs', None)
        self.options.setdefault('chef', None)

    @link
    def github_repo(self):
        return self.name, 'https://github.com/{repo}'

    @badge
    def github_issues(self):
        return {
            'img': 'https://img.shields.io/github/issues/{repo}.svg',
            'url': 'https://github.com/{repo}/issues',
            'alt': 'GitHub issue tracker for {repo}'
        }

    @badge
    def travis_status(self):
        return {
            'img': 'https://img.shields.io/travis/{repo}.svg',
            'url': 'https://travis-ci.org/{repo}',
            'alt': 'Continuous integration status for {repo}'
        }

    @badge
    def pypi_version(self):
        return {
            'img': 'https://img.shields.io/pypi/v/{name}.svg',
            'url': 'https://warehouse.python.org/pypi/{name}/',
            'alt': 'Version for package {name} on PyPI'
        }

    @badge
    def pypi_licence(self):
        return {
            'img': 'https://img.shields.io/pypi/l/{name}.svg',
            'url': 'https://warehouse.python.org/pypi/{name}/',
            'alt': 'Licence for package {name} on PyPI'
        }

    @badge
    def documentation(self):
        if self.options['docs'] is not None:
            return {
                # The RTD badge tends to be very slow
                # 'img': 'https://readthedocs.org/projects/{name}/badge/'
                #        '?version=latest&style=flat-square',
                'img': 'https://img.shields.io/badge/docs-latest-brightgreen.svg',
                'url': 'https://{name}.readthedocs.org/en/latest/',
                'alt': 'Documentation for package {name} on Read The Docs'
            }
        else:
            return {
                'img': 'https://img.shields.io/badge/docs-none-lightgrey.svg',
                'url': '#',
                'alt': 'No documentation availible for package {name}'
            }

    @badge
    def chef_cookbook(self):
        if self.options['chef'] is None:
            return {
                'img': 'https://img.shields.io/cookbook/v/{name}.svg',
                'url': 'https://supermarket.chef.io/cookbooks/{name}',
                'alt': '{name} cookbook on Chef Supermarket'
            }
        else:
            return {
                'img': 'https://img.shields.io/badge/cookbook-{chef}-red.svg',
                'url': '#',
                'alt': '{name} is not on Chef Supermarket'
            }


class ProjectStatusList(docutils.parsers.rst.Directive):
    """Exports a table of projects"""

    # The optional argument is the project type
    optional_arguments = 1

    projects = []

    COLUMNS = {
        'default': (
            ('Project', 'github_repo'),
            ('GitHub Issues', 'github_issues'),
            ('CI status', 'travis_status')
        ),
        'cookbook': (
            ('Project', 'github_repo'),
            ('Version', 'chef_cookbook'),
            ('GitHub Issues', 'github_issues'),
            ('CI status', 'travis_status')
        ),
        'python': (
            ('Package', 'github_repo'),
            ('Version', 'pypi_version'),
            ('GitHub Issues', 'github_issues'),
            ('CI status', 'travis_status'),
            ('Documentation', 'documentation')
        ),
        'deprecated': (
            ('Package', 'github_repo'),
        )
    }

    def columns(self):
        project_type = 'default'

        if len(self.arguments) > 0 and self.arguments[0] in self.COLUMNS:
            project_type = self.arguments[0]

        return self.COLUMNS[project_type]

    def export_headers(self):
        return [k for k, v in self.columns()]

    def export_project(self, project):
        return [getattr(project, v)() for k, v in self.columns()]

    def get_and_clear_projects(self):
        projects = self.__class__.projects
        self.__class__.projects = []
        return projects

    def run(self):
        return [table.table(
            head=self.export_headers(),
            body=map(self.export_project, self.get_and_clear_projects())
        )]


class ProjectDirective(docutils.parsers.rst.Directive):
    required_arguments = 1
    option_spec = {
        'repo': lambda x: x,
        'docs': lambda x: x,
        'chef': lambda x: x
    }

    def run(self):
        """Append a project to the current status list and return nothing."""
        ProjectStatusList.projects.append(
            Project(self.arguments[0].strip(), self.options))
        return []


def setup(app):
    app.add_directive('project', ProjectDirective)
    app.add_directive('project-status', ProjectStatusList)
