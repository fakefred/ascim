from .utils import *


class ASCIM:
    """Basic type for an ASCIM Image."""

    def __init__(self, text: str):
        """Initialize an ASCIM Image.

        In an ASCIM Image, a character is a pixel,
        line (row) #A corresponds to y=A, and column #A, x=A.
        A is zero-indexed, just like real bitmap images.

        When line widths vary, ASCIM will pad spaces to lines so that
        line widths are uniform.

        :param text: string to transform to an ASCIM object.
        """

        # all of what are assigned to `self` here are private.
        rows = text.split('\n')
        self.__size = (max([len(l) for l in rows]), len(rows))
        for i, l in enumerate(rows):
            # fill up margins so all rows are uniform in length
            rows[i] += ' ' * (self.__size[0] - len(l))
        self.__rows = rows

    @classmethod
    def from_list(cls, ls: list):
        """Construct an ASCIM Image from a list of strings.

        :param ls: list from which ASCIM Image is constructed.
        """
        return ASCIM('\n'.join(ls))  # HACK

    @classmethod
    def new(cls, size: tuple, fill=' '):
        """Construct a blank new ASCIM Image with a repeating single character.

        :param size: tuple (width, height) as size of the new ASCIM Image.
        :param fill: character to fill the image with.
        """
        if not is_char(fill):
            raise ValueError('`fill` must be an ascii character')
        # [:-1]: remove trailing \n
        return ASCIM(((fill * size[0] + '\n') * size[1])[:-1])

    def copy(self):
        """:returns: A copy of image."""
        return ASCIM(self.to_text())

    def to_text(self) -> str:
        """:returns: Textual representation of image"""
        return '\n'.join(self.__rows)

    def show(self):
        """Prints image to stdout"""
        print(self.to_text())

    def to_rows(self) -> list:
        """:returns: A representation of image in a list of rows."""

        return self.__rows

    def to_columns(self) -> list:
        """:returns: A representation of image in a list of columns."""

        columns = []
        for x in range(self.__size[0]):
            col = ''
            for y in range(self.__size[1]):
                col += self.__rows[y][x]
            columns.append(col)
        return columns

    def char_at(self, x: int, y: int) -> str:
        """Retrieve a single character from image.

        :returns: If (x, y) is inside of bound, the character at (x, y);
            else, ``None``.
        """

        if self.__in_bound(x, y):
            return self.__rows[y][x]
        else:
            return None

    def set_char(self, x: int, y: int, char: str):
        """Set one character of self to `char` in-place.

        :raises: ValueError if `char` is not 1 in length.
        """

        if not isinstance(char, str) or not len(char) == 1:
            raise ValueError

        row = self.__rows[y]
        self.__rows[y] = row[:x] + char + row[x+1:]

    @property  # read-only
    def size(self) -> tuple:
        """:returns: size of image in (width, height) characters"""

        return self.__size

    def crop(self, box: tuple):
        """:returns: a cropped copy of an ASCIM Image.

        When any parameter in `box` is out of bound, ASCIM will use the closest
        edge instead. For example, when `self` is 33 characters wide (right edge
        x=32) but a crop to right edge x=36, ASCIM will make the right edge x=32.

        :param box: a tuple of (left, top, width, height).
        """

        return ASCIM.from_list(
            [r[box[0]:box[0]+box[2]] for r in self.__rows[box[1]:box[1]+box[3]]])

    def autocrop(self):
        """:returns: a copy of `self` with spaces on the edges cropped out. """

        copy = self.copy()
        while copy.to_columns()[0].isspace():  # left
            copy = copy.crop((1, 0, copy.size[0] - 1, copy.size[1]))
        while copy.to_columns()[-1].isspace():  # right
            copy = copy.crop((0, 0, copy.size[0] - 1, copy.size[1]))
        while copy.to_rows()[0].isspace():  # top
            copy = copy.crop((0, 1, copy.size[0], copy.size[1] - 1))
        while copy.to_rows()[-1].isspace():  # bottom
            copy = copy.crop((0, 0, copy.size[0], copy.size[1] - 1))

        return copy

    def paste(self, im, xy: tuple, transparency=''):
        """Pastes ASCIM Image `im` onto self in-place.

        When the location specified in `xy` exceeds image boundary, make no
        modification to `self`.

        :param im: ASCIM Image to paste on `self`.
        :param xy: a tuple of (left, top) for the corner to paste `im`.
        :param transparency: the character which, when in `im`, is interpreted as
            a transparent pixel and will not overwrite the corresponding character
            on the destination image. When set to a False value, no transparency
            is applied.
        """

        imx, imy = im.size
        boxx, boxy = xy

        # when in doubt, use brute force
        for y in range(self.__size[1]):
            if boxy <= y < boxy + imy:
                for x in range(self.__size[0]):
                    if (boxx <= x < boxx + imx and
                            not im.char_at(x - boxx, y - boxy) == transparency):
                        self.set_char(x, y, im.char_at(x - boxx, y - boxy))

    def __in_bound(self, x, y) -> bool:
        """Check if point(x, y) is inside image bound."""

        if 0 <= x < self.__size[0] and 0 <= y < self.__size[1]:
            return True
        return False
