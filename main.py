import pygame #opens the file called pygame
background = (250, 250, 250)#at the moment I am setting this to 250,250,250 untill I can get the window to open
width = (500) # width may change to fill the whole of the screen
height = (400) # height may change to fill the whole of the screen
screen = pygame. display. set_mode((width, height))
screen.fill(background)
pygame.display.flip()

open = True
while open:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      open = False
pygame.quit()

