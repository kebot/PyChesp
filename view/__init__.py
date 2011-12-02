#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Views Based On Pygame
import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREY     = ( 50 , 50 , 50)
# GREEN    = (   0, 255,   0)
# RED      = ( 255,   0,   0)

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
    from config import *
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
        
        self.board = BoardView(self,evManager,screen)


    def Notify(self,event):
        if isinstance(event,TickEvent):
            pygame.display.flip()

class BoardView(object):
    def __init__(self):
        pass

class BoardView(EventBasedView):
    """Nothing"""
    def __init__(self, evManager,screen):
        super(BoardView, self).__init__(evManager)
        self.screen = screen

    def Nothing(self,event):
        if isinstance(event,BoardBuildEvent):
            self._build_board()

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
                pygame.draw.rect(self,screen,color,rect)
                print "Width %d , Height %d" % ( w , h)
                print rect
            color = change_color(color)
        pass

class GridView(object):
    def __init__(self):
        pass



import unittest
class test(unittest.TestCase):
    def setUp(self):
        pass
    def test_run(self):
        pass

if __name__ == '__main__':
    unittest.main()
