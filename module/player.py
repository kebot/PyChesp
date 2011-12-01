#!/usr/bin/env python
# -*- coding: utf-8 -*-
WHITE_CHESS = 0
BLACK_CHESS = 1

class Player(object):
    def __init__(self,chess_color=WHITE_CHESS):
        self.color = chess_color
        pass
