""""""
def choice():
   f = True
   while f == True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   pygame.quit()

       # mouse position
       mouse = pygame.mouse.get_pos()
       click = pygame.mouse.get_pressed()
       player_1 = players_2 = players_3 = players_4 = best5 = -1
       set_up.game_layout_display.blit(set_up.posts, (0, 0))
       # Single player button

       player_1 = player_button("Single Player", mouse[0], mouse[1], (constant.WIDTH / 2 - 150), 250, 300, 50, constant.green_color,
                      constant.blue_green_color, 30, "s")
       # 2 player button
       players_2 = player_button("2 Players", mouse[0], mouse[1], (constant.WIDTH / 2) - 150, 350, 300, 50, constant.green_color,
                      constant.blue_green_color, 30, 2)
       # 3 player
       players_3 = player_button("3 Players", mouse[0], mouse[1], (constant.WIDTH / 2) - 150, 450, 300, 50, constant.green_color,
                      constant.blue_green_color, 30, 3)
       # 4 player
       players_4 = player_button("4 Players", mouse[0], mouse[1], (constant.WIDTH / 2) - 150, 550, 300, 50, constant.green_color, constant.blue_green_color, 30, 4)
       # Back button
       best5 = player_button("Back", mouse[0], mouse[1], 0, 650, 200, 50, constant.red_color, constant.blue_red_color, 30, 5)





