#!/usr/bin/env python
#! -*- coding: utf-8 -*-
import pygame
import config
import os

class piece(pygame.sprite.Sprite):
    def __init__(self,path):
        pygame.sprite.Sprite.__init__(self)
        # height = config.SQUARE_HEIGHT
        # width  = config.SQUARE_WIDTH
        # self.image = pygame.Surface(path)
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()

    def update(self,x,y):
        # Set the location to the current Grid
        self.rect.left = x * config.SQUARE_WIDTH + config.MARGIN
        self.rect.top  = (config.GRID_HEIGHT - y) * config.SQUARE_HEIGHT + config.MARGIN
        pass

class Knight(piece):
    """docstring for Knight"""
    def __init__(self, player="black"):
        path = os.path.join(config.DOCROOT ,'images' ,  player + '_knight' + '.png')
        super(Knight, self).__init__(path)
