#start code from rfk  this one has to change because the  x and y for the screen
#need to change. 
import os

MAX_X = 60
MAX_Y = 20
FRAME_LENGTH = 0.1
PATH = os.path.dirname(os.path.abspath(__file__))
MESSAGES = open(PATH + "/messages.txt").read().splitlines()

