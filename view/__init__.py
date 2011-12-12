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
    WINDOW_WIDTH = SQUARE_WIDTH * GRID_WIDTH + MARGIN*2 + CONSOLE_WIDTH
    WINDOW_SIZE = [WINDOW_WIDTH,WINDOW_HEIGHT]

    def __init__(self,evManager):
        super(PygameView,self).__init__(evManager)
        pygame.init()
        screen = pygame.display.set_mode(self.WINDOW_SIZE)
        screen.fill(self.GREY)
        self.board = BoardView(evManager,screen)
        self.text_view = ConsoleView(evManager,screen)
        self.start_button = StartButton(evManager,screen)

    def Notify(self,event):
        if isinstance(event,TickEvent):
            # pygame.display.update()
            pygame.display.flip()
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
            self._build_board()
            self.piece_list.draw(self.screen)
            pygame.display.flip()
        elif isinstance(event,PlacePieceEvent):
            self.placeChess(event.piece)
        elif isinstance(event,GameRestartedEvent):
            # print "Game Restarted"
            self.piece_list.empty()
            # self._build_board()

    def placeChess(self,p):
        block = piece.make(p.player.color,p.name,self.piece_list)
        block.move(p.pos)
        p.bind(block)
        self.piece_list.add(block)

    def _build_board(self):
        # print "Build the board."
        color_a = (150,100,0)
        color_b = (250, 200, 100)
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

class ConsoleView(EventBasedView):
    MAX_LINE = 15
    messages = []
    def __init__(self, evManager , screen):
        super(ConsoleView, self).__init__(evManager)
        self.screen = screen
        self.font = pygame.font.SysFont('arial',16)

    def Notify(self,event):
        if isinstance(event,TickEvent):
            left= SQUARE_WIDTH * GRID_WIDTH + MARGIN*2
            top = MARGIN
            for msg in self.messages:
                self.text_surface = self.font.render(msg, True , (0,0,0) , (
                    255,255,255) )
                self.screen.blit(self.text_surface,(left,top))
                top = top + MARGIN
        elif isinstance(event,LogEvent):
            self.log(event.msg)

    def log(self,string):
        if len(self.messages) == self.MAX_LINE:
            self.messages.pop(0)
        self.messages.append(string)
        pass

class StartButton(EventBasedView):
    """StartButton"""
    def __init__(self, evManager , screen):
        super(StartButton, self).__init__(evManager)
        self.screen = screen
        self.font = pygame.font.SysFont('arial',16)
        self.button_surface = self.font.render( "Start", True , (0,0,0) , (
                    255,255,255) )
        left,top,w,h = START_BTN_LOC
        # left= SQUARE_WIDTH * GRID_WIDTH + MARGIN*2
        # top = 15 * MARGIN
        # self.rect = (left,top)
        self.rect = (left,top)
        # print self.rect

    def Notify(self,event):
        if isinstance(event,TickEvent):
            self.screen.blit(self.button_surface,self.rect)

import unittest
class test(unittest.TestCase):
    def setUp(self):
        pass
    def test_run(self):
        pass

if __name__ == '__main__':
    unittest.main()
