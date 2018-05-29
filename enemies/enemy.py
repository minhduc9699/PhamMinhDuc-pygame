import pygame

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('images/enemy/bacteria1.png')

    def update(self):
        self.y += 3

    def render(self, canvas):
        canvas.blit(self.image, (self.x, self.y))