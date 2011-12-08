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

    def log(self,message):
        ev = LogEvent(message)
        self.evManager.Post(ev)

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
                    self._onButtonClickEvent(pos)
                    location = self._getBoardPosition(pos)
                    if location:
                        ev = ClickOnBoardEvent(location)
                if ev:
                    self.evManager.Post(ev)

    def _getBoardPosition(self,pos):
        x, y = pos
        pos_x =  (x - config.MARGIN) / config.SQUARE_WIDTH + 1
        pos_y = 8 - (y - config.MARGIN) / config.SQUARE_HEIGHT
        arr = (pos_x,pos_y)
        # count = 0
        for i in arr:
            # count++
            if i < 0 or i>8:
                return False
        return arr

    def _onButtonClickEvent(self,pos):
        a,b  = pos
        x,y,w,h = START_BTN_LOC
        # print a,b,x,y,w,h
        if x<a<x+w and y<b<y+h:
            print "Start"
            ev = GameRestartedEvent()
            self.evManager.Post(ev)

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

class GameController(_E):
    def __init__(self , evManager):
        super(GameController, self).__init__(evManager)
        self.board_controller = BoardController(evManager)

    def Start(self):
        self.p1 = Player('white')
        self.p2 = Player('black')
        ev = GameStartedEvent(self)
        self.evManager.Post(ev)
        self.log("Game Started,Write Player's True.")
        pass

    def Notify(self,event):
        if isinstance(event,GameRestartedEvent):
            self.Start()
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
        self.current_player = None

    def _build_board(self):
        def place(player):
            for name in DEFAULT_DATA:
                pos_arr = DEFAULT_DATA[name]
                for pos in pos_arr:
                    if player.color == 'black':
                        x,y = pos
                        y = 9-y
                        x = 9-x
                        pos = (x,y)
                    piece = name(player)
                    piece.setPos(pos)
                    self.model.getGrid(pos).setPiece(piece)
                    ev = PlacePieceEvent(piece)
                    self.evManager.Post(ev)
        place(self.game.p1)
        place(self.game.p2)
        pass

    def _changeCurrentPlayer(self):
        if self.current_player is self.game.p1:
            self.current_player = self.game.p2
        else:
            self.current_player = self.game.p1
        self.log( "It's "+self.current_player.color+" Player's turn." )

    # Move the chess from a to b
    def _moveChess(self, piece , end):
        if piece.canMove(self.model,end):
            is_ended = False
            target_grid = self.model.getGrid(end)
            if target_grid:
                target_piece = target_grid.pickPiece()
                if target_piece:
                    is_ended = self._judgeWinner(target_piece)
                    target_piece.remove()
                    msg = "%s player's %s has been eaten." % (
                            target_piece.player.color , target_piece.name )
                    self.log( msg )
            self.model.getGrid(piece.pos).pickPiece()
            target_grid.setPiece(piece)
            piece.view.move(end)
            msg = "%s %s move to (%d,%d)" % (piece.player.color,piece.name,
                    end[0],end[1])
            self.log(msg)
            if is_ended:
                self._sentGameEndEvent()
                return
            self._changeCurrentPlayer()
            pass
        else:
            piece.view.move(piece.pos)

    def _sentGameEndEvent(self):
        ev = GameEndedEvent(self.current_player)
        self.evManager.Post(ev)
        msg = "Game Ended Winner:"+self.current_player.color
        self.log(msg)
        pass

    def _judgeWinner(self,piece):
        if piece.name is 'king':
            return True
            # print self.current_player
            # print 'wins'

    def _delegateMove(self,pos):
        if self.current_piece:
            self._moveChess(self.current_piece,pos)
            self.current_piece = None
        else:
            cp = self.model.getPiece(pos)
            if cp and cp.player is self.current_player:
                self.current_piece = cp

    def Notify(self,event):
        if isinstance(event,TickEvent):
            if self.current_piece:
                self.current_piece.view.follow_mouse()
        elif isinstance(event,ClickOnBoardEvent):
            self._delegateMove(event.location)
        elif isinstance(event,GameStartedEvent):
            self.game = event.game
            self.model = model.board.Board()
            self._build_board()
            self.current_player = self.game.p1

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
