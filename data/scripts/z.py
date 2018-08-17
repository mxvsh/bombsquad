# -*- coding: utf-8 -*-
import bs
import bsInternal
import bsPowerup
import bsUtils
import random

def list():
    for s in bsInternal._getForegroundHostSession().players:
        print ( s.getName() + "     "+ str(bsInternal._getForegroundHostSession().players.index(s)))
                       
    
    for i in bsInternal._getGameRoster():
            try:
                print(i['players'][0]['nameFull'] + "     (/kick " + str(i['clientID'])+")")
            except:
                pass
def kick(a):
       bsInternal._disconnectClient(int(a))
def freezeall():
    for i in bs.getSession().players:
                                try:
                                    i.actor.node.handleMessage(bs.FreezeMessage())
                                except:
                                    pass
def f(a):
    try:
        bs.getSession().players[int(a)].actor.node.handleMessage(bs.FreezeMessage())
    except:
        pass
def curseall():
    for i in bs.getSession().players:
                                try:
                                    i.actor.curse()
                                except:
                                    pass
def c(a):
    try:
        bs.getSession().players[int(a)].actor.curse()
    except:
        pass
def boxall():
    for i in bs.getSession().players:
                                    try:
                                        i.actor.node.torsoModel = bs.getModel("tnt")
                                    except:
                                        print 'error'
    
def box(a):
        bs.getSession().players[int(a)].actor.node.torsoModel = bs.getModel("tnt")
def texall():
    for i in bs.getSession().players:
                                    try:
                                        i.actor.node.colorTexture= bs.getTexture("egg1")
                                    except:
                                        print 'error'
    
def tex(a):
    try:
        bs.getSession().players[int(a)].actor.node.colorTexture= bs.getTexture("egg1")
    except:
        print 'error'
    
def flyall():
    for i in bsInternal._getForegroundHostActivity().players:
                                i.actor.node.fly = True
    
def fly(a):
    bsInternal._getForegroundHostActivity().players[int(a)].actor.node.fly = bsInternal._getForegroundHostActivity().players[int(a)].actor.node.fly == False
    
def hug(a,b):
    try:
        bsInternal._getForegroundHostActivity().players[int(a)].actor.node.holdNode = bsInternal._getForegroundHostActivity().players[int(b)].actor.node
    except:
        print 'error'
def pow(a,b):
    if b == 'h':
        try:
            bsInternal._getForegroundHostActivity().players[int(a)].actor.node.handleMessage(bs.PowerupMessage(powerupType = 'health'))
        except:
            bs.screenMessage('Error!',color = (1,0,0))
    elif b == 's':
        try:
            bsInternal._getForegroundHostActivity().players[int(a)].actor.node.handleMessage(bs.PowerupMessage(powerupType = 'shield'))
        except:
            bs.screenMessage('Error!',color = (1,0,0))
    elif b == 'p':
        try:
            bsInternal._getForegroundHostActivity().players[int(a)].actor.node.handleMessage(bs.PowerupMessage(powerupType = 'punch'))
        except:
            bs.screenMessage('Error!',color = (1,0,0))
    
