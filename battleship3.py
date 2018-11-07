turns = 5

from random import randint


#creates the board
board = []

for x in range(5):
  board.append(["O"] * 5)


#function that prints the board
def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)



#define random row
def random_row(board):
  return randint(0, len(board) - 1)
#define random collumn
def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


#use this for ddebugging
#print (ship_row)
#print (ship_col)




for turn in range(1, turns):

  print ('Turn ' + str(turn)
  
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  i guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sunk my battleship!")
    break
  else:
    if turn == turns - 1:
      print('\nGame Over')
    elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print ("Oops, that's not even in the ocean.")
    elif(board[guess_row][guess_col] == "X"):
      print ("You guessed that one already.")
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
      print_board(board)
    turn += 1
  # Print (turn + 1) here!'''
    


    #motherfucker man
