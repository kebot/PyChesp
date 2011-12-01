#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Grid(object):
    pos = [0,0]
    piece = {}
    def __init__(self,pos):
        for l in pos:
            if l<1 or l>8:
                print 'error'
        self.pos = pos
    def getX(self):
        return chr(self.pos[0]+96)

    def getY(self):
        return self.pos[1]

    def put(self,p):
        self.piece = p

# unit test code
if __name__ == '__main__':
    pass
