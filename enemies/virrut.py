import pygame

from game_objects.game_objects import GameObjects

class Virrut(GameObjects):
    def __init__(self, x, y):
        GameObjects.__init__(self, x, y)
        self.image = pygame.image.load("images/enemy/virrut.png")

    def update(self):
        self.x += 3

