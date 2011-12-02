#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------------------------------
class Event(object):
    def __init__(self):
        self.name = "General Event"

class TickEvent(Event):
    def __init__(self):
        self.name = "Tick Event"

class QuitEvent(Event):
    def __init__(self):
        self.name = "Quit Event"
        pass

class GameStartEvent(Event):
    def __init__(self, arg):
        self.name = "Game Start Event"

class ClickOnBoardEvent(Event):
    def __init__(self,loc):
        self.name = "ClickOnBoardEvent"
        self.location = loc
        pass

class BoardBuildEvent(Event):
    def __init__(self,arg):
        self.name = "BoardBuildEvent"
        self.board = arg
        

#----------------------------------------------------------------------------------------------------
def Debug(msg,_type='Message'):
    print '      %s:%s' % (_type , msg)

class EventManager:
    """
    This object is responsible for coordinating most communication between the
    Model, View, and Controller.
    """
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()
        self.eventQueue = []

    #----------------------------------------------------------------------
    def RegisterListener(self, listener):
        self.listeners[listener] = 1

    #----------------------------------------------------------------------
    def UnregisterListener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]
        
    #----------------------------------------------------------------------
    def Post(self, event):
        if not isinstance(event, TickEvent):
            Debug(event.name)
        for listener in self.listeners.keys():
            # NOTE: If the weakref has died, it will be automatically
            #       removed, so we do not need to worry about it.
            listener.Notify(event)

