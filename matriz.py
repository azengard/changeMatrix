# -*- coding: utf8 -*-

def read_sequence():  # Read and validate a sequence of commands.
    charValid = ("ICLVHKFSX")
    sqc = input("Digite um comando: ").upper()
    sqc = sqc.split()

    for char in charValid:
        if char == sqc[0] and not "":
            return sqc
    else:
        print("Comando Inválido!\n")
        return sqc


def print_board(board):  # Print the Board.
    for row in board:
        print("".join(row))
    print("\n")


def create_array(cmd):  # Create a array - 'I' Command.
    board = []
    _, M, N = cmd

    for x in range(int(N)):
        board.append(["O"] * int(M))
    return board


def clean_array(board):  # Clean a array - 'C' Command.
    for x in range(0, len(board) - 1):
        for y in range(0, len(board[x]) - 1):
            board[x][y] = "O"
    return board


def color_pixel(cmd, board):  # Change the color of one pixel - 'L' Command.
    _, X, Y, C = cmd

    board[int(Y) - 1][int(X) - 1] = C
    return board


def ver_pixel(cmd, board):  # Change the color of a column - 'V' Command.
    _, X, Y1, Y2, C = cmd

    for ver in range(int(Y1) - 1, int(Y2)):
        board[int(ver)][int(X) - 1] = C
    return board


def hor_pixel(cmd, board):  # Change the color of a line - 'H' Command.
    _, X1, X2, Y, C = cmd

    for hor in range(int(X1) - 1, int(X2)):
        board[int(Y) - 1][int(hor)] = C
    return board


def block_pixel(cmd, board):  # Change color of an entire block - 'K' Command.
    _, X1, Y1, X2, Y2, C = cmd

    for hor in range(int(X1) - 1, int(X2)):
        for ver in range(int(Y1) - 1, int(Y2)):
            board[int(ver)][int(hor)] = C
    return board


def out_range(board, Y, X):  # Check if a cmd is out of list range.
    line = len(board)
    col = len(board[0])

    if (X >= 0 and X < col) and (Y >= 0 and Y < line):
        return True
    else:
        return False


def fill_pixel(cmd, board):  # Fill a continuous region 'F' command.
    F, X, Y, chgColor = cmd

    color = board[Y][X]

    if out_range(board, Y, X):
        board[Y][X] = chgColor
        if out_range(board, Y, X - 1):
            if board[Y][X - 1] == color:
                print(X - 1, Y)
                fill_pixel([F, X - 1, Y, chgColor], board)

        if out_range(board, Y, X + 1):
            if board[Y][X + 1] == color:
                print(X + 1, Y)
                fill_pixel([F, X + 1, Y, chgColor], board)

        if out_range(board, Y - 1, X):
            if board[Y - 1][X] == color:
                print(X, Y - 1)
                fill_pixel([F, X, Y - 1, chgColor], board)

        if out_range(board, Y + 1, X):
            if board[Y + 1][X] == color:
                print(X, Y + 1)
                fill_pixel([F, X, Y + 1, chgColor], board)

    return board


def main():
    while True:
        cmd = read_sequence()

        if cmd[0] == "X" and len(cmd) == 1:
            break

        elif cmd[0] == "I" and len(cmd) == 3:
            board = create_array(cmd)

        elif cmd[0] == "L" and len(cmd) == 4:
            board = color_pixel(cmd, board)

        elif cmd[0] == "V" and len(cmd) == 5:
            board = ver_pixel(cmd, board)

        elif cmd[0] == "H" and len(cmd) == 5:
            board = hor_pixel(cmd, board)

        elif cmd[0] == "K" and len(cmd) == 6:
            board = block_pixel(cmd, board)

        elif cmd[0] == "F" and len(cmd) == 4:
            cmd[1] = int(cmd[1]) - 1
            cmd[2] = int(cmd[2]) - 1
            board = fill_pixel(cmd, board)

        elif cmd[0] == "S" and len(cmd) == 1:
            pass

        elif cmd[0] == "C" and len(cmd) == 1:
            board = clean_array(board)

        else:
            continue

        print_board(board)


if __name__ == '__main__':
    main()
