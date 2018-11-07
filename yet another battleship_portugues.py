from random import randint
board = []
board_size = 4
number_of_turns = 10
turn = 0

for x in range(board_size):
    board.append(["O"] * board_size)


def print_board(board):
    for row in board:
        print(' '.join(row))


def random_num(board):
    return randint(0, (len(board) - 1))


def ppv(x):
    nx = x.replace(',', '.')
    if nx.count('.') == 0:
        fx = int(nx)
    else:
        fx = float(nx)
    return fx


def formatação(m):
    while True:
        try:
            v = ppv(str(input(m)))
            return v
        except ValueError:
            print('\nVocê digitou um ou mais caracteres inválidos. '
                  'Digite apenas números, separando as casas decimais com ponto ou vírgula!\n')
            continue


ship_row = random_num(board)
ship_col = random_num(board)

while turn <= number_of_turns:

    print_board(board)

    if turn == (number_of_turns - 1):
        answear = input('Você quer continuar jogando?\n')
        if answear == 'sim':
            turn = 0
        else:
            print('Fim de Jogo')
            break

    else:
        print('Turno ' + str(turn + 1))

        guess_row = formatação("Chute a fileira: ")
        guess_col = formatação("Chute a coluna: ")
        guess_row -= 1
        guess_col -= 1

        if guess_row == ship_row and guess_col == ship_col:
            print("\nParabéns! Você destruiu o navio!\n")
            board[guess_row][guess_col] = "Y"
            print_board(board)
            break
        else:
            if (guess_row < 0 or guess_row > (board_size - 1) or (guess_col < 0 or guess_col > (board_size - 1))):
                print("\nNossa! Passou longe!\n")
            elif(board[guess_row][guess_col] == "X"):
                print("\nVocê já chutou essa.\n")
            else:
                print("\nVocê errou o navio!\n")
                board[guess_row][guess_col] = "X"
        turn += 1
