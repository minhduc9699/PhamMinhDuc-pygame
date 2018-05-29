import pygame
from bullet.bullet import Bullet
from game_objects.game_objects import add_object_to_game_objects

class Player:
    # 1. Describe properties (Properies: image, x, y)
    def __init__(self, x, y, input_manager):
        self.image = pygame.image.load('images/player/player1.png')
        self.x = x
        self.y = y
        self.input_manager = input_manager

    def update(self):
        if self.input_manager.right_pressed:
            self.x += 10
        if self.input_manager.left_pressed:
            self.x -= 10
        if self.input_manager.up_pressed:
            self.y -= 10
        if self.input_manager.down_pressed:
            self.y += 10

        if self.input_manager.x_pressed:
            new_bullet = Bullet(self.x, self.y)
            add_object_to_game_objects(new_bullet)



    def render(self, canvas):
        canvas.blit(self.image, (self.x, self.y))
