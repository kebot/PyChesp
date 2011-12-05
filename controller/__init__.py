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
#----------------------------------------------------------------------------------------------------
# EventHandler
# Short for EventBased Controller
class _E(object):
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

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
                    self.evManager.Post(ev)
                    # print ev.location

    def _getBoardPosition(self,pos):
        # print pos
        x, y = pos
        pos_x =  (x - config.MARGIN) / config.SQUARE_WIDTH + 1
        pos_y = 8 - (y - config.MARGIN) / config.SQUARE_HEIGHT
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
        self.board_controller = BoardController(evManager)

    def Start(self):
        self.p1 = Player('white')
        self.p2 = Player('black')
        ev = GameStartedEvent(self)
        self.evManager.Post(ev)
        pass

#----------------------------------------------------------------------------------------------------
# Models
import model
from model.piece import *

DEFAULT_DATA = {
    King  : [(5,1)],
    Queen : [(4,1)],
    Rook  : [(1,1),(8,1)], #车
    Bishop: [(3,1),(6,1)], #象
    Knight: [(2,1),(7,1)], #马
    Pawn  : [(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2)] #兵
}

class BoardController(_E):
    def __init__(self,arg):
        super(BoardController, self).__init__(arg)
        self.model = None
        self.current_piece = None

    def _build_board(self):
        def place(player):
            for name in DEFAULT_DATA:
                pos_arr = DEFAULT_DATA[name]
                for pos in pos_arr:
                    if player.color == 'black':
                        x,y = pos
                        y = 9-y
                        pos = (x,y)
                    piece = name(player)
                    piece.setPos(pos)
                    self.model.getGrid(pos).setPiece(piece)
                    ev = PlacePieceEvent(piece)
                    self.evManager.Post(ev)
        place(self.game.p1)
        place(self.game.p2)
        pass

    def Notify(self,event):
        if isinstance(event,TickEvent):
            if self.current_piece:
                self.current_piece.view.follow_mouse()
        elif isinstance(event,ClickOnBoardEvent):
            # Send it to Board Model
            if self.current_piece:
                self.current_piece = None
            else:
                print "try to get piece"
                self.current_piece = self.model.getGrid(event.location).getPiece()
                print self.current_piece

        elif isinstance(event,GameStartedEvent):
            self.game = event.game
            self.model = model.board.Board()
            self._build_board()

# Views
#----------------------------------------------------------------------------------------------------
from view import *

#----------------------------------------------------------------------------------------------------

import unittest
class test(unittest.TestCase):
    def setUp(self):
        pass

    def test_run(self):
        def place(color):
            for name in DEFAULT_DATA:
                pos_arr = DEFAULT_DATA[name]
                for pos in pos_arr:
                    if color == 'black':
                        x,y = pos
                        y = 9-y
                        pos = (x,y)
                    print pos
        place('black')
        place('white')
        pass
if __name__ == '__main__':
    unittest.main()
