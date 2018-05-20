import pygame
import time
from random import randint
pygame.init()
clock = pygame.time.Clock()
fps = 15


white = (255,255,255)
black = (0,0,0,0)
red = (255,0,0)
green = (0,155,0)
display_width = 800
display_height = 600
block_size = 20
apple_size = 30
font = pygame.font.SysFont(None,25)


screen = pygame.display.set_mode((display_width,display_height))
pygame.mixer.init()
pygame.display.set_caption('bullshit')
pygame.mixer.music.load('detto.mp3')
pygame.mixer.music.play()

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
        screen.fill(white)
        message_to_screen("Snake game", green, y_displace = -100)
        message_to_screen("press Space to start", black)
        pygame.display.update()


def snake(block_size, snake_list):
    for XnY in snake_list:
        pygame.draw.rect(screen, green, [XnY[0], XnY[1], block_size, block_size])

def text_oject(text, color):
    text_surf = font.render(text,True, color)
    return text_surf, text_surf.get_rect()

def message_to_screen(msg, color, y_displace = 0):
    screen_text, text_rect = text_oject(msg,color)
    text_rect.center = (display_width/2), (display_height/2) + y_displace
    screen.blit(screen_text, text_rect)

def game_loop():
    direction = "right"
    done = False
    game_over = False
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 20
    lead_y_change = 0
    snake_list = []
    snake_lenght = 1
    ran_apple_x = round(randint(0,display_width - apple_size)) #/ 10.0) * 10.0
    ran_apple_y = round(randint(0,display_height - apple_size)) #/ 10.0) * 10.0
    while not done:
        while game_over:
            screen.fill(white)
            message_to_screen("GAME OVER", red)
            message_to_screen("press C to play again or Q to quit", black, y_displace = 50)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        done = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "right" :
                    lead_x_change = -block_size
                    lead_y_change = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT and direction != "left" :
                    lead_x_change = block_size
                    lead_y_change = 0
                    direction = "right"
                elif event.key == pygame.K_UP and direction != "down" :
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction = "up"
                elif event.key == pygame.K_DOWN and direction != "up" :
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = "down"
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            game_over = True
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         lead_x_change = 0
        lead_x += lead_x_change
        lead_y += lead_y_change
        screen.fill(white)
        pygame.draw.rect(screen, red, [ran_apple_x, ran_apple_y, apple_size, apple_size])
        # screen.fill(red, rect=[200,200,50,50]) #faster way

        snake_head = [lead_x, lead_y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_lenght:
            del snake_list[0]

        for XnY in snake_list[:-1]:
            if XnY == snake_head:
                game_over = True

        snake(block_size, snake_list)

        if lead_x > ran_apple_x and lead_x < ran_apple_x + apple_size \
        or lead_x + block_size > ran_apple_x and lead_x + block_size < ran_apple_x + apple_size:
            if lead_y > ran_apple_y and lead_y < ran_apple_y + apple_size \
            or lead_y + block_size > ran_apple_y and lead_y + block_size < ran_apple_y + apple_size:
                ran_apple_x = round(randint(0,display_width - apple_size))
                ran_apple_y = round(randint(0,display_height - apple_size))
                snake_lenght += 1

        pygame.display.update()
        clock.tick(fps)
game_intro()
game_loop()
