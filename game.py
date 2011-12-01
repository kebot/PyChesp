#!/usr/bin/env python
#! -*- coding: utf-8 -*-

# Goal Draw a Board with PyGame
import pygame
import os,sys
import random

from config import *
from chess import piece

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

# print black / white to the current grid
def print_grid(screen):
    color_a = GREY
    color_b = WHITE
    color = color_a
    def change_color(color):
        if color == color_a:
            color = color_b
            # debug('Color : WHITE')
        else:
            color = color_a
            # debug('Color : BLACK')
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

def drawImage( screen ,img , pos ):
    path = os.path.join(DOCROOT,"images",img+".png")
    # print path
    image = pygame.image.load(path).convert_alpha()#.convert()
    screen.blit( image , pos )

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

    # drawImage(screen,"black_king",[0,0])
    block = piece.Knight()
    piece_list = pygame.sprite.RenderPlain()
    
    block.rect.x = random.randrange(WINDOW_WIDTH)
    block.rect.y = random.randrange(WINDOW_HEIGHT)

    piece_list.add( block )

    while done is False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                get_grid_from_pos(pos)
        piece_list.draw(screen)
        clock.tick(20)
        pygame.display.flip()
    pass

if __name__ == '__main__':
    main()
