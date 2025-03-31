import pygame
from settings import *
from colors import *

pygame.init()

size_number = 3

def selecting_size(number):
    width_var = f"application_window_width{number}"
    height_var = f"application_window_height{number}"

    current_application_width = globals().get(width_var, 0)
    current_application_height = globals().get(height_var, 0)

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