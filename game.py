#!/usr/bin/env python
#! -*- coding: utf-8 -*-

# Goal Draw a Board with PyGame
import pygame

# Config.py
GRID_WIDTH = 8 
GRID_HEIGHT= 8

SQUARE_WIDTH = 50
SQUARE_HEIGHT = 50

MARGIN = 20

TITLE = "PyChesp"

DEBUG = True

# After Config

WINDOW_HEIGHT = SQUARE_HEIGHT * GRID_HEIGHT + MARGIN*2
WINDOW_WIDTH = SQUARE_WIDTH * GRID_WIDTH + MARGIN*2

WINDOW_SIZE = [WINDOW_WIDTH,WINDOW_HEIGHT]

# Define some colors

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREY     = ( 50 , 50 , 50)
# GREEN    = (   0, 255,   0)
# RED      = ( 255,   0,   0)

grid = []

def debug(var):
    if DEBUG:
        print var

def _get_grid_color():
    color = BLACK

# print black / white to the current grid
def print_grid(screen):
    color = BLACK
    def change_color(color):
        if color == BLACK:
            color = WHITE
            debug('Color : WHITE')
        else:
            color = BLACK
            debug('Color : BLACK')
        return color
    for w in xrange(0,GRID_WIDTH):
        for h in xrange(0,GRID_HEIGHT):
            color = change_color(color)
            rect = [MARGIN+w*SQUARE_WIDTH,MARGIN+h*SQUARE_HEIGHT,SQUARE_WIDTH,SQUARE_HEIGHT]
            pygame.draw.rect(screen,color,rect)
            print "Width %d , Height %d" % ( w , h)
            print rect
        color = change_color(color)
    pass

# return the current grid for the position
def get_grid_from_pos(pos):
    y , x = pos
    pos_x = 8 - (x - MARGIN) / SQUARE_WIDTH
    pos_y = (y - MARGIN) / SQUARE_HEIGHT + 1
    print pos_y , pos_x

def main():
    pygame.init()
    screen = pygame.display.set_mode([WINDOW_WIDTH,WINDOW_HEIGHT])
    pygame.display.set_caption('')
    done = False
    clock = pygame.time.Clock()
    screen.fill(GREY)
    print_grid(screen)

    while done is False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                get_grid_from_pos(pos)

        clock.tick(20)
        # Update the screen
        pygame.display.flip()
    pass

if __name__ == '__main__':
    main()
