import pygame
import main
import buttons

def main_menu():

    F = True
    while F: # while loop  says when m.
        for event in pygame.event.get(): #fetching the items from event queue
            if event.type == pygame.QUIT:
                quit.Quit() # quiting the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit.Quit() # clicking KEYDOWN of Escape will trigger the quitting of the game. if you press quit/ escape key it will quit the game
             # mouse position
            mouse = pygame.mouse.get_pos(mouse)
            pygame.display.update()
            
            
def mouse():
    # this where the positions of mouse will be stored
      if buttons.button3("STOP Music", mouse[0], mouse[1], 900, 0, 200, 50, constant.red_color, constant.purple_color, 25):
                pygame.mixer.music.pause()
      if buttons.button3("PLAY Music", mouse[0], mouse[1], 900, 85, 200, 50, constant.purple_color, constant.grey, 25):
                pygame.mixer.music.unpause()
      if buttons.button3("CREDITS AND COPYWRIGHT", mouse[0], mouse[1], 900, 160, 200, 50, constant.grey_color, constant.red_color, 25):
                credits_page()
            pygame.display.update()
            
def credits_page():
    while True:
        set_up.game_layout_display.blit(copyrights, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
       mouse()
        if buttons.centre_button("Back", mouse[0], mouse[1], constant.WIDTH / 2 - 100, 700, 200, 50, constant.grey_color, constant.white_color, 25, 20):
            main_menu()

        pygame.display.update()
