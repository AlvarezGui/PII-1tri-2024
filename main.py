import pygame
import pygame.mixer
from screens.Validar import Validar
from screens.screen import Screen_manager

pygame.init()

screen_manager = Screen_manager()
cad = Validar()

while True:
    screen_manager.push_screen(cad.run())
    current_screen = screen_manager.current_screen()
    if current_screen:
        current_screen() 


# pip freeze > requirements.txt - para add novos requerimentos
# pip install -r requirements.txt - para instalar requerimentos
