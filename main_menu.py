import pygame
import main

def main_menu():

    m = True
    while m: # while loop  says when m.
        for event in pygame.event.get(): #fetching the items from event queue
            if event.type == pygame.QUIT:
                quit.Quit() # quiting the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit.Quit() # clicking KEYDOWN of Escape will trigger the quitting of the game. if you press quit/ escape key it will quit the game
             # mouse position
            mouse = pygame.mouse.get_pos(mouse)
            pygame.display.update()
