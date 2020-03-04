from .ascim import ASCIM


class ASCIMDraw:
    """Draw text and shapes on an ASCIM Image. Operations will be done in-place."""

    def __init__(self, im):
        """Construct a ASCIMDraw object on a canvas.
        
        :param im: ASCIM Image this ASCIMDraw object applies modifications to.
        """
        
        if hasattr(im, 'size'):
            # HACK: very naïve duck type checking
            self.__image = im
        else:
            raise TypeError('`ASCIMDraw` requires an ASCIM Image as argument.')

    def text(self, box: tuple, text: str, transparency=False):
        """Draw text on ASCIM Image.

        :param box: box to fit the text in. (left, top, width, height)
        :param text: text to draw on ASCIM Image.
        :param transparency: if set to True, when the ``text`` to be drawn overlaps
            with non-whitespace characters in the original image, the character
            from the latter is kept. Otherwise, the character is a space.
        """

        wrapped = ''
        words = text.split(' ')
        width = 0
        for wd in words:
            if width + len(wd) <= box[2]:
                wrapped += wd + ' '
                width += len(wd) + 1
            else:
                wrapped += '\n' + wd + ' '
                width = len(wd) + 1
        # remove trailing space on each line, incl. last line
        wrapped = wrapped.replace(' \n', '\n')[:-1]
        self.__image.paste(ASCIM(wrapped), (box[0], box[1]))
