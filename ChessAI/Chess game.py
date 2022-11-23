import pygame as pg
import sys, os
from Gamestate import game,moves,possible
from pygame.locals import *
pg.init()
white = (255,255,255)
bblack = (204,102,0)
bwhite = (255,178,102)
bred = (255,20,20)
pink = (200,50,50)
bsize = bwidth, bheight = (480,480)
board = pg.display.set_mode(bsize)
clicked = False
def draw():
    for i in range(0,8):
        for j in range(0,8):
            possible[i][j] = 0
    for i in range(1,8,2):
        for j in range(1,8,2):
            pg.draw.rect(board,bblack,pg.Rect(i*60,(j-1)*60,60,60))
            pg.draw.rect(board,bblack,pg.Rect((i-1)*60,j*60,60,60))
            pg.draw.rect(board,bwhite,pg.Rect((i*60,j*60,60,60)))
            pg.draw.rect(board,bwhite,pg.Rect((i-1)*60,(j-1)*60,60,60))
    if clicked and game[pos[1]][pos[0]] != None:
        x = game[pos[1]][pos[0]]
        y1,x1 = pos[1],pos[0]
        pg.draw.rect(board,bred,pg.Rect((x1)*60,(y1)*60,60,60))
        if x == "bR" or x == "wR":
            i = 1
            while y1+i < 8 and game[y1+i][x1] == None:
                possible[y1+i][x1] = 1
                i +=1
            i = 1
            while y1-i >= 0 and game[y1-i][x1] == None:
                possible[y1-i][x1] = 1
                i +=1
            i = 1
            while  x1+i < 8 and game[y1][x1+i] == None:
                possible[y1][x1+i] = 1
                i +=1
            i = 1
            while x1-i >= 0 and game[y1][x1-i] == None:
                possible[y1][x1-i] = 1
                i +=1
            
        if x == "bN" or x == "wN":
            a,b,c,d,e,f,g,h = x1+2,x1-2,x1+1,x1-1,y1+2,y1-2,y1+1,y1-1
            for i in range(-2,3,4):
                for j in range(-1,2,2):
                    if y1+i > -1 and y1 +i < 8 and x1 +j > -1 and x1+j <8:
                        if game[y1+i][x1+j] == None:
                            possible[y1+i][x1+j] = 1
            for i in range(-2,3,4):
                for j in range(-1,2,2):
                    if y1+j > -1 and y1 +j < 8 and x1 +i > -1 and x1+i <8:
                        if game[y1+j][x1+i] == None:
                            possible[y1+j][x1+i] = 1
        if x == "bP":
            i = 1
            while i < 3 and game[y1+i][x1] == None and y1+i<8:
                possible[y1+i][x1] = 1
                i += 1
        if x == "wP":
            i = 1
            while i < 3 and game[y1-i][x1] == None and y1-i<8:
                possible[y1-i][x1] = 1
                i += 1
        if x == "bB" or x == "wB":
            i = 1
            while y1+i < 8 and x1+i <8 and game[y1+i][x1+i] == None:
                possible[y1+i][x1+i] = 1
                i +=1
            i = 1
            while y1-i >= 0 and x1-i >= 0 and game[y1-i][x1-i] == None:
                possible[y1-i][x1-i] = 1
                i +=1
            i = 1
            while  x1+i < 8 and y1-i >= 0 and game[y1][x1+i] == None:
                possible[y1-i][x1+i] = 1
                i +=1
            i = 1
            while x1-i >= 0 and y1+i < 8 and game[y1][x1-i] == None:
                possible[y1+i][x1-i] = 1
                i +=1
        if x == "bQ" or x == "wQ":
            i = 1
            while y1+i < 8 and x1+i <8 and game[y1+i][x1+i] == None:
                possible[y1+i][x1+i] = 1
                i +=1
            i = 1
            while y1-i >= 0 and x1-i >= 0 and game[y1-i][x1-i] == None:
                possible[y1-i][x1-i] = 1
                i +=1
            i = 1
            while  x1+i < 8 and y1-i >= 0 and game[y1][x1+i] == None:
                possible[y1-i][x1+i] = 1
                i +=1
            i = 1
            while x1-i >= 0 and y1+i < 8 and game[y1][x1-i] == None:
                possible[y1+i][x1-i] = 1
                i +=1
            i = 1
            while y1+i < 8 and game[y1+i][x1] == None:
                possible[y1+i][x1] = 1
                i +=1
            i = 1
            while y1-i >= 0 and game[y1-i][x1] == None:
                possible[y1-i][x1] = 1
                i +=1
            i = 1
            while  x1+i < 8 and game[y1][x1+i] == None:
                possible[y1][x1+i] = 1
                i +=1
            i = 1
            while x1-i >= 0 and game[y1][x1-i] == None:
                possible[y1][x1-i] = 1
                i +=1
        if x == "bK" or x == "wK":
            if y1+1 < 8 and x1+1 <8 and game[y1+1][x1+1] == None:
                possible[y1+1][x1+1] = 1
            if y1-1 >= 0 and x1-1 >= 0 and game[y1-1][x1-1] == None:
                possible[y1-1][x1-1] = 1
            if  x1+1 < 8 and y1-1 >= 0 and game[y1][x1+1] == None:
                possible[y1-1][x1+1] = 1
            if x1-1 >= 0 and y1+1 < 8 and game[y1][x1-1] == None:
                possible[y1+1][x1-1] = 1
            if y1+1 < 8 and game[y1+1][x1] == None:
                possible[y1+1][x1] = 1
            if y1-1 >= 0 and game[y1-1][x1] == None:
                possible[y1-1][x1] = 1
            if x1+1 < 8 and game[y1][x1+1] == None:
                possible[y1][x1+1] = 1
            if x1-1 >= 0 and game[y1][x1-1] == None:
                possible[y1][x1-1] = 1
                   




while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            pos = ((pos[0]//60),(pos[1]//60))
            print(pos)
            clicked = True
    board.fill(white)
    draw()
    for i in range(0,8):
        for j in range(0,8):
            if game[i][j] != None:
                board.blit(pg.image.load("C:\\Users\\joeok\\Downloads\\chess-main\\chess-main\\Game\\images\\"+game[i][j]+".png"),(j*60,i*60))
    for i in range(0,8):
        for j in range(0,8):
            if possible[i][j] == 1:
                    pg.draw.rect(board,pink,pg.Rect(j*60,i*60,60,60))

    
    pg.display.flip()
