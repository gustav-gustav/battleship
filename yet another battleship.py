from random import randint
import datetime as f
cmd_list = []
abertura = 'Welcome to Battleship'
game_modes = '\nChoose your gamemode:\n1 - Easy \n2 - Medium\n3 - Hard\n'
print(f.date.today())


def print_list_(list_):
    for x in list_:
        print(x)


def ppv(x):
    nx = x.replace(',', '.')
    if nx.count('.') == 0:
        fx = int(nx)
    else:
        fx = float(nx)
    return fx


def format_(m):
    while True:
        try:
            v = ppv(str(input(m)))
            return v
        except ValueError:
            print('\nYou typed one or more invalid characters. '
                  'Type only numbers!\n')
            continue


def game(board_size, number_of_turns):
    turn = 0
    board = [['0'] * board_size for x in range(board_size)]
    types = ['hor', 'ver']
    type_ = types[randint(0, 1)]
    # type_ = types[1]
    ship_list = []
    print(type_)

    def print_board(board):
        for row in board:
            print(' '.join(row))

    def verify(type_, rev=False):
        if rev:
            if type_ is 'hor':
                return 1
            else:
                return 0
        else:
            if  type_ is 'hor':
                return 0
            else:
                return 1

    def random_num(first=None, board_size=board_size):
        if  first == None:
            i = randint(0, (board_size - 1))
            j = randint(0, (board_size - 1))
            ship_list.append([i,j])
            return [i, j]
        else:
            index = verify(type_)
            rev_index = verify(type_, True)

            moving = randint((first[rev_index]-1), (first[rev_index]+1))
            constant = first[index]

            if moving == first[rev_index]:
                print(f'moving == first:\n{moving} == {first[index]}')
                random_num(first)

            elif moving < 0:
                print("out of domain, moving < board_size")
                random_num(first)

            elif moving > (board_size-1):
                print("out  of domain, moving > board_size")
                random_num(first)

            else:
                if type_ is "hor":
                    ship_list.append([constant, moving])
                elif type_ is "ver":
                    ship_list.append([moving, constant])

    first_point = random_num()
    random_num(first_point)
    # print(ship_list, '\n')
    # for points in ship_list:
    #     i, j = points
    #     board[i][j] = 'Y'

    # print_board(board)
    # ship_row = random_num(board)
    # ship_col = random_num(board)

    while turn <= number_of_turns:
        if turn == (number_of_turns - 1):
            answear = input('Do you want to keep playing?\n')
            if answear == 'yes':
                print('\n')
                turn = 0
            else:
                print('Game Over\n')
                break

        else:
            print_board(board)
            print('Turn ' + str(turn + 1))
            # print(ship_row + 1) for debugging
            # print(ship_col + 1)
            guess_row = format_("Guess Row: ")
            guess_col = format_("Guess Col: ")
            guess_row -= 1
            guess_col -= 1

            if guess_row == ship_row and guess_col == ship_col:
                print('\n')
                board[guess_row][guess_col] = "Y"
                print_board(board)
                print("\nCongratulations! You sunk my battleship!\n")
                break
            else:
                if (guess_row < 0 or guess_row > (board_size - 1) or (guess_col < 0 or guess_col > (board_size - 1))):
                    print("\nOops, that's not even in the ocean.\n")
                elif(board[guess_row][guess_col] == "X"):
                    print("\nYou guessed that one already.\n")
                else:
                    print("\nYou missed my battleship!\n")
                    board[guess_row][guess_col] = "X"
            turn += 1


def prompt():
    rotation = 0
    while True:
        if rotation < 1:
            print(abertura)

        print(game_modes)
        prompt = input('prompt:')
        print('\n')

        if prompt == 'cmd':
            print_list_(cmd_list)

        elif prompt == '3':
            game(5, 6)

        elif prompt == '2':
            game(4, 8)

        elif prompt == '1':
            game(3, 10)

        elif prompt == 'sair':
            break

        else:
            print('\nType a valid command')
        rotation += 1


prompt()
