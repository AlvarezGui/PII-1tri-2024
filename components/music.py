import pygame
import pygame.mixer

pygame.mixer.init()

class Music:
    def __init__(self):
        self.musica_de_fundo = pygame.mixer.music.load('man-is-he-mega-glbml-22045.mp3')
        self.volume = 0.03
        pygame.mixer.music.set_volume(self.volume)

    def play(self):
        pygame.mixer.music.play(-1)

    @staticmethod
    def aumenta_volume():
        volume = pygame.mixer.music.get_volume()  # Obtém o volume atual
        volume += 0.1  # Incrementa o volume em 0.1
        volume = min(1.0, volume)  # Limita o volume máximo a 1.0
        pygame.mixer.music.set_volume(volume)

    @staticmethod
    def diminui_volume():
        volume = pygame.mixer.music.get_volume()  # Obtém o volume atual
        volume -= 0.1  # Decrementa o volume em 0.1
        volume = max(0.0, volume)  # Limita o volume mínimo a 0.0
        pygame.mixer.music.set_volume(volume)