
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


def c_array(cmd):  # Create a array - 'I' Command.
    board = []
    for x in range(int(cmd[2])):
        board.append(["O"] * int(cmd[1]))
    return board


def print_board(board):  # Print the Board.
    for row in board:
        print("".join(row))
    print("\n")


def color_pixel(cmd, board):  # Change the color of one pixel - 'L' Command.
    L, X, Y, C = cmd
    board[int(Y) - 1][int(X) - 1] = C
    return board


def ver_pixel(cmd, board):  # Change color of a collum - 'V' Command.
    V, X, Y1, Y2, C = cmd
    for ver in range(int(Y1) - 1, int(Y2)):
        board[int(ver)][int(X) - 1] = C
    return board


def hor_pixel(cmd, board):  # Change color of a line - 'H' Command.
    H, X1, X2, Y, C = cmd
    for hor in range(int(X1) - 1, int(X2)):
        board[int(Y) - 1][int(hor)] = C
    return board


def main():
    while True:
        cmd = read_sequence()
        if cmd[0] == "X" and len(cmd) == 1:
            break
        elif cmd[0] == "I" and len(cmd) == 3:
            board = c_array(cmd)
        elif cmd[0] == "L" and len(cmd) == 4:
            board = color_pixel(cmd, board)
        elif cmd[0] == "V" and len(cmd) == 5:
            board = ver_pixel(cmd, board)
        elif cmd[0] == "H" and len(cmd) == 5:
            board = hor_pixel(cmd, board)
        elif cmd[0] == "K" and len(cmd) == 6:
            pass
        elif cmd[0] == "F" and len(cmd) == 4:
            pass
        elif cmd[0] == "S" and len(cmd) == 2:
            pass
        elif cmd[0] == "C" and len(cmd) == 1:
            pass
        else:
            continue
        print_board(board)


if __name__ == '__main__':
    main()
