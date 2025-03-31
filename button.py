import pygame
from colors import *
pygame.init()

font = pygame.font.Font(None, 50)

class Button:
    def __init__(self, x, y, width, height, text, function):
        self.rect = pygame.Rect(x, y, width, height)
        self.width = width
        self.height = height
        self.text = text
        self.function = function

    def draw(self, screen):
        font_size = max(10, int(self.height * 0.75))
        font = pygame.font.Font(None, font_size)

        txt_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = txt_surface.get_rect(center=self.rect.center)

        pygame.draw.rect(screen, (0, 0, 0), self.rect)
        screen.blit(txt_surface, text_rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.function:  # Ha van megadott függvény
                    self.function()

r = True

def displaying_methods(application_window):
    application_window.fill(RGBColors.white)
    button.draw(application_window)
    pygame.display.flip()

application_window = pygame.display.set_mode((1000,1000))
button = Button(10,10,300,100,'ASD','ASD')
while r:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = False
    
    displaying_methods(application_window)

pygame.quit()