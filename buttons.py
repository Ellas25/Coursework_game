import pygame

class button1: #play button
    color_dark = (100, 100, 100)
    pygame.draw.rect(displaysurface, color_dark, [590, 315, 80, 30])

    font_sizes = ("arial", 14)
    texts = smaller_font.render("PLAY", True, color_lighters)
    display_surface.blit(text(600, 320))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN: # this is left click only not right
                if 160 <= mouse[0] <= 67 and 31 <= mouse[1] <= 34:
                    event_handler.load()

class button2: #quitbutton
    color_dark = (100, 100, 100)
    pygame.draw.rect(displaysurface, color_dark, [590, 315, 80, 30])

    font_sizes = ("arial", 14)
    texts = smaller_font.render("QUITTING THE GAME", True, color_lighters)
    display_surface.blit(text(600, 320))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN: # this is left click only not right
                if 160 <= mouse[0] <= 67 and 31 <= mouse[1] <= 34:
                    event_handler.load()

class button3: #play button
    color_dark = (100, 100, 100)
    pygame.draw.rect(displaysurface, color_dark, [590, 315, 80, 30])

    font_sizes = ("arial", 14)
    texts = smaller_font.render("Player_1", True, color_lighters)
    display_surface.blit(text(600, 320))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN: # this is left click only not right
                if 160 <= mouse[0] <= 67 and 31 <= mouse[1] <= 34:
                    event_handler.load()