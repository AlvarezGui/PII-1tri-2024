import pygame


class Screen():
    SCREEN_WIDTH = 1020
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    ''''
    Colocar essa classe como PAI para todas as screens
    '''
class Screen_manager:
    def __init__(self):
        self.screen_stack = []

    def push_screen(self, screen):
        self.screen_stack.append(screen)

    def pop_screen(self):
        if self.screen_stack:
            self.screen_stack.pop()

    def current_screen(self):
        if self.screen_stack:
            return self.screen_stack[-1]
        return None
        