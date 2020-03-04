.. py:module:: ascim.table.ASCIMTable
.. py:currentmodule:: ascim.table.ASCIMTable

:py:mod:`ASCIMTable` Module
===========================

An ASCIM Table is a container object of ASCIM Images. An ASCIM Image
(or NoneType) can take up one cell in a table, just like in spreadsheets.

Example
-------

.. code-block:: python

    from ascim.ascim import ASCIM
    from ascim.table import ASCIMTable

    table = ASCIMTable.from_text('''
    +--------+---------------+---------------+------------------------+
    | symbol | name          | size          | notes                  |
    +--------+---------------+---------------+------------------------+
    | kB     | Kilobyte      | 1024 bytes    | 1000 bytes during leap |
    |        |               | or 1000 bytes | years, 1024 otherwise  |
    +--------+---------------+---------------+------------------------+
    | KB     | Kelly-Bootle  | 1012 bytes    | Compromise between     |
    |        | Standard Unit |               | 1000 and 1024 bytes    |
    +--------+---------------+---------------+------------------------+
    | KiB    | Imaginary     | 1024sqrt(-1)  | Used in quantum        |
    |        | Kilobyte      | bytes         | computing              |
    +--------+---------------+---------------+------------------------+
    | kb     | Intel         | 1023.937528   | Calculated on          |
    |        | Kilobyte      | bytes         | Pentium F.P.U          |
    +--------+---------------+---------------+------------------------+
    | Kb     | Drivemaker's  | Currently     | Shrinksby 4 bytes each |
    |        | Kilobyte      | 908 bytes     | year for marketing     |
    |        |               |               | reasons                |
    +--------+---------------+---------------+------------------------+
    | KBa    | Baker's       | 1152 Bytes    | 9 bits to the byte     |
    |        | Kilobyte      |               | since you're such a    |
    |        |               |               | good customer          |
    +--------+---------------+---------------+------------------------+
    '''.strip()
    print(table.cell_at(0, 0).to_text())  # => 'symbol'
    print(table.size)  # => (4, 7)

This initializes an ASCIMTable from a plaintext table, then extracts its cell
at (x=0, y=0) and print its size in (x, y).

The textual representation for ASCIM Tables are designed to be both machine
and human-readable. This example: `relevant xkcd <https://xkcd.com/394>`_.

Construction
------------

.. autofunction:: ascim.table.ASCIMTable.__init__

.. autofunction:: ascim.table.ASCIMTable.new

.. autofunction:: ascim.table.ASCIMTable.from_text


Methods
-------

.. automethod:: ascim.table.ASCIMTable.copy

.. automethod:: ascim.table.ASCIMTable.cell_at

.. automethod:: ascim.table.ASCIMTable.to_text

Attributes
----------

.. autoattribute:: ascim.table.ASCIMTable.size
