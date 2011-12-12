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

class GameStartedEvent(Event):
    def __init__(self, game=None):
        self.name = "Game Start Event"
        self.game = game

class GameRestartedEvent(Event):
    def __init__(self):
        self.name = "GameRestartedEvent"
        pass

class GameEndedEvent(Event):
    def __init__(self,player=None):
        self.winner = player
        pass

class ClickOnBoardEvent(Event):
    def __init__(self,loc):
        self.name = "ClickOnBoardEvent"
        self.location = loc
        pass

class BoardBuildEvent(Event):
    def __init__(self,arg):
        self.name = "BoardBuildEvent"
        self.board = arg

class PlacePieceEvent(Event):
    """Place an Piece From a Grid"""
    def __init__(self, p):
        self.name = "PlacePieceEvent"
        self.piece = p

class PieceMoveEvent(Event):
    def __init__(self,source,target):
        # Make a Move
        pass
class LogEvent(Event):
    """Log Message"""
    def __init__(self, msg):
        super(LogEvent, self).__init__()
        self.msg = msg

# ********* ________ **********

# ********* ________ **********
class PieceMoveEvent(Event):
    def __init__(self,source,location):
        self.move =  [source,location]
        pass

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
        if not isinstance(event, TickEvent) and not isinstance(event,LogEvent):
            pass
            # Debug(event.name)
            # ev = LogEvent(event.name)
            # self.Post(ev)

        for listener in self.listeners.keys():
            # NOTE: If the weakref has died, it will be automatically
            #       removed, so we do not need to worry about it.
            listener.Notify(event)

