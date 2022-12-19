from random import randint

board = []


for x in range(0, 10):
  board.append(["O"] * 10)




def print_board(board):
  for row in board:
    print (" ".join(row))




def random_row(board):
  return randint(1, len(board) - 2)

def random_col(board):
  return randint(1, len(board[0]) - 2)
for x in range(2):
  ship_row = []
  ship_row = random_row(board)
  ship_col = random_col(board)





for turn in range(8):
    print ("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
      board[ship_row][ship_col] = "W"
      print ("Congratulations! You sank my battleship!")
      print_board(board)
      break
    else:
      if (guess_col==ship_col+1 and guess_row==ship_row) or (guess_col==ship_col-1 and guess_row==ship_row) or (guess_col==ship_col and guess_row==ship_row+1) or (guess_col==ship_col and guess_row==ship_row-1):
        board[guess_row][guess_col] = "Y"
        print("You gueesed a rear part of the ship")
        if (turn == 7):
          print("Game Over")
          board[ship_row][ship_col] = "L"
          print("The battleship was located at: " + str(ship_row) + " " + str(ship_col))
      elif guess_row not in range(10) or \
        guess_col not in range(10):
        print ("Oops, that's not even in the ocean.")
      elif board[guess_row][guess_col] == "X":
        print( "You guessed that one already." )
      else:
        print ("You missed my battleship!")
        if(turn == 7):
          print ("Game Over")
          board[ship_row][ship_col] = "L"
          print ("The battleship was located at: " + str(ship_row) + " " + str(ship_col))
        board[guess_row][guess_col] = "X"
      print_board(board)