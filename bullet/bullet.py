import pygame

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/player-bullet.png")

    def update(self):
        self.y -= 10

    def render(self, canvas):
        canvas.blit(self.image, (self.x, self.y))
