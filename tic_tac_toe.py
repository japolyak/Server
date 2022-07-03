cells = input("Enter the cells: > ")


def x_or_o(inp):
    x_list_o = []
    for i in inp:
        if i == "x":
            x_list_o.append(i)
        elif i == "o":
            x_list_o.append(i)
        else:
            x_list_o.append(" ")
    return x_list_o


def start_matrix(a):
    game_field = [["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                  ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
                  ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
                  ["|", " ", " ", " ", " ", " ", " ", " ", "|"],
                  ["-", "-", "-", "-", "-", "-", "-", "-", "-"]]

    n = 0
    xo = x_or_o(a)

    for it in range(1, 4):
        for j in range(2, 7, 2):
            game_field[it][j] = xo[n]
            n += 1
    return game_field


def print_field(nest_list):

    for k in range(0, 9):
        print(nest_list[0][k], end='')
    print()

    for i in range(1, 4):
        for k in range(0, 9):
            print(nest_list[i][k], sep='', end='')
        print()

    for k in range(0, 9):
        print(nest_list[4][k], end='')


print_field(start_matrix(cells))
