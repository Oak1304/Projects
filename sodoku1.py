from asyncio import events
import pygame, sys
from pygame.locals import *
# Initializes pygame
pygame.init()
clock = pygame.time.Clock()
# Defines the screen and sodoku board
screen = pygame.display.set_mode((1500,1000))
board = pygame.Surface([900,900])
textbox = pygame.Surface([280,40])
# Defines the text parameters
fontn = pygame.font.SysFont(None, 90)
fontl = pygame.font.SysFont(None, 60)
grid =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
clicked = False
clicked1 = False
complete = 0
verify = False
def newlist(list,n):
    return [x[n] for x in list]
while True:
    # Ensures programme quits when pressing exit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # Drawing the sodoku board outline
    screen.fill((255,255,255))
    screen.blit(board,(50,50))
    board.fill((255,255,255), board.get_rect().inflate(-10,-10))
    # Draws thicker 3x3 grid and thinner 9x9 grid
    for x in range (300, 601, 300):
        pygame.draw.line(board, (0,0,0), (x,0), (x, 900), 5)
        pygame.draw.line(board, (0,0,0), (0,x), (900,x), 5)
    for x in range (100, 801, 100):
        pygame.draw.line(board, (0,0,0), (x,0), (x,900), 2)
        pygame.draw.line(board, (0,0,0), (0,x), (900,x), 2)

    # Displays numbers in the grid
    for i in range(0,9):
        for x in range(0,9):
            if grid[i][x] != 0:
                n = fontn.render(str(grid[i][x]), True, (0,0,0))
                board.blit(n, (38 + i*100, 25 + x*100))
    # Checks whether mouse has been clicked
    if not clicked and complete < 9:
        enter = fontl.render('Select a cell', True, (235,120,0))
        screen.blit(enter, (1000,415))
        if pygame.mouse.get_pressed()[0]:
            clicked = True
            clicked1 = True
    # Displays 'Enter number' until number is pressed
    elif clicked:
        if clicked1:
            where = pygame.mouse.get_pos()
            cellx = ((where[0]-50)//100)
            celly =  ((where[1]-50)//100)
            clicked1 = False
        screen.blit(textbox, (1000,415))
        text = fontl.render('Enter number', True, (255,255,255))
        screen.blit(text, (1000,415))
        # If a number is pressed, it will replace the number in the cell
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.unicode.isdigit():
                grid[cellx][celly] = int(event.unicode)
                clicked = False
    
    for i in range(0,9):
        if not 0 in grid[i]:
            complete += 1
    # Only runs the statement if all cells are nonzero
    if complete == 9:
        for i in range(0,9):
            # Horizontal rule
            if len(grid[i]) != len(set(grid[i])):
                verify = False
            # Vertical rule
            elif len(newlist(grid,i)) != len(set(newlist(grid,i))):
                verify = False
            else:
                verify = True
        # 3x3 grid rule
        for i in range(0,9,3):
            for j in range(0,9,3):
                for x in range(1,3):
                    for n in range (0,3):
                        if grid[i][j+n] == grid[i+x][j]:
                            verify = False
                        elif grid[i+n][j] == grid[i][j+x]:
                            verify = False
        # Shows 'YOU WIN!' if you complete sodoku correctly
        if verify:
            win = fontl.render('YOU WIN!', True, (0,225,75))
            screen.blit(win, (1000,100))
        # Shows 'Incorrect, try again.' if you complete sodoku incorrectly
        elif not verify:
            lose = fontl.render('Incorrect, try again.', True, (225,0,25))
            screen.blit(lose, (1000,100))
        
            

    complete = 0
    # Updates the screen 
    pygame.display.flip()
    # Ensures game renders at 120fps
    clock.tick(120)
