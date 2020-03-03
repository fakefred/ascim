# ASCIM - Manipulate ASCII art as you would do with raster images

![Upload Python Package](https://github.com/fakefred/ascim/workflows/Upload%20Python%20Package/badge.svg) ![PyPI](https://img.shields.io/pypi/v/ascim)

## Pre-document Humor

> Do you know why the crazy guy started a side project to feed another one?
>
> No, you should ASCIM.

If you came here from memethesis-cli, go straight to section 'ASCIM Tables'.

## Installation

`pip install ascim` will do.

## Usage

### Basic ASCIM Class

```python
from ascim.ascim import ASCIM
im = ASCIM('''In ASCIM,
every character
is like
a pixel''')
```

`im` is now an ASCIM object, with the following text (enclosed in rectangle\*):

```
 +-----------------+
0| In ASCIM,       |
1| every character |
2| is like         |
3| a pixel         |
 +-----------------+
```

Lines 0, 2, and 3, which are zero-indexed, are padded with spaces to their right
so that they are all uniform in length with Line 1.
An ASCIM object is treated as an image, so string methods no longer apply.

> \* but what _is_ in this rectangle? We will cover this later on in section
> 'ASCIM Tables'.

### ASCIM Tables

An ASCIM Table is a container object of ASCIM Images. An ASCIM Image (or NoneType)
can take up one cell in a table, just like in spreadsheets.

Code example:

```python
from ascim.ascim import ASCIM
from ascim.table import ASCIMTable

table = ASCIMTable.from_text('<copy paste that table from below>')
print(table.cell_at(0, 0).to_text())  # => 'symbol'
print(table.size)  # => (4, 7)
```

#### Textual representation

The textual representation for ASCIM Tables are designed to be both machine- and
human-readable. Here is an example:
([relevant xkcd](https://xkcd.com/394/))

```
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
```

##### Specification

1. A **cell** is an ASCIM object or NoneType stored in the ASCIMTable.
   When printed, it is enclosed with `+` and `-` horizontally and
   `+` and `|` vertically. NoneType denotes there is no content in the cell,
   and is interpreted as an 1x1 ASCIM object when displayed.
2. On each side of the pipe (vertical bar; `|`) that is a cell MUST
   be a space. As illustrated:

   ```
   +---+
   |012|
   |345|
   |678|
   +---+
   ```

   In this rect-enclosed area, the "cell" only covers 1, 4, and 7.
   Locations 0, 3, 6, 2, 5, 8 MUST be a space.
   Locations 1 and 7 SHOULD NOT be a space.
   That said, only horizontal margins are necessary.

3. When a row is too wide or a column is too tall in the text to convert
   to an ASCIMTable, the excess columns/rows of spaces are cut off.

### ASCIM Draw

With ASCIMDraw you can make in-place modifications with an ASCIM Image.
An ASCIMDraw object takes a (reference to) an ASCIM object as its argument.

Code example:

```python
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
```
