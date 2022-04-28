import main
import pygame
import random
pygame.init()
background = (250, 250, 250)#at the moment I am setting this to 250,250,250 untill I can get the window to open
width = (500) # width may change to fill the whole of the screen
height = (400) # height may change to fill the whole of the screen
screen = pygame. display. set_mode((width, height))

dice_import = False
clock = pygame.time.Clock()
xx = 30
yy = 30

button = pygame.Rect(150, 150, 80, 80)


def dice_is_rolling():
    dice_is_rolling = random.randint(1, 6)
    if dice_is_rolling == 1:
        dices = pygame.image.load("di1.png")
    elif dice_is_rolling == 2:
        dices = pygame.image.load("di2.jpg")
    elif dice_is_rolling == 3:
        dices = pygame.image.load("di3.jpg")
    elif dice_is_rolling == 4:
        dices = pygame.image.load("di4.png")
    elif dice_is_rolling == 5:
        dices = pygame.image.load("di6.jpg")
    elif dice_is_rolling == 6:
        dices = pygame.image.load("di5.jpg")

    return (dice_is_rolling)

while dice_import == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dice_import = True

pygame.quit()