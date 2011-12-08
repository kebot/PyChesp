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
