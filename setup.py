from distutils.core import setup # Need this to handle modules
import py2exe
import math
import pyxel
import pygame
from time import time
from Lemming import Lemming
from Board_Game import Gameboard
from Draw import Draw
from Tools import Tools
from Scoreboard import Scoreboard

# We have to import all modules used in our program

setup(windows=['main.py']) # Calls setup function to indicate that we're dealing with a single console application
