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

# class ClassName(object):
    # """docstring for ClassName"""
    # def __init__(self, arg):
        # super(ClassName, self).__init__()
        # self.arg = arg

class PygameView(EventBasedView):
    """ ... """
    GREY     = ( 50 , 50 , 50)
    WINDOW_HEIGHT = SQUARE_HEIGHT * GRID_HEIGHT + MARGIN*2
    WINDOW_WIDTH = SQUARE_WIDTH * GRID_WIDTH + MARGIN*2
    WINDOW_SIZE = [WINDOW_WIDTH,WINDOW_HEIGHT]
    def __init__(self,evManager):
        super(PygameView,self).__init__(evManager)
        # self.evManager = evManager
        # self.evManager.RegisterListener(self)
        pygame.init()
        screen = pygame.display.set_mode(self.WINDOW_SIZE)
        screen.fill( self.GREY )
        self.board = BoardView(evManager,screen)

    def Notify(self,event):
        if isinstance(event,TickEvent):
            pygame.display.flip()

#----------------------------------------------------------------------------------------------
default_chess_data = {
    'king'  : [(5,1)],
    'queen' : [(4,1)],
    'rook'  : [(1,1),(8,1)], #车
    'bishop': [(3,1),(6,1)], #象
    'knight': [(2,1),(7,1)], #马
    'pawn':   [(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2)] #兵
}

class BoardView(EventBasedView):
    import piece
    """Nothing"""
    def __init__(self,evManager,screen):
        super(BoardView, self).__init__(evManager)
        self.screen = screen
        self.piece_list = pygame.sprite.RenderPlain()

    def Notify(self,event):
        if isinstance(event,TickEvent):
            self.piece_list.draw(self.screen)
        elif isinstance(event,GameStartedEvent):
            self._build_board()
            self._put_pieces(default_chess_data)

    def _build_board(self):
        print "Build the board."
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

    def _put_pieces(self,init_data):
        # import game
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
                    self.piece_list.add(block)
        place('black')
        place('white')
        pass


# class GridView(object):
    # def __init__(self):
        # pass



import unittest
class test(unittest.TestCase):
    def setUp(self):
        pass
    def test_run(self):
        pass

if __name__ == '__main__':
    unittest.main()
