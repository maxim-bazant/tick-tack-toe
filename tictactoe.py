import time

laps = 0
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def show_board():
    print("A" + "|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("B" + "|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("C" + "|" + board[6] + "|" + board[7] + "|" + board[8] + "|")
    print("  " + "A" + " " + "B" + " " + "C")


def write_x():
    x_position_of_x = input("In which line do you want to put your x? A, B or C: ")
    y_position_of_x = input("In which column do you want to put your x? A, B or C: ")

    if x_position_of_x.capitalize() == "A" and y_position_of_x.capitalize() == "A" and board[0] != "x" and board[0] != "o":
        board[0] = "x"

    elif x_position_of_x.capitalize() == "A" and y_position_of_x.capitalize() == "B" and board[1] != "x" and board[1] != "o":
        board[1] = "x"

    elif x_position_of_x.capitalize() == "A" and y_position_of_x.capitalize() == "C" and board[2] != "x" and board[2] != "o":
        board[2] = "x"

    elif x_position_of_x.capitalize() == "B" and y_position_of_x.capitalize() == "A" and board[3] != "x" and board[3] != "o":
        board[3] = "x"

    elif x_position_of_x.capitalize() == "B" and y_position_of_x.capitalize() == "B" and board[4] != "x" and board[4] != "o":
        board[4] = "x"

    elif x_position_of_x.capitalize() == "B" and y_position_of_x.capitalize() == "C" and board[5] != "x" and board[5] != "o":
        board[5] = "x"

    elif x_position_of_x.capitalize() == "C" and y_position_of_x.capitalize() == "A" and board[6] != "x" and board[6] != "o":
        board[6] = "x"

    elif x_position_of_x.capitalize() == "C" and y_position_of_x.capitalize() == "B" and board[7] != "x" and board[7] != "o":
        board[7] = "x"

    elif x_position_of_x.capitalize() == "C" and y_position_of_x.capitalize() == "C" and board[8] != "x" and board[8] != "o":
        board[8] = "x"

    else:
        print("This position is already taken or does not exist(like if you type D)")
        write_x()


def write_o():
    x_position_of_o = input("In which line do you want to put your o? A, B or C: ")
    y_position_of_o = input("In which column do you want to put your o? A, B or C: ")

    if x_position_of_o.capitalize() == "A" and y_position_of_o.capitalize() == "A" and board[0] != "x" and board[0] != "o":
        board[0] = "o"

    elif x_position_of_o.capitalize() == "A" and y_position_of_o.capitalize() == "B" and board[1] != "x" and board[1] != "o":
        board[1] = "o"

    elif x_position_of_o.capitalize() == "A" and y_position_of_o.capitalize() == "C" and board[2] != "x" and board[2] != "o":
        board[2] = "o"

    elif x_position_of_o.capitalize() == "B" and y_position_of_o.capitalize() == "A" and board[3] != "x" and board[3] != "o":
        board[3] = "o"

    elif x_position_of_o.capitalize() == "B" and y_position_of_o.capitalize() == "B" and board[4] != "x" and board[4] != "o":
        board[4] = "o"

    elif x_position_of_o.capitalize() == "B" and y_position_of_o.capitalize() == "C" and board[5] != "x" and board[5] != "o":
        board[5] = "o"

    elif x_position_of_o.capitalize() == "C" and y_position_of_o.capitalize() == "A" and board[6] != "x" and board[6] != "o":
        board[6] = "o"

    elif x_position_of_o.capitalize() == "C" and y_position_of_o.capitalize() == "B" and board[7] != "x" and board[7] != "o":
        board[7] = "o"

    elif x_position_of_o.capitalize() == "C" and y_position_of_o.capitalize() == "C" and board[8] != "x" and board[8] != "o":
        board[8] = "o"

    else:
        print("This position is already taken or does not exist(like if you type D)")
        write_o()


def check_if_x_won():
    # { check lines

    if board[0] == "x" and board[1] == "x" and board[2] == "x":
        print("X have won! You have 3 in line.")
        time.sleep(3)
        exit()

    elif board[3] == "x" and board[4] == "x" and board[5] == "x":
        print("X have won! You have 3 in line.")
        time.sleep(3)
        exit()

    elif board[6] == "x" and board[7] == "x" and board[8] == "x":
        print("X have won! You have 3 in line.")
        time.sleep(3)
        exit()

    # }

    # { check comlums

    elif board[0] == "x" and board[3] == "x" and board[6] == "x":
        print("X have won! You have 3 in column.")
        time.sleep(3)
        exit()

    elif board[1] == "x" and board[4] == "x" and board[7] == "x":
        print("X have won! You have 3 in column.")
        time.sleep(3)
        exit()

    elif board[2] == "x" and board[5] == "x" and board[8] == "x":
        print("X have won! You have 3 in column.")
        time.sleep(3)
        exit()

    # }

    # { check diagonals

    elif board[0] == "x" and board[4] == "x" and board[8] == "x":
        print("X have won! You have 3 in diagonal.")
        time.sleep(3)
        exit()

    elif board[2] == "x" and board[4] == "x" and board[6] == "x":
        print("X have won! You have 3 in diagonal.")
        time.sleep(3)
        exit()

    # }


def check_if_o_won():
    # { check lines

    if board[0] == "o" and board[1] == "o" and board[2] == "o":
        print("O have won! You have 3 in line")
        time.sleep(3)
        exit()

    elif board[3] == "o" and board[4] == "o" and board[5] == "o":
        print("O have won! You have 3 in line")
        time.sleep(3)
        exit()

    elif board[6] == "o" and board[7] == "o" and board[8] == "o":
        print("O have won! You have 3 in line")
        time.sleep(3)
        exit()

    # }

    # { check comlums

    elif board[0] == "o" and board[3] == "o" and board[6] == "o":
        print("O have won! You have 3 in column.")
        time.sleep(3)
        exit()

    elif board[1] == "o" and board[4] == "o" and board[7] == "o":
        print("O have won! You have 3 in column.")
        time.sleep(3)
        exit()

    elif board[2] == "o" and board[5] == "o" and board[8] == "o":
        print("O have won! You have 3 in column.")
        time.sleep(3)
        exit()

    # }

    # { check diagonals

    elif board[0] == "o" and board[4] == "o" and board[8] == "o":
        print("O have won! You have 3 in diagonal.")
        time.sleep(3)
        exit()

    elif board[2] == "o" and board[4] == "o" and board[6] == "o":
        print("O have won! You have 3 in diagonal.")
        time.sleep(3)
        exit()

    # }


def check_if_no_one_won():
    if board[0] != "-" and board[1] != "-" and board[2] != "-" and board[3] != "-" and board[4] != "-" and \
       board[5] != "-" and board[6] != "-" and board[7] != "-" and board[8] != "-" and board[9] != "-":
        print("No one have won")
        time.sleep(3)
        exit()


def game(rounds):
    while True:

        rounds += 1

        if rounds % 2 == 1:
            print("\n Now is x's turn")
            write_x()
            show_board()
            check_if_x_won()

        elif rounds % 2 == 0:
            print("\n Now is o's turn")
            write_o()
            show_board()
            check_if_o_won()

        check_if_no_one_won()


show_board()
game(laps)