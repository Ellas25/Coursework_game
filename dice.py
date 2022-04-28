import main
import pygame
import random
pygame.init()


dice_import = False
clock = pygame.time.Clock()
xx = 30
yy = 30

button = pygame.Rect(150, 150, 80, 80)


def dice_is_rolling():
    dice_is_rolling = random.randint(1, 6)
    if dice_is_rolling == 1:
        dices = pygame.image.load("src/di1.png")
    elif dice_is_rolling == 2:
        dices = pygame.image.load("src/di2.jpg")
    elif dice_is_rolling == 3:
        dices = pygame.image.load("src/di3.jpg")
    elif dice_is_rolling == 4:
        dices = pygame.image.load("src/di4.png")
    elif dice_is_rolling == 5:
        dices = pygame.image.load("src/di6.jpg")
    elif dice_is_rolling == 6:
        dices = pygame.image.load("src/di5.jpg")

    return (dice_is_rolling)

while dice_import == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dice_import = True

pygame.quit()