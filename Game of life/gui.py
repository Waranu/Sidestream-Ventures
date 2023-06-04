import pygame
import copy
from time import sleep
from random import randint

WIDTH = 1200
HEIGHT = 900
FPS = 60

WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (50, 50, 50)
ORANGE = (255, 119, 66)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()    
BLOCKSIZE = 30
BoardRows = WIDTH//BLOCKSIZE
BoardColumns = HEIGHT//BLOCKSIZE









def DrawBOARD(CurrentBoard): # Fill each box with white if the array contains a one
    for x in range(BoardRows):
        for y in range(BoardColumns):
            block = pygame.Rect(x * BLOCKSIZE, y * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(screen, pygame.Color('dimgray'), block, 1)
            if CurrentBoard[x][y] == 1:
                cell = pygame.Rect(x * BLOCKSIZE, y * BLOCKSIZE, BLOCKSIZE - 2, BLOCKSIZE - 2)
                pygame.draw.rect(screen, ORANGE, cell)
               

     
    
# TODO: Figure out how to change color of a cell if left click is pressed
def SetCells(updatedBoard):
    # Assuming cursor_pos = nBlockSize + c then n = cursor_pos/BlockSize - c/BlockSize
    MouseState = pygame.mouse.get_pressed() # STATE = (leftClick, middleClick, rightClick)
    cursor_pos = pygame.mouse.get_pos()
    x = cursor_pos[0]//BLOCKSIZE
    y = cursor_pos[1]//BLOCKSIZE
    if x < BoardRows and y < BoardColumns:        
        if MouseState[0] == 1: 
            if updatedBoard[x][y] == 0:
                updatedBoard[x][y] = 1
        elif MouseState[2] == 1:
            if updatedBoard[x][y] == 1:
                updatedBoard[x][y] = 0
             
    
def CheckNeighbour(CurrentBoard, updatedBoard): 
    

            
    UP = 0 
    DOWN = 0
    LEFT = 0
    RIGHT = 0
     
    for x in range(BoardRows):
        for y in range(BoardColumns):
            numNeighbours = 0
            #FIXME: What to do when x or y = 0 ? Assuming A < 0 then A % B returns B-A
            LEFT = (x - 1) % BoardRows  # LEFT = ROWS - (0 - 1)
            RIGHT = (x + 1) % BoardRows
            UP = (y - 1) % BoardColumns
            DOWN = (y + 1) % BoardColumns
               
            # Check for numNeighbours
           
            if CurrentBoard[x][UP] == 1: # TOP neighbour
                numNeighbours += 1
            
                            
            if CurrentBoard[x][DOWN] == 1: # Bottom neighbour
                numNeighbours += 1
                     
                            
                            
            if CurrentBoard[LEFT][UP] == 1: # Top Left Neighbour
                numNeighbours += 1
             
                    
                            
            if CurrentBoard[LEFT][DOWN] == 1: # Top Right Neighbour
                numNeighbours += 1
            
                        
            if CurrentBoard[RIGHT][UP] == 1: # 
                numNeighbours += 1
            
                                
            if CurrentBoard[RIGHT][DOWN] == 1:
                numNeighbours += 1
            

            if CurrentBoard[LEFT][y] == 1:
                numNeighbours += 1
            
                                
            if CurrentBoard[RIGHT][y] == 1:
                numNeighbours += 1
            
            
            
                
            if CurrentBoard[x][y] == 1 and numNeighbours < 2: 
                updatedBoard[x][y] = 0
            
            elif CurrentBoard[x][y] == 1 and numNeighbours > 3: 
                updatedBoard[x][y] = 0
            
            elif CurrentBoard[x][y] == 1 and (numNeighbours == 2 or numNeighbours == 3): 
                updatedBoard[x][y] = 1
            
            elif CurrentBoard[x][y] == 0 and numNeighbours == 3: 
                updatedBoard[x][y] = 1
            
    sleep(0.055)





def main(): 
    PAUSE = 0
    RUNNING = 1
    STATE = PAUSE
    currentBOARD = [[0 for y in range(BoardColumns)] for x in range(BoardRows)]
    nextBOARD = [[0 for y in range(BoardColumns)] for x in range(BoardRows)]

    while True:     

        
        

        for event in pygame.event.get():        
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    STATE = PAUSE
                if event.key == pygame.K_s:
                    STATE = RUNNING
                if event.key == pygame.K_c and STATE == PAUSE:
                    nextBOARD = [[0 for y in range(BoardColumns)] for x in range(BoardRows)]
                    
                if event.key == pygame.K_r and STATE == PAUSE:
                    nextBOARD = [[randint(0, 1) for y in range(BoardColumns)] for x in range(BoardRows)]
                    
        screen.fill(BLACK)
        
        
        if STATE == RUNNING: 
            CheckNeighbour(currentBOARD, nextBOARD)
        elif STATE == PAUSE: 
            SetCells(nextBOARD)
                
        
        currentBOARD = copy.deepcopy(nextBOARD)  
        DrawBOARD(currentBOARD)
        pygame.display.update()      
        clock.tick(FPS)     
        
        

    pygame.quit()
if __name__ == '__main__':
    main()
