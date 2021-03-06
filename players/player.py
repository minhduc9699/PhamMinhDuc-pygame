import pygame
from bullet.bullet import Bullet
from game_objects.game_objects import add_object_to_game_objects, GameObjects, recycle

class Player(GameObjects):

    # 1. Describe properties (Properies: image, x, y)
    def __init__(self, x, y, input_manager):
        GameObjects.__init__(self, x, y)
        self.image = pygame.image.load('images/player/player1.png')
        self.input_manager = input_manager
        self.last_shot = pygame.time.get_ticks()
        self.cooldown = 200

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
            now = pygame.time.get_ticks()
            if now - self.last_shot >= self.cooldown:
                self.last_shot = now
                recycle(Bullet, self.x, self.y - 25)





