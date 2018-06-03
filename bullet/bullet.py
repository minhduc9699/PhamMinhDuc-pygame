import pygame
from game_objects.game_objects import  GameObjects

class Bullet(GameObjects):
    def __init__(self, x, y):
        GameObjects.__init__(self, x, y)
        self.image = pygame.image.load("images/player-bullet.png")

    def update(self):
        self.y -= 10
        if self.y < 0:
            self.is_active = False

