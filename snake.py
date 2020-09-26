import pygame
import math
from random import choice
import random
# Init pygame window
pygame.init()
window_width = 500
window_height = 500
screen = pygame.display.set_mode((window_width, window_height))

# Setting color
purple_color = (86, 50, 168)
green_color  = (87, 168, 50)
red_color    = (168, 50, 68)
yellow_color = (236, 245, 66)
# Init snake
UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4

size_block = 25
snake = [[50, 50, size_block, size_block], [75, 50, size_block, size_block]]
speed = size_block
status = choice([UP, DOWN, LEFT, RIGHT])

# Init snake
fruit = [random.randint(0, int(window_width / size_block) * size_block),
         random.randint(0, int(window_height / size_block) * size_block)]


game_running = True

while game_running:
    screen.fill(purple_color)

    # draw rectangle
    pygame.draw.rect(screen, yellow_color, snake[0])
    for block in snake[1:]:
        pygame.draw.rect(screen, green_color, block)

    # draw fruit
    pygame.draw.circle(screen, red_color, fruit, int(size_block/2))

    # Check key event in game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                status = RIGHT
            elif event.key == pygame.K_LEFT:
                status = LEFT
            elif event.key == pygame.K_UP:
                status = UP
            elif event.key == pygame.K_DOWN:
                status = DOWN

    # snake direction
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i-1].copy()

    if status == UP:
        snake[0][1] -= speed
    elif status == DOWN:
        snake[0][1] += speed
    elif status == LEFT:
        snake[0][0] -= speed
    elif status == RIGHT:
        snake[0][0] += speed

    if snake[0][0] < 0:
        snake[0][0] = window_width - size_block
    if snake[0][0] >= window_width:
        snake[0][0] = 0
    if snake[0][1] < 0:
        snake[0][1] = window_height - size_block
    if snake[0][1] >= window_height:
        snake[0][1] = 0

    # Check snake eat fruit
    xSnake, ySnake = snake[0][0] + \
        int(size_block/2), snake[0][1] + int(size_block / 2)
    distance = math.sqrt((xSnake - fruit[0])**2 + (ySnake - fruit[1])**2)
    if distance <= size_block:
        fruit[0], fruit[1] = random.randint(
            0, window_width), random.randint(0, window_height)
        snake.append(snake[-1].copy())
    # Game over
    for block in snake[1:]:
        if block[0] == snake[0][0] and block[1] == snake[0][1]:
            pygame.font.init()
            myfont = pygame.font.SysFont('Comic Sans MS', 50)
            textsurface = myfont.render('Game over', False, (0, 0, 0))
            screen.blit(textsurface, (window_width / 3,
                                      window_height / 2, 100, 100))
            game_running = False

    pygame.display.flip()
    if game_running == False:
        pygame.time.wait(1000)
    pygame.time.wait(50)

pygame.quit()
