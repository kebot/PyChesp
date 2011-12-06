#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Views Based On Pygame
import pygame
from event import *

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREY     = ( 50 , 50 , 50)
# GREEN    = (   0, 255,   0)
# RED      = ( 255,   0,   0)
from config import *

class EventBasedView(object):
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)
    
    def Notify(self,event):
        pass

class PygameView(EventBasedView):
    """ ... """
    GREY     = ( 50 , 50 , 50)
    WINDOW_HEIGHT = SQUARE_HEIGHT * GRID_HEIGHT + MARGIN*2
    WINDOW_WIDTH = SQUARE_WIDTH * GRID_WIDTH + MARGIN*2
    WINDOW_SIZE = [WINDOW_WIDTH,WINDOW_HEIGHT]

    def __init__(self,evManager):
        super(PygameView,self).__init__(evManager)
        pygame.init()
        screen = pygame.display.set_mode(self.WINDOW_SIZE)
        screen.fill(self.GREY)
        self.board = BoardView(evManager,screen)

    def Notify(self,event):
        if isinstance(event,TickEvent):
            # pygame.display.flip()
            pass

#----------------------------------------------------------------------------------------------
import piece
class BoardView(EventBasedView):
    """Nothing"""
    def __init__(self,evManager,screen):
        super(BoardView, self).__init__(evManager)
        self.screen = screen
        self.piece_list = pygame.sprite.RenderPlain()

    def Notify(self,event):
        if isinstance(event,TickEvent):
            self.screen.fill( WHITE )
            self._build_board()
            self.piece_list.draw(self.screen)
            pygame.display.flip()
        elif isinstance(event,PlacePieceEvent):
            self.placeChess(event.piece)
        elif isinstance(event,GameStartedEvent):
            self._build_board()

    def placeChess(self,p):
        block = piece.make(p.player.color,p.name,self.piece_list)
        block.move(p.pos)
        p.bind(block)
        self.piece_list.add(block)

    def _build_board(self):
        # print "Build the board."
        color_a = GREY
        color_b = WHITE
        color = color_a
        def change_color(color):
            if color == color_a:
                color = color_b
            else:
                color = color_a
            return color
        for w in xrange(0,GRID_WIDTH):
            for h in xrange(0,GRID_HEIGHT):
                color = change_color(color)
                rect = [MARGIN+w*SQUARE_WIDTH,MARGIN+h*SQUARE_HEIGHT,SQUARE_WIDTH,SQUARE_HEIGHT]
                pygame.draw.rect(self.screen,color,rect)
            color = change_color(color)
        pass

import unittest
class test(unittest.TestCase):
    def setUp(self):
        pass
    def test_run(self):
        pass

if __name__ == '__main__':
    unittest.main()
