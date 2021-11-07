"""Module constants containing all the main parameters for the game.
    Stereotype:
        Information holder
"""
import os

MAX_X = 80
MAX_Y = 20
FRAME_LENGTH = 0.1
PADDLE_LENGTH = 10
PADDLE_SPEED_FACTOR = 5  # it needs to be an integer
BRICKS_LEFT_MARGIN = 5
NUMBER_OF_LIVES = 2
FINAL_MESSAGES_LAPSE_TIME = 3
PATH = os.path.dirname(os.path.abspath(__file__))