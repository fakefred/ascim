from .ascim import ASCIM
import re


class ASCIMTable:
    """ASCII Tables with simple manipulation functionalities.

    Each cell is an ASCIM Image, contrary to plaintext, although ASCIM Images
    can hold plaintext.

    If you're looking for a library that dumps csv or markdown, please look
    somewhere else.
    """

    def __init__(self, data: list):
        """Construct an ASCIM table object from a 2-dimensional list

        When rows are different in width, extra ``None`` are padded to their
        right until all rows have the same amount of columns.

        :param data: for a w*h table, this is a len=h list of len-w lists, each
            element of which populated by an ASCIM Image.
        """
        self.__size = (max([len(r) for r in data]), len(data))
        for i, r in enumerate(data):
            data[i].extend([None] * (self.__size[0] - len(r)))

        self.__data = data

    @classmethod
    def from_text(self, text: str):
        """Constructs an ASCIM Table from a string.

        Note that the string ``text`` must conform to a set of rules,
        as is generated from ASCIMTable's ``to_text()``.
        Valid table string:

        .. code-block::

            +-----+-----+------+
            | qwe | rty | uiop |
            +-----+-----+------+
            | asd | fgh | jkl  |
            +-----+-----+------+
            | zx  | cv  | bnm  |
            +-----+-----+------+

        """

        im = ASCIM(text)

        horizontal_lines = []
        vertical_lines = []

        for n, row in enumerate(im.to_rows()):
            if re.match('^\+(-+\+)+$', row):
                horizontal_lines.append(n)

        for n, col in enumerate(im.to_columns()):
            if re.match('^\+(\|+\+)+$', col):
                vertical_lines.append(n)

        if len(horizontal_lines) < 2 or len(horizontal_lines) < 2:
            raise ValueError('Invalid string to convert to table')

        cells = []
        for y in range(len(horizontal_lines) - 1):
            row = []
            y_start = horizontal_lines[y] + 1
            for x in range(len(vertical_lines) - 1):
                x_start = vertical_lines[x] + 2
                row.append(im.crop((
                    x_start, y_start,
                    vertical_lines[x + 1] - vertical_lines[x] - 3,
                    horizontal_lines[y + 1] - horizontal_lines[y] - 1
                )).autocrop())
            cells.append(row)

        return ASCIMTable(cells)

    def to_text(self) -> str:
        """:returns: textual representation of table."""
        # replace all None cells with an empty 1x1 ASCIM Image
        data = [[ASCIM.new((1, 1)) if col is None else col for col in row]
                for row in self.__data]
        table = ASCIMTable(data)
        # determine size of cells
        sizes = [[col.size for col in row] for row in data]
        widths = [max([row[x][0] for row in sizes])
                  for x in range(table.size[0])]
        heights = [max([col[1] for col in row]) for row in sizes]
        text = ''
        hl = '+'  # a line of +/- that make up horizontal lines
        vl = '|'  # a line of |/<space> that make up vertical lines
        for wd in widths:
            vl += ' ' * (wd + 2) + '|'
            hl += '-' * (wd + 2) + '+'
        hl += '\n'
        vl += '\n'
        for ht in heights:
            text += hl + vl * ht
        text += hl

        im = ASCIM(text)
        for rn, row in enumerate(data):
            for cn, col in enumerate(row):
                im.paste(col, (sum(widths[:cn]) + 3 * cn + 2,
                               sum(heights[:rn]) + rn + 1))

        return im.to_text()

    @classmethod
    def new(cls, size: tuple):
        """Construct a blank ASCIM Table of a certain size.

        :param size: tuple (width, height) as size of the new ASCIM Table,
            in number of cells.
        """

        return ASCIMTable([[None] * size[0]] * size[1])

    def copy(self):
        """:returns: a copy of `self`."""
        return ASCIMTable(self.__data)

    def cell_at(self, x: int, y: int):
        """Retrieve a single cell from table.

        :returns: ASCIM image or ``None`` as in the cell, or if ``(x, y)``
            exceeds bound, ``None``.
        """

        return self.__data[y][x]

    # TODO
    # def set_cell(self, x: int, y: int, cell):

    @property
    def size(self) -> tuple:
        """:returns: size of table in (width, height) cells"""

        return self.__size

    def __in_bound(self, x: int, y: int) -> bool:
        if 0 <= x < self.__size[0] and 0 <= y < self.__size[1]:
            return True
        return False
