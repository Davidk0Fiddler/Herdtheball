import pygame
from setting import *
from colors import *


current_application_width = application_window_width1
current_application_height = application_window_height2
pygame.init()


application_window = pygame.display.set(current_application_width, current_application_height)

while application_running:
    application_window.fill(RGBColors.black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            application_running = False

    pygame.display.flip()    

pygame.quit()