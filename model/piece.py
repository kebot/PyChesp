#!/usr/bin/env python
# -*- coding: utf-8 -*-
from player import *
import pygame

class Piece(object):
    def __init__(self,player,pos=None):
        self.player = player
        # self.grid = None
        self.pos = pos
        pass

    def canMove(self,board,end):
        target_piece = board.getPiece(end)
        if target_piece and target_piece.player == self.player:
            return False
        return self.pieceMove(board,end)

    def pieceMove(self,board,end):
        return True

    def setPos(self,pos):
        self.pos = pos

    # remove the piece from grid
    def remove(self):
        self.pos = None
        self.view.removeFromBoard()

    def bind(self,view):
        self.view = view

    def _range(self,a,b):
        if a < b:
            smaller,bigger = a , b
        else:
            smaller,bigger = b , a
        print "From:" , smaller , " To:" , bigger
        return xrange(smaller+1,bigger)

class Knight(Piece):
    def __init__(self,player):
        super(Knight, self).__init__(player)
        self.name = 'knight'
    #
    def pieceMove(self,board,end):
        end_x,end_y=end
        current_x,current_y = self.pos
        distance_x = abs(current_x-end_x)
        distance_y = abs(current_y-end_y)
        if(distance_x is 2 and distance_y is 1) or (distance_x is 1 and
                distance_y is 2):
            return True
        else:
            return False

class Queen(Piece):
    def __init__(self,player):
        super(Queen, self).__init__(player)
        self.name = 'queen'

    def pieceMove(self,board,end):
        print "Queen move"
        end_x , end_y = end
        current_x , current_y = self.pos
        distance_x = abs(current_x-end_x)
        distance_y = abs(current_y-end_y)
        # Positions
        positions = []
        if distance_x is 0:
            for y in self._range(current_y,end_y):
                positions.append( (current_x,y) )
        elif distance_y is 0:
            for x in self._range(current_x,end_x):
                positions.append( (x,current_y) )
        elif distance_y == distance_x:
            begin_x = min( current_x , end_x )
            begin_y = min( current_y , end_y )
            for dis in range( 1 , distance_x ):
                positions.append( ( begin_x+dis,begin_y+dis ) )
        else:
            return False
        # print "Positions - " , positions
        for pos in positions:
            if board.getPiece(pos):
                return False
        return True

class Bishop(Piece):
    def __init__(self,player):
        super(Bishop, self).__init__(player)
        self.name = 'bishop'

    def pieceMove(self,board,end):
        print "Bisshop move"
        end_x , end_y = end
        current_x , current_y = self.pos
        distance_x = abs(current_x-end_x)
        distance_y = abs(current_y-end_y)
        # Positions
        positions = []
        if distance_y == distance_x:
            begin_x = min( current_x , end_x )
            begin_y = min( current_y , end_y )
            for dis in range( 1 , distance_x ):
                positions.append( ( begin_x+dis,begin_y+dis ) )
        else:
            return False
        # print "Positions - " , positions
        for pos in positions:
            if board.getPiece(pos):
                return False
        return True

class King(Piece):
    def __init__(self,player):
        super(King, self).__init__(player)
        self.name = 'king'

    def pieceMove(self,board,end):
        end_x , end_y = end
        current_x , current_y = self.pos
        if abs(current_x - end_x) < 1 and abs(current_y - end_y) < 1:
            return True
        else:
            return False

class Rook(Piece):
    def __init__(self,player):
        super(Rook, self).__init__(player)
        self.name = 'rook'

    def pieceMove(self,board,end):
        print "Rook move"
        end_x , end_y = end
        current_x , current_y = self.pos
        distance_x = abs(current_x-end_x)
        distance_y = abs(current_y-end_y)
        positions = []
        if distance_x is 0:
            for y in self._range(current_y,end_y):
                positions.append( (current_x,y) )
        elif distance_y is 0:
            for x in self._range(current_x,end_x):
                positions.append( x,current_y )
        else:
            return False
        for pos in positions:
            if board.getPiece(pos):
                return False
        return True

class Pawn(Piece):
    def __init__(self,player):
        super(Pawn, self).__init__(player)
        self.name = 'pawn'
        self.first_step = True

    def pieceMove(self,board,end):
        end_x , end_y = end
        current_x , current_y = self.pos
        distance_y = end_y - current_y
        distance_x = current_x-end_x
        if ( abs(distance_y) > 2 ) or ( abs(distance_x) > 1 ):
            return False
        # Pawn can only move forward
        is_front = distance_y > 0
        if self.player.color=='black':
            is_front = not is_front
        if not is_front:
            return False
        if abs(distance_x) is 1:
            return board.getPiece(end)
        elif abs(distance_x) is 0:
            if abs(distance_y) is 2:
                if not self.first_step:
                    return False
                else:
                    if board.getPiece( (current_x, (current_y+end_y)/2 ) ):
                        return False
                    else:
                        self.first_step = False
            result = not board.getPiece(end)
            if result and self.first_step:
                self.first_step = False
            return result
        else:
            return False
