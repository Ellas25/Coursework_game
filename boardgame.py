import pygame 
import rgb
import dice

def dice(d):
    if d == 1:
        d = dice.d1
    elif d == 2:
        d = dice.d2
    elif d == 3:
        d = set_up.d3
    elif d == 4:
        d = dice.d4
    elif d == 5:
        d = dice.d5
    elif d == 6:
        d = dice.d6

    time_clock = pygame.time.get_ticks()  # fetches the time
    while pygame.time.get_ticks() - time_clock < 1000:  # 1000 milli seconds loads the image
        set_up.game_layout_display.blit(d, (300, 500))  # shows the image of the number
        pygame.display.update()  # updates the image on the screen


def choice(t):
    t = True
    while t == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        p1 = p_2 = p_3 = p_4 = best5 = -1
        game_layout_display.blit(.posts, (0, 0))
        # Single player button

        p_1 = player_button("You vs Robot", mouse[0], mouse[1], (main.width / 2 - 150), 250, 300, 50,
                            rgb.lime,
                            rgb.teal, 30, "s")
        # 2 player button
        p_2 = player_button("Duo", mouse[0], mouse[1], (main.width / 2) - 150, 350, 300, 50,
                                  rgb.lime,
                            rgb.blue_T, 30, 2)
        # 3 player
        players_3 = player_button("Trio", mouse[0], mouse[1], (main.width / 2) - 150, 450, 300, 50,
                                  rgb.lime,
                                  rgb.blue_l, 30, 3)
        # 4 player
        players_4 = player_button("4 Players", mouse[0], mouse[1], (constant.WIDTH / 2) - 150, 550, 300, 50,
                                  rgb.lime, rg.lime, 30, 4)
        # Back button
        best5 = player_button("Back", mouse[0], mouse[1], 0, 650, 200, 50,rgb.lime, rgb.red,
                              30, 5)

        class best_funct():
            if best5 == 5:
                pass
        if player_1 == "s":
            playing(21)
        if players_2 == 2:
            playing(2)
        if players_3 == 3:
            playing(3)
        if players_4 == 4:
            playing(4)
        pygame.display.update()
