from random import randint
from time import sleep

# Any live cell with < 2 live numNeighbours dies, as if by underpopulation.
# Any live cell with 2 <= x <= 3 live numNeighbours lives on to the next generation.
# Any live cell with > 3 numNeighbours dies, as if by overpopulation.
# Any dead cell with = 3 three live numNeighbours becomes a live cell, as if by reproduction.



ROWS = 10
COLS = 10
BOARD = [[0 for j in range(COLS)] for x in range(ROWS)]



# TODO: Popularize the board via the random function

def FillboardRandomly(board):
     randomRow = randint(0, 3)
     randomColumn = randint(0, 3)
     
     
     for i in range(ROWS-3):
          for j in range(COLS-3):
               board[i+randomRow][j+randomColumn] = randint(0, 1)

def Printboard(board):
     for i in board:
          print(i)
     print("\n")

# TODO: Try the compute intensive approach
     # TODO: Code the basic Rules stated above




def CreateNextState(board):
     numNeighbours = 0
     UP = 0 
     DOWN = 0
     LEFT = 0
     RIGHT = 0
     
     for x in range(ROWS):
          for y in range(COLS):
               #FIXME: What to do when x or y = 0 ? 
               LEFT = (x - 1) % ROWS
               RIGHT = (x + 1) % ROWS
               UP = (y - 1) % COLS
               DOWN = (y + 1) % COLS
               
               # Check for numNeighbours
               
               if board[x][UP] == 1:
                    numNeighbours += 1
                         
               if board[x][DOWN] == 1:
                    numNeighbours += 1
                         
               if board[LEFT][UP] == 1:
                    numNeighbours += 1
                         
               if board[LEFT][DOWN] == 1:
                    numNeighbours += 1
                         
               if board[RIGHT][UP] == 1:
                    numNeighbours += 1
                              
               if board[RIGHT][DOWN] == 1:
                    numNeighbours += 1
                              
               if board[LEFT][y] == 1:
                    numNeighbours += 1
                              
               if board[RIGHT][y] == 1:
                    numNeighbours += 1
                
               if numNeighbours > 0:
                    if (numNeighbours == 2 or numNeighbours == 3) and board[x][y] == 1:
                         board[x][y] = 1
                    elif numNeighbours == 3 and board[x][y] == 0:
                         board[x][y] = 1
                    else: 
                         board[x][y] = 0
                         numNeighbours = 0     
     sleep(1.0)



def main():
     FillboardRandomly(BOARD)
     Printboard(BOARD)
     
     run = True
     
     while run:
          CreateNextState(BOARD)
          Printboard(BOARD)



if __name__ == '__main__':
     main()