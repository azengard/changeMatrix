
def read_sequence():  # Read and validate a sequence of commands.

    CharValid = ("ICLVHKFSX")

    Sqc = input("Digite um comando: ").upper()

    Sqc = Sqc.split()

    for Char in CharValid:

        if Char == Sqc[0] and not "":

            return Sqc

    else:

        return False


def create_array(Cmd):  # Create a array with the Command I.

    Board = []

    for x in range(int(Cmd[2])):

        Board.append(["O"] * int(Cmd[1]))

    return Board


def print_board(Board):

    for row in Board:

        print("".join(row))


Cmd = read_sequence()  # aa

Board = create_array(Cmd)  # aa

print_board(Board)
