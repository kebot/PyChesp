#!/usr/bin/env python
#! -*- coding: utf-8 -*-
import pygame
import config
import os

def make(player,kind):
    path = os.path.join(config.DOCROOT,'images',player+ '_' + kind +'.png')
    return piece(path)

class piece(pygame.sprite.Sprite):
    def __init__(self,path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
    def move(self,x,y=None):
        if not y:
            x , y = x
        # Set the location to the current Grid
        self.rect.left = (x-1) * config.SQUARE_WIDTH + config.MARGIN
        self.rect.top  = (config.GRID_HEIGHT - y) * config.SQUARE_HEIGHT + config.MARGIN

# class moveable(piece):
    # def __init__(self, arg):
        # path = os.path.join(config.DOCROOT,'images','movemark.png')
        # super(moveable, self).__init__()
        # self.arg = arg
