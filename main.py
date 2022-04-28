import pygame #opens the file called pygame
#import dice
import constant


background = (0, 128, 128)#at the moment I am setting this to 250,250,250 untill I can get the window to open
width = (1874) # width may change to fill the whole of the screen
height = (1500) # height may change to fill the whole of the screen
screen = pygame. display. set_mode((width, height))
screen.fill(background)
pygame.display.flip()

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake And Ladders') # title on top of the window

open = True
while open:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      open = False
pygame.quit()
