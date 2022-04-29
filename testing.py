#start

import pygame

black_color = (10, 10, 10)
green_color = (0, 200, 0)
mother_board = pygame.image.load("src/snakes.jpg")
pygame.init()
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.Font("src/Qarolina.ttf", 21)

while mother_board == True:
    screen.fill(black_color)
    for events in pygame.event.get():  # look at all events in pygame
         if events.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
            text = font.render(f"{mouse_position[0]}, {mouse_position[1]}", True, green_color)
            textRect = text.get_rect()
            textRect.center = (77, 77)
            screen.blit(mother_board, (350, 35))
            screen.blit(text, textRect)
            pygame.display.update()
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    pygame.quit()

    # end