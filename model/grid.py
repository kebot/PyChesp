#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chess import *
from player import *

class Grid(object):
    def __init__(self,pos,grid=None):
        self.pos = pos
        self.chess = None
        pass

    def __str__(self):
        return "%s" % self.pos 
        return 

    def setPiece(self,c):
        if not self.getPiece():
            self.chess=c
            # c.setGrid(self)
            return c
        else:
            return None

    def getPiece(self):
        return self.chess
    
    # @return Chess Actions
    def pickPiece(self):
        chess = self.chess
        chess.clearGrid()
        self.chess = None
        return chess

import unittest
class test(unittest.TestCase):
    def setUp(self):
        g =  Grid([1,1])
        kebot = Player(WHITE_CHESS)
        chess = Chess(kebot)
        pass

    def test_ccc(self):
        pass

if __name__ == '__main__':
    unittest.main()
