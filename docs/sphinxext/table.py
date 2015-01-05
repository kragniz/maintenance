"""Functions for building a table"""

import docutils.nodes


def cell(contents):
    if isinstance(contents, basestring):
        contents = docutils.nodes.paragraph(text=contents)
    return docutils.nodes.entry('', contents)


def row(cells):
    return docutils.nodes.row('', *[cell(c) for c in cells])


def table(head, body, colspec=None):
    table = docutils.nodes.table()
    tgroup = docutils.nodes.tgroup()
    table.append(tgroup)

    # Create a colspec for each column
    if colspec is None:
        colspec = [1 for n in range(len(head))]

    for width in colspec:
        tgroup.append(docutils.nodes.colspec(colwidth=width))

    # Create the table headers
    thead = docutils.nodes.thead()
    thead.append(row(head))
    tgroup.append(thead)

    # Create the table body
    tbody = docutils.nodes.tbody()
    tbody.extend([row(r) for r in body])
    tgroup.append(tbody)

    return table
