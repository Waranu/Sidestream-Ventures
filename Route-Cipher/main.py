from random import randint

# Rules of Game of life 
# Rule 1: Any cell with <= 2 or 3 neighbours dies
# Rule 2: Any cell with  >= 4 neighbours dies 
# Rule 3: Any dead cell with exactly 3 neighbours comes alive
# 0 = Dead Cell and 1 = Alive Cell



ROWS = 10
COLS = 10
BOARD = [[0 for j in range(COLS)] for x in range(ROWS)]



# TODO: Popularize the board via the random function

def FillboardRandomly(board):
     for i in range(ROWS):
          for j in range(COLS):
               board[i][j] = randint(0, 1)

def Printboard(board):
     for i in board:
          print(i)




def main():
     FillboardRandomly(BOARD)
     Printboard(BOARD)




if __name__ == '__main__':
     main()