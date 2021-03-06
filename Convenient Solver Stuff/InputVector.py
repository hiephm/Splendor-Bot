# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 15:56:33 2019

@author: huber.288
"""

import sys
sys.path.append('../Game implementation')
sys.path.append('../Convenient Solver Stuff')
import numpy as np
from Splendor import *
from SplendorCard import *
from Player import *

def InputVector_Simple(Game,L):
    IVlist=[]
    IVlist.extend(Game.gems)
    IVlist.extend(Game.player[0].gems)
    IVlist.extend(Game.player[0].bonuses)
    IVlist.append(Game.player[0].VPs)
    for card in Game.cards:
        IVlist.extend(card.cost)
        IVlist.append(card.bonus)
        IVlist.append(card.VPs)
    while len(IVlist)<L:  #Make sure IV is padded with 0s if cards are gone
        IVlist.append(0)   
    IV=np.array(IVlist)
    return IV

def InputVector_Full(Game,L):
    IVlist=[]
    IVlist.extend(Game.gems)
    IVlist.extend(Game.player[0].gems)
    IVlist.extend(Game.player[0].bonuses)
    IVlist.append(Game.player[0].VPs)
    for deck in Game.cards:
        for card in deck:
            IVlist.extend(card.cost)
            IVlist.append(card.bonus)
            IVlist.append(card.VPs)
    while len(IVlist)<L:  #Make sure IV is padded with 0s if cards are gone
        IVlist.append(0)
    IV=np.array(IVlist)
    return IV