#!/usr/bin/env python
# -*- coding: utf-8 -*-
from player import *

class Chess(object):
    def __init__(self,player):
        self.player = player
        self.grid = None
        pass

    def setGrid(self,g):
        self.grid = g
        pass
    def clearGrid(self):
        self.grid = None
        pass
    # Grid
    def move(self,target_grid):
        if( self.grid ):
            self.grid.pickChess()
        target_grid.setChess(self)

class Knight(Chess):
    def __init__(self,player):
        super(Knight, self).__init__(player)

class Queen(Chess):
    def __init__(self,player):
        super(Knight, self).__init__(player)

class Bishop(Chess):
    def __init__(self,player):
        super(Knight, self).__init__(player)

class King(Chess):
    def __init__(self,player):
        super(Knight, self).__init__(player)

class Rook(Chess):
    def __init__(self,player):
        super(Knight, self).__init__(player)

class Pawn(Chess):
    def __init__(self,player):
        super(Knight, self).__init__(player)
