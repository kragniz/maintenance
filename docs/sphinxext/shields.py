"""Functions for generating shields.io urls"""


def shield(*args):
    return 'https://img.shields.io/{args}.svg?style=flat-square'.format(
        args='/'.join(args))


def custom_badge(subject, status, color):
    status = status.replace('-', '--')
    status = status.replace('_', '__')
    status = status.replace(' ', '_')

    return shield('badge', '{}-{}-{}'.format(subject, status, color))


def rtd_badge(name):
    return (
        'https://readthedocs.org/projects/{name}/badge/'
        '?version=latest&style=flat'
    ).format(name=name)
