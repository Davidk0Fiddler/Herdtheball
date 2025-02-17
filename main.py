import pygame
from settings import *
from colors import *

pygame.init()

current_application_width = application_window_width1
current_application_height = application_window_height1

def displaying_methods(application_window):
    application_window.fill(RGBColors.black)
    pygame.display.flip()    

application_window = pygame.display.set_mode((current_application_width, current_application_height))

while application_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            application_running = False
    
    displaying_methods(application_window)
pygame.quit()