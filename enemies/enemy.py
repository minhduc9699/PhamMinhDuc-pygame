import pygame
from game_objects.game_objects import  GameObjects

class Enemy(GameObjects):
    def __init__(self, x, y):
        GameObjects.__init__(self,x, y)
        self.image = pygame.image.load('images/enemy/bacteria1.png')

    def update(self):
        self.y += 3

