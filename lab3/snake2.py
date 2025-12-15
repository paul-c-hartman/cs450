import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game with Obstacles and Power-ups')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Snake settings
snake_block_size = 10
snake_speed = 15

# Obstacle and power-up settings
obstacle_size = 20
powerup_size = 20

# Font styles
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    obstacle_x = round(random.randrange(0, width - obstacle_size) / 10.0) * 10.0
    obstacle_y = round(random.randrange(0, height - obstacle_size) / 10.0) * 10.0

    powerup_x = round(random.randrange(0, width - powerup_size) / 10.0) * 10.0
    powerup_y = round(random.randrange(0, height - powerup_size) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not game_over:

        while game_close == True:
            screen.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, green, [obstacle_x, obstacle_y, obstacle_size, obstacle_size])
        pygame.draw.rect(screen, red, [powerup_x, powerup_y, powerup_size, powerup_size])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for segment in snake_List:
            pygame.draw.rect(screen, white, [segment[0], segment[1], snake_block_size, snake_block_size])

        pygame.display.update()

        # Check for collisions
        if x1 < obstacle_x + obstacle_size and x1 + snake_block_size > obstacle_x:
            if y1 < obstacle_y + obstacle_size and y1 + snake_block_size > obstacle_y:
                game_close = True

        if x1 < powerup_x + powerup_size and x1 + snake_block_size > powerup_x:
            if y1 < powerup_y + powerup_size and y1 + snake_block_size > powerup_y:
                Length_of_snake += 1
                obstacle_x = round(random.randrange(0, width - obstacle_size) / 10.0) * 10.0
                obstacle_y = round(random.randrange(0, height - obstacle_size) / 10.0) * 10.0

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()