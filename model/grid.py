#!/usr/bin/env python
# -*- coding: utf-8 -*-

from piece import *
from player import *

class Grid(object):
    def __init__(self,pos,grid=None):
        self.pos = pos
        self.piece = None
        pass

    def __str__(self):
        return "%s" % self.pos 
        return 

    def setPiece(self,c):
        if not self.getPiece():
            self.piece=c
            # c.setGrid(self)
            return c
        else:
            return None

    def getPiece(self):
        return self.piece
    
    # @return piece Actions
    def pickPiece(self):
        piece = self.piece
        # piece.clearGrid()
        self.piece = None
        return piece

import unittest
class test(unittest.TestCase):
    def setUp(self):
        g =  Grid([1,1])
        kebot = Player(WHITE_CHESS)
        piece = piece(kebot)
        pass

    def test_ccc(self):
        pass

if __name__ == '__main__':
    unittest.main()
