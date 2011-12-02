#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREY     = ( 50 , 50 , 50)
RED      = ( 255 , 0 , 0)
class Grid(object):
    def __init__(self,rect,screen):
        self.rect = rect
        pass

    def draw(self,color):
        pygame.draw.rect(screen,color,rect)

    def black(self):
        self.draw(BLACK)

    def white(self):
        self.draw(WHITE)
