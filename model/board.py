#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
# import unittest

from grid import *
from chess import *
from player import *
import config

class Board(object):
    def __init__(self):
        self.grids = []
        # [config.GRID_WIDTH][config.GRID_HEIGHT]
        for w in xrange(1,config.GRID_WIDTH+1):
            column = []
            for h in xrange(1,config.GRID_HEIGHT+1):
                grid = Grid([w,h],self)
                # print grid
                column.append(grid)
            self.grids.append(column)
    def getGrid(self,pos):
        w,h = pos
        return self.grids[w-1][h-1]

    def getPiece(self,pos):
        return self.getGrid(pos).getPiece()

import unittest
class test(unittest.TestCase):
    def setUp(self):
        self.b = Board()
        self.player1 = Player(WHITE_CHESS)
        self.chess = Chess(self.player1)

    def test_grid_pos(self):
        poses = ( [8,8] , [1,1] , [2,2] , [3,3] )
        for pos in poses:
            self.assertEqual(self.b.getGrid(pos).pos,pos)

    def test_put_chess(self):
        pos = [1,1]
        kebot = Player(WHITE_CHESS)
        chess = Chess(kebot)
        self.b.getGrid(pos).setChess(chess)
        self.assertEqual(chess , self.b.getGrid(pos).getChess()  )

    def test_move_chess(self):
        begin_pos = [1,1]
        end_pos   = [2,1]
        b_grid = self.b.getGrid(begin_pos)
        b_grid.setChess(self.chess)
        t_grid = self.b.getGrid(end_pos)
        self.chess.move(t_grid)
        self.assertEqual( b_grid.getChess() , None )
        self.assertEqual( t_grid.getChess() , self.chess )

if __name__ == '__main__':
    unittest.main()
