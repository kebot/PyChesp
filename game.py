#!/usr/bin/env python
# -*- coding: utf-8 -*-
from event import *
from controller import *
from view import *
from model import *

def main():
    em = EventManager()
    mouse_controller = MouseController(em)
    pygame_view = PygameView(em)
    game_controller = GameController(em)
    game_controller.Start()
    clock_controller = ClockController(em)
    clock_controller.Run()
    pass

if __name__ == '__main__':
    main()
