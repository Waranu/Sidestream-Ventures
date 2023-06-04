import pygame
import copy
from time import sleep

WIDTH = 1000
HEIGHT = 800
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (50, 50, 50)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()    
BLOCKSIZE = 40
BoardRows = WIDTH//BLOCKSIZE
BoardColumns = HEIGHT//BLOCKSIZE









def DrawBOARD(CurrentBoard, NextBOARD): # Fill each box with white if the array contains a one
    for x in range(BoardRows):
        for y in range(BoardColumns):
            rect = pygame.Rect(x * BLOCKSIZE, y * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(screen, pygame.Color('dimgray'), rect, 1)
            if NextBOARD[x][y] == 1:
                pygame.draw.rect(screen, WHITE, rect)
               

     
    
# TODO: Figure out how to change color of a cell if left click is pressed
def SetCells(NextBOARD):
    # Assuming cursor_pos = nBlockSize + c then n = cursor_pos/BlockSize - c/BlockSize
    MouseState = pygame.mouse.get_pressed() # STATE = (leftClick, middleClick, rightClick)
    cursor_pos = pygame.mouse.get_pos()
    x = cursor_pos[0]//BLOCKSIZE
    y = cursor_pos[1]//BLOCKSIZE
    if x < BoardRows and y < BoardColumns:        
        if MouseState[0] == 1: 
            if NextBOARD[x][y] == 0:
                NextBOARD[x][y] = 1
        elif MouseState[2] == 1:
            if NextBOARD[x][y] == 1:
                NextBOARD[x][y] = 0
             
    
def CheckNeighbour(CurrentBOARD, NextBOARD): 
    

            
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
           
            if CurrentBOARD[x][UP] == 1: # TOP neighbour
                numNeighbours += 1
                print(f"Neighbour cell of ({x},{y}) at ({x},{UP})")
                # print(f"No. of Neightbour of ({x},{y}): {numNeighbours}")
                            
            if CurrentBOARD[x][DOWN] == 1: # Bottom neighbour
                numNeighbours += 1
                print(f"Neighbour cell of ({x},{y}) at ({x},{DOWN})")
                # print(f"No. of Neightbour of ({x},{y}): {numNeighbours}")         
                            
                            
            if CurrentBOARD[LEFT][UP] == 1: # Top Left Neighbour
                numNeighbours += 1
                print(f"Neighbour cell of ({x},{y}) at ({LEFT},{UP})")
                # print(f"No. of Neightbour of ({x},{y}): {numNeighbours}") 
                    
                            
            if CurrentBOARD[LEFT][DOWN] == 1: # Top Right Neighbour
                numNeighbours += 1
                print(f"Neighbour cell of ({x},{y}) at ({LEFT},{DOWN})")
                # print(f"No. of Neightbour of ({x},{y}): {numNeighbours}")
                        
            if CurrentBOARD[RIGHT][UP] == 1: # 
                numNeighbours += 1
                print(f"Neighbour cell of ({x},{y}) at ({RIGHT},{UP})")
                # print(f"No. of Neightbour of ({x},{y}): {numNeighbours}")
                                
            if CurrentBOARD[RIGHT][DOWN] == 1:
                numNeighbours += 1
                print(f"Neighbour cell of ({x},{y}) at ({RIGHT},{DOWN})")
                # print(f"No. of Neightbour of ({x},{y}): {numNeighbours}")
                                
            if CurrentBOARD[LEFT][y] == 1:
                numNeighbours += 1
                print(f"Neighbour cell of ({x},{y}) at ({LEFT},{y})")
                # print(f"No. of Neightbour of ({x},{y}): {numNeighbours}")
                                
            if CurrentBOARD[RIGHT][y] == 1:
                numNeighbours += 1
                print(f"Neighbour cell of ({x},{y}) at ({RIGHT},{y})")
                # print(f"No. of Neightbour of ({x},{y}): {numNeighbours}")
            
            
                
            if CurrentBOARD[x][y] == 1 and numNeighbours < 2: 
                NextBOARD[x][y] = 0
            
            if CurrentBOARD[x][y] == 1 and numNeighbours > 3: 
                NextBOARD[x][y] = 0
            
            if CurrentBOARD[x][y] == 1 and (numNeighbours == 2 or numNeighbours == 3): 
                NextBOARD[x][y] = 1
            
            if CurrentBOARD[x][y] == 0 and numNeighbours == 3: 
                NextBOARD[x][y] = 1
            
    sleep(1/2)





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
        screen.fill(BLACK)
        
        
        if STATE == RUNNING: 
            CheckNeighbour(currentBOARD, nextBOARD)
        elif STATE == PAUSE: 
            SetCells(nextBOARD)
                
        
        currentBOARD = copy.deepcopy(nextBOARD)  
        DrawBOARD(currentBOARD, nextBOARD)
        pygame.display.flip()       
        clock.tick(FPS)     
        
        

    pygame.quit()
if __name__ == '__main__':
    main()
