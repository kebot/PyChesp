#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
# Config.py
GRID_WIDTH = 8 
GRID_HEIGHT= 8

SQUARE_WIDTH = 50
SQUARE_HEIGHT = 50

MARGIN = 20

CONSOLE_WIDTH = 400

TITLE = "PyChesp"

DEBUG = True

# left , top ,  width , height
START_BTN_LOC = (SQUARE_WIDTH * GRID_WIDTH + MARGIN*2,
        15 * MARGIN + 100,
        160,20)

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREY     = ( 50 , 50 , 50)
# GREEN    = (   0, 255,   0)
# RED      = ( 255,   0,   0)

# Env veriables
DOCROOT = sys.path[0]

def debug(var):
    if DEBUG:
        print var
