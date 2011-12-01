#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")

########################
from view import piece
import config

import pygame
# EventHandler

init_data = {
    'king'  : [(5,1)],
    'queen' : [(4,1)],
    'rook'  : [(1,1),(8,1)], #车
    'bishop': [(3,1),(6,1)], #象
    'knight': [(2,1),(7,1)], #马
    'pawn':   [(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2)] #兵
    }

def init_make_piece_list():
    import game
    piece_list = pygame.sprite.RenderPlain()
    def place(color):
        for name in init_data:
            pos_arr = init_data[name]
            for pos in pos_arr:
                if color == 'black':
                    x,y = pos
                    y = 9-y
                    pos = (x,y)
                block = piece.make(color,name)
                block.move(pos)
                piece_list.add(block)
    place('black')
    place('white')
    return piece_list
# _start main loop and handle events
class BoardController(object):
    def __init__(self):
        



        pass


