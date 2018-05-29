import pygame

class InputManager:
    def __init__(self):
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.x_pressed = False

    def __str__(self):
        return "[{o}, {1}, {2}, {3}, {4]".format(
            self.up_pressed,
            self.down_pressed,
            self.left_pressed,
            self.right_pressed,
            self.x_pressed
        )


    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.left_pressed = True
            elif event.key == pygame.K_RIGHT:
                self.right_pressed = True
            elif event.key == pygame.K_UP:
                self.up_pressed = True
            elif event.key == pygame.K_DOWN:
                self.down_pressed = True
            elif event.key == pygame.K_x:
                self.x_pressed = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.left_pressed = False
            elif event.key == pygame.K_RIGHT:
                self.right_pressed = False
            elif event.key == pygame.K_UP:
                self.up_pressed = False
            elif event.key == pygame.K_DOWN:
                self.down_pressed = False
            elif event.key == pygame.K_x:
                self.x_pressed = False

