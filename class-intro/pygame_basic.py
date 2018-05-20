import pygame

pygame.init()

#1.setup game window
size = (800, 600)
canvas = pygame.display.set_mode(size)

#3. Clock
clock = pygame.time.Clock()
loop = True

#creat player
class Player:
    def __init__(self, x, y, player_image):
        self.x = x
        self.y = y
        self.player_image = player_image

player_image = pygame.image.load("./player1.png")

player_one = Player(800/2, 600/2, player_image )
player_two = Player(800/2, 600/2, player_image )




while loop:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
    key_pressed = pygame.key.get_pressed()
    print(key_pressed)
    #player 1 move
    if key_pressed[pygame.K_UP]:
        player_one.y -= 3
    if key_pressed[pygame.K_DOWN]:
        player_one.y += 3
    if key_pressed[pygame.K_LEFT]:
        player_one.x -= 3
    if key_pressed[pygame.K_RIGHT]:
        player_one.x += 3
    #player 2 move
    # if key_pressed[pygame.K_w]:
    #     player_two.y -= 3
    # if key_pressed[pygame.K_s]:
    #     player_two.y += 3
    # if key_pressed[pygame.K_a]:
    #     player_two.x -= 3
    # if key_pressed[pygame.K_d]:
    #     player_two.x += 3
    #player 2 move by mouse
    (player_two.x, player_two.y) = pygame.mouse.get_pos()


    canvas.fill((225, 0, 0))
    canvas.blit(player_one.player_image, (player_one.x, player_one.y))
    canvas.blit(player_one.player_image, (player_two.x, player_two.y))



    clock.tick(60)
    pygame.display.flip()
