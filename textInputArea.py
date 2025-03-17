import pygame
from colors import *

font = pygame.font.Font(None, 50)

class TextInputBox:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = RGBColors.gray
        self.text = ""
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = RGBColors.blue if self.active else RGBColors.gray

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(f"Beírt szöveg: {self.text}")
                    self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        txt_surface = font.render(self.text, True, RGBColors.black)
        width = max(400, txt_surface.get_width() + 10)
        self.rect.w = width
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

# DOKUMENTÁCIÓ
# 
# Az eventekhez be kell írni ezt: {INPUT BOX NAME}.handle_event(event) (Egy szinten kell lennie a pygame.QUIT eventtel)
# A megjelenítést a {INPUT BOX NAME}.draw(screen) metódust kell használni.
# Az osztály attribútumai: x = balfelső sarok x-koordinátája, y = balfelső sarok y-koordinátája, w = az input mező szélessége, h = az input mező magassága
#
