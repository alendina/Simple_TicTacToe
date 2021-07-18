#  ~~~ TIC-TAC-TOY GAME ~~~~~
# ~~~ Put three in row and win! ~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def shaw_table(m):
    print('---------')
    print(f'| {m[0][0]} {m[0][1]} {m[0][2]} |')
    print(f'| {m[1][0]} {m[1][1]} {m[1][2]} |')
    print(f'| {m[2][0]} {m[2][1]} {m[2][2]} |')
    print('---------')


def check_wins(m):
    x_win = False
    o_win = False
    for i in range(3):
        if m[i][0] == m[i][1] == m[i][2] == 'O':     # for raw
            o_win = True
        if m[i][0] == m[i][1] == m[i][2] == 'X':     # for raw
            x_win = True
        if m[0][i] == m[1][i] == m[2][i] == 'O':     # for column
            o_win = True
        if m[0][i] == m[1][i] == m[2][i] == 'X':     # for column
            x_win = True
    if m[0][0] == m[1][1] == m[2][2] == 'O':     # for diagonal
        o_win = True
    if m[0][0] == m[1][1] == m[2][2] == 'X':     # for diagonal
        x_win = True
    if m[2][0] == m[1][1] == m[0][2] == 'O':  # for diagonal
        o_win = True
    if m[2][0] == m[1][1] == m[0][2] == 'X':  # for diagonal
        x_win = True

    # print('x_win', x_win, 'o_win', o_win, 'str(matrix).count(_)' , str(matrix).count('_'))
    if x_win == o_win == True:
        print('Impossible')
        exit()
    elif o_win:
        print('O wins')
        exit()
    elif x_win:
        print('X wins')
        exit()
    elif str(matrix).count('_') == 0:
        print('Draw')
        exit()


def check_occupied(i, j, m):
    if m[i-1][j-1] == 'X' or m[i-1][j-1] == 'O':
        return True
    else:
        return False


xo = 'X'
matrix = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
shaw_table(matrix)

while True:
    coord = input('Enter the coordinates: ').split()
    if len(coord) == 2:
        x = coord[0]
        y = coord[1]
    else:
        print('You should enter numbers!')
        continue
    if not x.isnumeric() or not y.isnumeric():
        print('You should enter numbers!')
        continue
    elif x not in '123' or y not in '123':
        print('Coordinates should be from 1 to 3!')
        continue
    elif check_occupied(int(x), int(y), matrix):
        print('This cell is occupied! Choose another one!')
        continue
    else:
        matrix[int(x)-1][int(y)-1] = xo
        shaw_table(matrix)
        check_wins(matrix)
        if xo == 'X':
            xo = 'O'
        else:
            xo = 'X'
