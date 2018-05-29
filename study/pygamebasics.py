import pygame

WHITE = (255, 0, 0)

#1. Init pygame
pygame.init()

#2. Setup screen
size = (600, 800)
canvas = pygame.display.set_mode(size)

#3. Clock
clock = pygame.time.Clock()

# 4 Load image
player_image = pygame.image.load("player1.png")
player_x = 100
player_y = 100

loop = True
while loop:
    # Game loop 1: Event processing
    events = pygame.event.get() # Mouse & Keyboards
    for event in events:
        if event.type == pygame.QUIT:
           loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x += 10
                # BT 1: Code 4 huong di chuyen
                # BT 2: Gioi han di chuyen, khong cho phi ra ngoai man hinh

    # Game loop 2: Draw
    pygame.display.set_caption("Micro-war")
    canvas.fill(WHITE)

    canvas.blit(player_image, (player_x, player_y))

    # Game loop 3: Flip
    clock.tick(60)
    pygame.display.flip() # second buffer