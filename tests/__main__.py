#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from testchess import *


from module import *

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.a = Grid()

    def test_kiss(self):
        self.assertFalse(self.a.is_empty())
        
        king = Chess.King()
        
        self.a.put()

        # self.assert


unittest.main()

