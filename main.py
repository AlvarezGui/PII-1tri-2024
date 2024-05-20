import pygame
from screens.Cadastro import Cadastro
from screens.screen import Screen_manager

pygame.init()

screen_manager = Screen_manager()
cad = Cadastro()

while True:
    screen_manager.push_screen(cad.run())
    current_screen = screen_manager.current_screen()
    if current_screen:
        current_screen() 
