import pygame
from screens.menu_principal import main_menu
from screens.screen import Screen_manager

pygame.init()

screen_manager = Screen_manager()

while True:
    screen_manager.push_screen(main_menu.inicia_main_menu())
    current_screen = screen_manager.current_screen()
    if current_screen:
        current_screen() 
