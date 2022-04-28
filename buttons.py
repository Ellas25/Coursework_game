import pygame
#from main_menu import main_menu
import main
screen = 1
"""
def centre_button(screen, position, text):
    font = pygame.font.SysFont("comicsans", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
    return screen.blit(text_render, (x, y))


def menu():
    b1 = centre_button(centre_button.screen, (400, 400), "Player1")
    b2 = centre_button(centre_button.screen, (500, 400), "Player2")
    
    b3 = centre_button(centre_button.screen, (600, 400), "Player3")
    b4 = centre_button(centre_button.screen, (700, 400), "player4")
    

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_start:
                    pass
        pygame.display.update()
    pygame.quit()

"""
# try again
"""
class Button():
    def __init__(self, text, width, height, pos):
        self.main_rect = pygame.Rect(pos(width,height))
        self.main_color = (0, 255, 0)
        # this has created the colour of the button and the size

        self.text_name = self.font.render(text, True, "#FFFFFFF")
        self.text_rect = self.text_surf.get_rect(center = self.main_rect)

        def draw(self):
            pygame.draw.rect(self.screen, self.main_color, self.main_rect)
            pygame.screen.blit(self.text_surf, self.text_rect)

button = button("play", 100, 20, (1500, 1874))

pygame.quit()
"""
"""
class Button:
    def create_button(self, surface, color, x, y, length, height, width, text, text_color):
        surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x,y, length, height)
        return surface

    def button_text(self, surface, text, text_color, length, height, x, y):
        font_size = int(length // len(text))
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x + length / 2) - myText.get_width() / 2, (y + height / 2) - myText.get_height() / 2))
        return surface

    def text_button(self, surface, color, length, height, x, y, width):
        for i in range(1, 10):
            s = pygame.Surface((length + (i * 2), height + (i * 2)))
            s.fill(color)
            alpha = (255 / (i + 2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x - i, y - i, length + i, height + i), width)
            surface.blit(s, (x - i, y - i))
        pygame.draw.rect(surface, color, (x, y, length, height), 0)
        pygame.draw.rect(surface, (190, 190, 190), (x, y, length, height), 1)
        return surface

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        print("Some button was pressed!")
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

"""
