"""
    A Snake Game written in Python by le Remlon & me ☺
    Creation Date: 03.11.2022
"""

# region Imports
import pygame
import Variables
import Snake
import Food
# endregion

# region Game class


class Game():
    def __init__(self,):
        self.game_over = False
        self.snake = Snake.Snake()
        self.display = pygame.display.set_mode(Variables.Sizes["WindowSize"])
        self.food = Food.Food(self.snake)

        # region Initialise PyGame
        pygame.init()
        pygame.display.set_caption("SnakeGame")
        # endregion

        self.clock = pygame.time.Clock()
        self.game_loop()

    @staticmethod
    def addDirection(curPos, num):
        if num == 99:
            return
        if num == 0:
            newPos = {
                'x': (curPos['x'] + Variables.Sizes['TileLength']),
                'y': (curPos['y'])}
        elif num == 1:
            newPos = {
                'x': (curPos['x'] - Variables.Sizes['TileLength']),
                'y': (curPos['y'])}
        elif num == 2:
            newPos = {
                'x': (curPos['x']),
                'y': (curPos['y'] + Variables.Sizes['TileLength'])}
        elif num == 3:
            newPos = {
                'x': (curPos['x']),
                'y': (curPos['y'] - Variables.Sizes['TileLength'])}
        return newPos

    def collisionDetect(self):
        shp = self.snake.body[0].pos  # Snake Head Position
        if (shp['x'] + Variables.Sizes['TileLength'] > Variables.Sizes['WindowWidth'] or
                shp['x'] < 0 or
            shp['y'] + Variables.Sizes['TileLength'] > Variables.Sizes['WindowWidth'] or
                shp['y'] < 0):
            self.game_over = True
        if shp['x'] == self.food.pos['x'] and shp['y'] == self.food.pos['y']:
            self.snake.addBodyPart()
            self.food = Food.Food(self.snake)
        for bp in self.snake.body[1::]:
            if (shp['x'] == bp.pos['x'] and shp['y'] == bp.pos['y']):
                self.game_over = True

    def draw(self):
        self.display.fill(Variables.Colors['White'])
        for bp in self.snake.body:
            pygame.draw.rect(self.display, Variables.Colors['Black'], [
                (bp.pos['x']-1),
                (bp.pos['y']-1),
                (Variables.Sizes['TileLength']-2),
                (Variables.Sizes['TileLength']-2)])

        pygame.draw.rect(self.display, self.food.color, [
            (self.food.pos['x']-1),
            (self.food.pos['y']-1),
            (Variables.Sizes['TileLength']-2),
            (Variables.Sizes['TileLength']-2)])

        pygame.display.update()

    def tick(self):
        self.clock.tick(Variables.SNAKE_SPEED)

    def game_loop(self):
        snakehead = self.snake.body[0]
        direction = 99
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if direction == 1:
                            continue
                        direction = 0
                    if event.key == pygame.K_LEFT:
                        if direction == 0:
                            continue
                        direction = 1
                    if event.key == pygame.K_DOWN:
                        if direction == 3:
                            continue
                        direction = 2
                    if event.key == pygame.K_UP:
                        if direction == 2:
                            continue
                        direction = 3

            snakehead.nextPos = Game.addDirection(snakehead.pos, direction)
            self.collisionDetect()
            self.draw()
            self.tick()
            if direction != 99:
                for bp in self.snake.body:
                    bp.updateBodyPart()
                self.snake.handDown()

# endregion


game = Game()
pygame.quit()
quit()
