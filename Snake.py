"""
    Implementing the Snake and BodyPart class.
"""

# region Imports
import Variables
import random
import Variables
# endregion

# region SnakeBody class


class BodyPart(object):
    def __init__(self, pos={'x': -50, 'y': -50}, nextPos={'x': 0, 'y': 0}):
        self.x_vel = self.y_vel = 0
        self.pos = pos
        self.nextPos = nextPos

    def updateBodyPart(self):
        self.pos = self.nextPos
# endregion

# region Snake class


class Snake(object):
    def __init__(self, *args):
        self.body = []
        self.body.append(BodyPart(pos=Variables.STARTING_POINT))

    def addBodyPart(self):
        posBodyPartBefore = self.body[-1].pos
        self.body.append(BodyPart(nextPos=posBodyPartBefore))

    def handDown(self):
        for i in range(len(self.body) - 1):
            self.body[(i+1)].nextPos = self.body[(i)].pos

# endregion
