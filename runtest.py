#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from model import *
from model.piece import *
from model.player import *

# DEFAULT_DATA = {
    # King  : [(5,1)],
    # Queen : [(4,1)],
    # Rook  : [(1,1),(8,1)], #车
    # Bishop: [(3,1),(6,1)], #象
    # Knight: [(2,1),(7,1)], #马
    # Pawn  : [(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2)] #兵
# }
TEST_LOCATIONS = {
    Queen : [(1,0)], 
    Pawn  : [(2,0)]
}

class TestGrid(unittest.TestCase):
    #
    #
    #
    #
    def setUp(self):
        print "Create a board."
        self.board = Board()
        p1 = Player('white')
        p2 = Player('black')
        DEFAULT_DATA = TEST_LOCATIONS
        # Put chess on the board with given position
        for name in DEFAULT_DATA:
            pos_arr = DEFAULT_DATA[name]
            for pos in pos_arr:
                piece = name(p1)
                piece.setPos(pos)
                self.board.getGrid(pos).setPiece(piece)
        # set an enermy
        enermy = King(p2)
        self.board.getGrid((1,1)).setPiece(enermy)

    # Test this:
    # A queen cannot move to a destination when there is a piece between it and
    # the destionation.
    def test_queen(self):
        print "try to move a Queen from (1,0) -> (3,0)"
        can_move = self.board.getGrid( (1,0)
                ).getPiece().canMove(self.board,(3,0))
        self.assertFalse(can_move)
        pass

    # A pawn can move to a square diagonally in front of it when there is an
    # enermy piece there.
    def test_pawn(self):
        print "try to move a Queen from (2,0) -> (1,1)"
        pawn = self.board.getGrid( (2,0) ).getPiece()
        can_move = pawn.getPiece().canMove(self.board,(2,1))
        self.assertTrue(can_move)
        pass


unittest.main()

