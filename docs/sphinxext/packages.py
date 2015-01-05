"""Adds a Sphinx directive to generate a list of packages"""

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

        return docutils.nodes.image(
            uri=info['img'], target=info['url'], alt=info['alt'])
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


class Package(object):
    @classmethod
    def from_line(cls, line):
        info = line.split()
        return cls(name=info[0], options=dict(s.split('=') for s in info[1:]))

    def __init__(self, name, options):
        self.name = name
        self.options = options


class PythonPackage(Package):
    def __init__(self, name, options):
        super(PythonPackage, self).__init__(name, options)
        self.options.setdefault('repo', 'borntyping/{}'.format(name))
        self.options.setdefault('docs', 'none')

    @link
    def package(self):
        return self.name, 'https://github.com/{repo}'

    # @link
    # def github_link(self):
    #     return ('GitHub repository', 'https://github.com/{repo}')

    # @link
    # def github_issues(self):
    #     return ('Issue tracker', 'https://github.com/{repo}/issues')

    @badge
    def issues(self):
        return {
            'img': 'http://img.shields.io/github/issues/{repo}.svg',
            'url': 'https://github.com/{repo}/issues',
            'alt': 'GitHub issue tracker for {repo}'
        }

    @badge
    def travis(self):
        return {
            'img': 'http://img.shields.io/travis/{repo}.svg',
            'url': 'https://travis-ci.org/{repo}',
            'alt': 'Continuous integration status for {repo}'
        }

    @badge
    def version(self):
        return {
            'img': 'http://img.shields.io/pypi/v/{name}.svg',
            'url': 'https://pypi.python.org/pypi/{name}',
            'alt': 'Version for package {name} on PyPI'
        }

    @badge
    def licence(self):
        return {
            'img': 'http://img.shields.io/pypi/l/{name}.svg',
            'url': 'https://pypi.python.org/pypi/{name}',
            'alt': 'Licence for package {name} on PyPI'
        }

    @badge
    def documentation(self):
        if self.options['docs'] == 'rtd':
            return {
                'img': 'https://readthedocs.org/projects/{name}/badge/'
                       '?version=latest&style=flat-square',
                'url': 'http://{name}.readthedocs.org/en/latest/',
                'alt': 'Documentation for package {name} on Read The Docs'
            }
        elif self.options['docs'] == 'none':
            return {
                'img': 'http://img.shields.io/badge/docs-none-lightgrey.svg',
                'url': '#',
                'alt': 'No documentation availible for package {name}'
            }
        else:
            return {
                'img': 'http://img.shields.io/badge/docs-link-yellow.svg',
                'url': self.options['docs'],
                'alt': 'Documentation for package {name}'
            }


class PackageDirective(docutils.parsers.rst.Directive):
    required_arguments = 1
    option_spec = {
        'repo': lambda x: x,
        'docs': lambda x: x
    }

    def run(self):
        global loaded_packages
        package = PythonPackage(self.arguments[0].strip(), self.options)
        loaded_packages.append(package)
        return []


class PackageTableDirective(docutils.parsers.rst.Directive):
    columns = (
        ('Package', 'package'),
        ('Version', 'version'),
        ('Licence', 'licence'),
        ('GitHub Issues', 'issues'),
        ('CI status', 'travis'),
        ('Documentation', 'documentation')
    )

    def export_headers(self):
        return [k for k, v in self.columns]

    def export_package(self, package):
        return [getattr(package, v)() for k, v in self.columns]

    def run(self):
        return [table.table(
            head=self.export_headers(),
            body=map(self.export_package, loaded_packages)
        )]


# class PackageDetailsDirective(docutils.parsers.rst.Directive):
#     def export_package(self, package):
#         section = docutils.nodes.section(ids=[package.name])
#         section.append(docutils.nodes.title(text=package.name))

#         badges = docutils.nodes.paragraph()
#         for attr in ('version', 'licence', 'issues', 'documentation'):
#             badges.append(getattr(package, attr)())
#         section.append(badges)

#         links = docutils.nodes. bullet_list()
#         for attr in ('github_link', 'github_issues', 'documentation_link'):
#             link = getattr(package, attr)()
#             links.append(docutils.nodes.list_item('', link))
#         section.append(links)

#         return section

#     def run(self):
#         global loaded_packages
#         return [self.export_package(package) for package in loaded_packages]


def setup(app):
    app.add_directive('package', PackageDirective)
    app.add_directive('package-status', PackageTableDirective)
    # app.add_directive('package-details', PackageDetailsDirective)
