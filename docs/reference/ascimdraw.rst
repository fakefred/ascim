.. py:module:: ascim.draw.ASCIMDraw
.. py:currentmodule:: ascim.draw.ASCIMDraw

:py:mod:`ASCIMDraw` Module
==========================

With ASCIMDraw you can make in-place modifications with an ASCIM Image.
An ASCIMDraw object takes a (reference to) an ASCIM object as its argument.

Example
-------

Draw text on Image
^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from ascim.ascim import ASCIM
    from ascim.draw import ASCIMDraw

    im = ASCIM.new((5, 5))
    draw = ASCIMDraw(im)
    draw.text((1, 2, 4, 2), 'oh nice')  # text is wrapped in a 4x2 box
    # `im` is modified in-place
    print(im.to_text())
    #
    #
    #  oh
    #  nice
    #

Construction
------------

.. autofunction:: ascim.draw.ASCIMDraw.__init__

Methods
-------

.. automethod:: ascim.draw.ASCIMDraw.text
