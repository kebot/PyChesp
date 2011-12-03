#!/usr/bin/env python
# -*- coding: utf-8 -*-
from player import *

class Piece(object):
    def __init__(self,player,pos=None):
        self.player = player
        # self.grid = None
        self.pos = pos
        pass

    def setPos(self,pos):
        self.pos = pos

    def bind(self,view):
        self.view = view

class Knight(Piece):
    def __init__(self,player):
        super(Knight, self).__init__(player)
        self.name = 'knight'

class Queen(Piece):
    def __init__(self,player):
        super(Queen, self).__init__(player)
        self.name = 'queen'

class Bishop(Piece):
    def __init__(self,player):
        super(Bishop, self).__init__(player)
        self.name = 'bishop'

class King(Piece):
    def __init__(self,player):
        super(King, self).__init__(player)
        self.name = 'king'

class Rook(Piece):
    def __init__(self,player):
        super(Rook, self).__init__(player)
        self.name = 'rook'

class Pawn(Piece):
    def __init__(self,player):
        super(Pawn, self).__init__(player)
        self.name = 'pawn'
