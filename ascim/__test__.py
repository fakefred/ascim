from .ascim import ASCIM
from .draw import ASCIMDraw
from .table import ASCIMTable

if __name__ == '__main__':
    """Test basic ASCIM features."""
    digit_matrix = '''0123456789
1234567890
2345678901
3456789012
4567890123
5678901234
6789012345
7890123456
8901234567
9012345678'''
    im = ASCIM(digit_matrix)
    assert im.to_text() == digit_matrix

    full_of_x = ASCIM.new((5, 5), fill='x')
    x_matrix = ('xxxxx\n' * 5)[:-1]
    assert full_of_x.to_text() == x_matrix

    textbox = ASCIM('lorem\nipsum')
    im.paste(textbox, (4, 2))
    assert im.to_text() == '''0123456789
1234567890
2345lorem1
3456ipsum2
4567890123
5678901234
6789012345
7890123456
8901234567
9012345678'''

    table_text = '''
+---------+-------+------------+
| absolut | vodka | wooooo     |
+---------+-------+------------+
| vintage | beer  | asdfgh     |
+---------+-------+------------+
| badass  | shit  | zxcvbnm    |
| asfuck  | wine  | 1234567    |
+---------+-------+------------+
'''.strip('\n')

    # print(ASCIMTable.from_text(table_text).cell_at(1, 1).to_text())
    # print(ASCIMTable.from_text(table_text).to_text())
    # print(ASCIMTable.new((3, 3)).to_text())

    draw = ASCIMDraw(im)
    draw.text((1, 5, 5, 2), 'lorem ipsum')
    print(im.to_text())
