#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")

########################
from view import piece
import config

import pygame

## import all events
from event import *

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
# class GameController(object):


#----------------------------------------------------------------------------------------------------
import config
class MouseController(object):
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

    def Notify(self,event):
        if isinstance(event,TickEvent):
            # print "event received"
            for event in pygame.event.get():
                ev = None
                if event.type == pygame.QUIT:
                    ev = QuitEvent()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    location = self._getBoardPosition(pos)
                    if location:
                        ev = ClickOnBoardEvent(location)
                if ev:
                    # print ev.location
                    self.evManager.Post(ev)

    def _getBoardPosition(self,pos):
        y , x = pos
        pos_x = 8 - (x - config.MARGIN) / config.SQUARE_WIDTH
        pos_y = (y - config.MARGIN) / config.SQUARE_HEIGHT + 1
        return (pos_x , pos_y)

#----------------------------------------------------------------------------------------------------

class ClockController:
    WAIT_TIME = 20
    def __init__(self,evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)
        self.clock = pygame.time.Clock()
        self.keepGoing = True
        pass

    def Run(self):
        while self.keepGoing:
            event = TickEvent()
            self.evManager.Post(event)
            self.clock.tick(self.WAIT_TIME)
    
    def Notify(self,event):
        if isinstance(event,QuitEvent):
            self.keepGoing = False

class GameController:
    def __init__(self , evManager):
        self.evManager = evManager
        # self.RegisterListener(self)

    def Start(self):
        ev = GameStartedEvent(self)
        self.evManager.Post(ev)
        pass

#----------------------------------------------------------------------------------------------------
# Models

# Views
#----------------------------------------------------------------------------------------------------
from view import *

#----------------------------------------------------------------------------------------------------

import unittest
class test(unittest.TestCase):
    def setUp(self):
        em = EventManager()
        mouse_controller = MouseController(em)
        pygame_view = PygameView(em)
        game_controller = GameController(em)
        game_controller.Start()
        clock_controller = ClockController(em)
        clock_controller.Run()

    def test_run(self):
        pass
if __name__ == '__main__':
    unittest.main()
