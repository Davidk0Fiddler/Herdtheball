import pygame
from settings import *
from colors import *

pygame.init()

size_number = 1

def selecting_size(number):
    current_application_width = 0
    current_application_height = 0  

    selector_w = f'current_application_width = application_window_width{number}'
    selector_h = f'current_application_height = application_window_height{number}'

    exec(selector_w)
    exec(selector_h)

    return (current_application_width, current_application_height)

def displaying_methods(application_window):
    application_window.fill(RGBColors.black)
    pygame.display.flip()    

application_window = pygame.display.set_mode(selecting_size(size_number))

while application_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            application_running = False
    
    displaying_methods(application_window)
pygame.quit()