import pygame
import random

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
BLOCKSIZE = 20
BOARD = [[0 for y in range(HEIGHT//BLOCKSIZE)] for x in range(WIDTH//BLOCKSIZE)]





test_state = [[0, 0, 1, 0], 
              [0, 0, 1, 0],
              [0, 0, 1, 0]] 






def DrawBOARD(): # Fill each box with white if the array contains a one
    for x in range(WIDTH//BLOCKSIZE):
        for y in range(HEIGHT//BLOCKSIZE):
            rect = pygame.Rect(x * BLOCKSIZE, y * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)

            if BOARD[x][y] == 1:
                pygame.draw.rect(screen, WHITE, rect, 16)
            
    
    
# TODO: Figure out how to change color of a cell if left click is pressed
def SetCells():
    # Assuming cursor_pos = nBlockSize + c then n = cursor_pos/BlockSize - c/BlockSize
    state = pygame.mouse.get_pressed() # state = (leftClick, middleClick, rightClick)
    
    if state[0] == 1: 
        cursor_pos = pygame.mouse.get_pos()
        
        x = cursor_pos[0]//BLOCKSIZE
        y = cursor_pos[1]//BLOCKSIZE
        if x < WIDTH//BLOCKSIZE and y < HEIGHT//BLOCKSIZE:        
            print(f"LEFT KEY GOT PRESSED on ({x},{y}) BLOCK")
            if BOARD[x][y] == 0:
                BOARD[x][y] = 1
             
    

def DrawCells():
    pass
    

def DrawGame(): 
    DrawBOARD()
    DrawCells()
    pygame.display.update()



def main(): 
    
    


    running = True
    while running:

        

        clock.tick(FPS)     
        for event in pygame.event.get():        
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)
        DrawGame()
        SetCells()
        pygame.display.flip()       

    pygame.quit()
if __name__ == '__main__':
    main()
