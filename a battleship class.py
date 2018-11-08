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


class Battleship():
    def __init__(self, board_size, number_of_turns):
        types = ['hor', 'ver']
        self.board_size = board_size
        self.number_of_turns = number_of_turns
        self.turn = 0
        self.board = [['0'] * board_size for x in range(board_size)]
        self.type_ = types[randint(0, 1)]
        self.ship_list = []
        self.game()

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def verify(self, rev=False):
        if rev:
            if self.type_ is 'hor':
                return 1
            else:
                return 0
        else:
            if self.type_ is 'hor':
                return 0
            else:
                return 1

    def random_num(self, first=None):
        if first == None:
            i = randint(0, (self.board_size - 1))
            j = randint(0, (self.board_size - 1))
            self.ship_list.append([i, j])
            return [i, j]
        else:
            index = self.verify()
            rev_index = self.verify(True)

            moving = randint((first[rev_index]-1), (first[rev_index]+1))
            constant = first[index]

            if moving == first[rev_index]:
                # print(f'moving == first:\n{moving} == {first[index]}')
                self.random_num(first)

            elif moving < 0:
                # print("out of domain, moving < self.board_size")
                self.random_num(first)

            elif moving > (self.board_size-1):
                # print("out  of domain, moving > board_size")
                self.random_num(first)

            else:
                if self.type_ is "hor":
                    self.ship_list.append([constant, moving])
                elif self.type_ is "ver":
                    self.ship_list.append([moving, constant])

    def game(self):
        self.random_num()
        while self.turn <= self.number_of_turns:
            if self.turn == (self.number_of_turns - 1):
                answear = input('Do you want to keep playing?\n')
                if answear == 'yes':
                    print('\n')
                    self.turn = 0
                else:
                    print('Game Over\n')
                    break

            else:
                self.print_board()
                print('Turn ' + str(self.turn + 1))
                guess_row = format_("Guess Row: ")
                guess_col = format_("Guess Col: ")

                for point in self.ship_list:
                    print(point)
                    if guess_row == point[0] and guess_col == point[1]:
                        print('\n')
                        self.board[guess_row][guess_col] = "Y"
                        self.print_board()
                        print("\nCongratulations! You sunk my battleship!\n")
                        break
                    else:
                        if (guess_row < 0 or guess_row > (self.board_size - 1) or (guess_col < 0 or guess_col > (self.board_size - 1))):
                            print("\nOops, that's not even in the ocean.\n")
                        elif (self.board[guess_row][guess_col] == "X"):
                            print("\nYou guessed that one already.\n")
                        else:
                            print("\nYou missed my battleship!\n")
                            self.board[guess_row][guess_col] = "X"
                self.turn += 1


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
            Battleship(5, 6)

        elif prompt == '2':
            Battleship(4, 8)

        elif prompt == '1':
            Battleship(3, 10)

        elif prompt == 'sair':
            break

        else:
            print('\nType a valid command')
        rotation += 1


prompt()