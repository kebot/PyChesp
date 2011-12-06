#!/usr/bin/env python
#! -*- coding: utf-8 -*-
import pygame
import config
import os

def make(player,kind,li=None):
    path = os.path.join(config.DOCROOT,'images',player+ '_' + kind +'.png')
    p = piece(path)
    if li:
        p.group = li
    return p

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

    def follow_mouse(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0] - config.SQUARE_WIDTH/2
        self.rect.y  = pos[1] - config.SQUARE_HEIGHT/2
        pass

    #remove the current piece from board
    def removeFromBoard(self):
        self.remove(self.group)
        pass
