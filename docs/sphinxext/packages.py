"""Adds a Sphinx directive to generate a list of packages"""

import functools

import docutils.nodes
import sphinx.util.compat

# import shields
import table


def badge(function):
    @functools.wraps(function)
    def wrapper(self, *args, **kwargs):
        info = function(self, *args, **kwargs)

        for k, v in info.items():
            info[k] = v.format(name=self.name, **self.options)

        if 'img.shields.io' in info['img']:
            info['img'] += '?style=flat-square'

        return docutils.nodes.image(
            uri=info['img'], target=info['url'], alt=info['alt'])
    return wrapper


class Package(object):
    columns = ()

    @classmethod
    def create_row(cls, line):
        return cls.from_line(line).export()

    @classmethod
    def from_line(cls, line):
        info = line.split()
        return cls(name=info[0], options=dict(s.split('=') for s in info[1:]))

    def __init__(self, name, options):
        self.name = name
        self.options = options
        self.options.setdefault('repo', 'borntyping/{}'.format(name))
        self.options.setdefault('licence', 'none')
        self.options.setdefault('docs', 'none')

    def export(self):
        return [getattr(self, v)() for k, v in self.columns]


class PythonPackage(Package):
    columns = (
        ('Package', 'link'),
        ('Version', 'version'),
        ('Licence', 'licence'),
        ('GitHub Issues', 'issues'),
        ('Documentation', 'documentation')
    )

    def link(self):
        return docutils.nodes.paragraph('', '', docutils.nodes.reference(
            text=self.name,
            refuri='https://github.com/{repo}'.format(**self.options)))

    @badge
    def issues(self):
        return {
            'img': 'http://img.shields.io/github/issues/{repo}.svg',
            'url': 'https://github.com/{repo}/issues',
            'alt': 'GitHub issue tracker for {repo}'
        }

    @badge
    def licence(self):
        if self.options['licence'] == 'MIT':
            color = 'brightgreen'
        elif self.options['licence'] == 'none':
            color = 'red'
        else:
            color = 'yellowgreen'

        return {
            'img': 'http://img.shields.io/badge/licence-{}-{}.svg'.format(
                self.options['licence'], color),
            'url': 'https://github.com/{repo}/blob/master/licence',
            'alt': 'Licence for package {name}'
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
                'img': 'http://img.shields.io/badge/docs-none-red.svg',
                'url': '#',
                'alt': 'No documentation availible for package {name}'
            }
        else:
            return {
                'img': 'http://img.shields.io/badge/docs-link-yellow.svg',
                'url': self.options['docs'],
                'alt': 'Documentation for package {name}'
            }


class PackageTableDirective(sphinx.util.compat.Directive):
    has_content = True

    def run(self):
        return [table.table(
            head=[k for k, v in PythonPackage.columns],
            body=[PythonPackage.from_line(l).export() for l in self.content],
        )]

def setup(app):
    app.add_directive('package-table', PackageTableDirective)
    return
