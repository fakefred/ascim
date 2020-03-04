.. py:module:: ascim.ascim.ASCIM
.. py:currentmodule:: ascim.ascim.ASCIM

:py:mod:`ASCIM` Module
======================

Basic type for an ASCIM Image. In an ASCIM Image, every character works like
a pixel as in raster images. Characters are zero-indexed, and are represented
in (x, y). For an ASCIM Image whose bottom-right character is (x, y), its size
is (x + 1, y + 1).

Example
-------

.. code-block:: python

    from ascim.ascim import ASCIM
    im = ASCIM('''In ASCIM,
    every character
    is like
    a pixel''')


`im` is now an ASCIM object, with the following text (enclosed in rectangle*):

.. code-block::

     +-----------------+
    0| In ASCIM,       |
    1| every character |
    2| is like         |
    3| a pixel         |
     +-----------------+

Lines 0, 2, and 3, which are zero-indexed, are padded with spaces to their
right so that they are all uniform in length with Line 1.
An ASCIM object is treated as an image, so string methods no longer apply.

\* but what _is_ in this rectangle? We will cover this later on in section
'ASCIM Tables'.

Construction
------------

.. autofunction:: ascim.ascim.ASCIM.__init__

.. autofunction:: ascim.ascim.ASCIM.new

.. autofunction:: ascim.ascim.ASCIM.from_list

Methods
-------

.. automethod:: ascim.ascim.ASCIM.copy

.. automethod:: ascim.ascim.ASCIM.paste

.. automethod:: ascim.ascim.ASCIM.crop

.. automethod:: ascim.ascim.ASCIM.autocrop

.. automethod:: ascim.ascim.ASCIM.show

.. automethod:: ascim.ascim.ASCIM.to_text

.. automethod:: ascim.ascim.ASCIM.to_rows

.. automethod:: ascim.ascim.ASCIM.to_columns

.. automethod:: ascim.ascim.ASCIM.char_at

.. automethod:: ascim.ascim.ASCIM.set_char

Attributes
----------

.. autoattribute:: ascim.ascim.ASCIM.size
