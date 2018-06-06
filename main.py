import pygame
from players.player import Player
from enemies.enemy_spawner import EnemySpawner
from inputs.input_manger import InputManager
from game_objects.game_objects import *
from random import randint

BG_COLOR = (255, 255, 0)

# 1. Init pygame
pygame.init()

# 2. Game window & canvas
SIZE = (1024, 600)
canvas = pygame.display.set_mode(SIZE)

# 3. Clock
clock = pygame.time.Clock()

input_manager = InputManager()

player = Player(10, 300, input_manager)
add_object_to_game_objects(player)


# 3. Game loop
loop = True
right_pressed = False
left_pressed = False
count = 0

while loop:
    # Game Loop 1: Events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            input_manager.update(event)
    spawner = EnemySpawner(randint(0, 1024), randint(0, 600))

    if 20< count < 25:
        spawner.spawn_enemy1()
        count += 1
    elif count == 25:
        spawner.spawn_enemy2()
        count = 0
    else:
        count += 1

    game_object_update()

    # Game Loop 2: Draw
    canvas.fill(BG_COLOR)
    pygame.display.set_caption("Micro war")

    game_object_render(canvas)

    # Game Loop 3: Delay and flip
    pygame.display.flip()
    clock.tick(60)
