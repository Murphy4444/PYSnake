# region Imports
import random
import Variables
# endregion


class Food():
    def __init__(self, snake):

        validPlacement = False
        while not validPlacement:
            randx = random.randint(1, (Variables.Sizes['WindowWidth']/25)) * 25
            randy = random.randint(1, (Variables.Sizes['WindowWidth']/25)) * 25

            for bp in snake.body:
                if randx == bp.pos['x'] or randy == bp.pos['y']:
                    break
                validPlacement = True

        self.pos = {'x': randx, 'y': randy}

        self.color = (random.randint(50, 255), random.randint(
            50, 255), random.randint(50, 255))
