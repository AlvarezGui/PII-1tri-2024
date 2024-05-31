import pygame
import sys
from components.Button import Button
from screens.screen import Screen_manager
from components.SpriteSheet import SpriteSheet

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

# FONTE
CAMINHO_FONTE = "./m6x11plus.ttf"
base_font = pygame.font.Font(CAMINHO_FONTE, 32)

class PerguntaJogo:
    def __init__(self, enunciado, alternativas, resposta_correta, respostas):
        self.enunciado = enunciado
        self.alternativas = alternativas
        self.resposta_correta = resposta_correta.lower()
        self.respostas = respostas

    def run(self):
        running = True
        fundo_painel = SpriteSheet().cria_painel(SCREEN_WIDTH-100)
        fundo_button_alternativas = SpriteSheet().cria_fundo_botao_pequeno(70)

        start_pos = pygame.Vector2(((SCREEN_WIDTH/3 - 250), 70))
        texts = []
        words = []
        total_width = 0
        indice = 0
        words = self.enunciado.split(" ")
        for i in words:
            indice = words.index(i)
            word = base_font.render(i, True, ("white"))
            if total_width + word.get_width() > (SCREEN_WIDTH - 300):
                start_pos.y += 20
                total_width = 0
                texts.append(Escrita(((start_pos.x, start_pos.y)), ' '.join(words[:indice + 1])))
                words = words[indice + 1:]

            elif total_width < (SCREEN_WIDTH - 300) and indice == len(words) - 1:
                start_pos.y += 20
                texts.append(Escrita(((start_pos.x, start_pos.y)), ' '.join(words[:indice + 1])))

            total_width += word.get_width()

        while running:
            pygame.display.set_caption("PERGUNTA!")
            selecao_mouse = pygame.mouse.get_pos()

            screen.blit(fundo_painel, (50, 20))
            for i in texts:
                i.draw(screen)

            pos_y = SCREEN_HEIGHT / 2
            pos_x = ((SCREEN_WIDTH / 3) - 200)
            counter = 0
            if self.alternativas == 5:
                for c in self.respostas:
                    match counter:
                        case 0:
                            n = "A) "
                        case 1:
                            n = "B) "
                        case 2:
                            n = "C) "
                        case 3:
                            n = "D) "
                        case 4:
                            n = "E) "
                    formatada = str(n) + str(c)
                    alternativa = base_font.render(formatada, True, ("white"))
                    screen.blit(alternativa, (pos_x, pos_y))
                    pos_y += 30
                    counter += 1

                botao_a = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 - 250, 650), text_input="A")
                botao_b = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 - 125, 650), text_input="B")
                botao_c = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2, 650), text_input="C")
                botao_d = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 + 125, 650), text_input="D")
                botao_e = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 + 250, 650), text_input="E")
                for button in [botao_a, botao_b, botao_c, botao_d, botao_e]:
                    button.changeColor(selecao_mouse)
                    button.update(screen)

            if self.alternativas == 4:
                for c in self.respostas:
                    match counter:
                        case 0:
                            n = "A) "
                        case 1:
                            n = "B) "
                        case 2:
                            n = "C) "
                        case 3:
                            n = "D) "
                    formatada = str(n) + str(c)
                    alternativa = base_font.render(formatada, True, ("white"))
                    screen.blit(alternativa, (pos_x, pos_y))
                    pos_y += 30
                    counter += 1
                
                botao_a = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 - 187.5, 650), text_input="A")
                botao_b = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 - 62.5, 650), text_input="B")
                botao_c = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 + 62.5, 650), text_input="C")
                botao_d = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 + 185.5, 650), text_input="D")
                for button in [botao_a, botao_b, botao_c, botao_d]:
                    button.changeColor(selecao_mouse)
                    button.update(screen)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.alternativas == 5:
                        if botao_a.checkForInput(selecao_mouse):
                            print("Alternativa A")
                            if self.resposta_correta == "a":
                                screen_manager.pop_screen()
                                return True
                            else:
                                screen_manager.pop_screen()
                                return False
                        if botao_b.checkForInput(selecao_mouse):
                            print("Alternativa B")
                            if self.resposta_correta == "b":
                                screen_manager.pop_screen()
                                return True
                            else:
                                screen_manager.pop_screen()
                                return False
                        if botao_c.checkForInput(selecao_mouse):
                            print("Alternativa C")
                            if self.resposta_correta == "c":
                                screen_manager.pop_screen()
                                return True
                            else:
                                screen_manager.pop_screen()
                                return False
                        if botao_d.checkForInput(selecao_mouse):
                            print("Alternativa D")
                            if self.resposta_correta == "d":
                                screen_manager.pop_screen()
                                return True
                            else:
                                screen_manager.pop_screen()
                                return False
                        if botao_e.checkForInput(selecao_mouse):
                            print("Alternativa E")
                            if self.resposta_correta == "e":
                                screen_manager.pop_screen()
                                return True
                            else:
                                screen_manager.pop_screen()
                                return False
                            
                    else:
                        if botao_a.checkForInput(selecao_mouse):
                            print("Alternativa A")
                            if self.resposta_correta == "a":
                                screen_manager.pop_screen()
                                return True
                            else:
                                screen_manager.pop_screen()
                                return False
                        if botao_b.checkForInput(selecao_mouse):
                            print("Alternativa B")
                            if self.resposta_correta == "b":
                                screen_manager.pop_screen()
                                return True
                            else:
                                screen_manager.pop_screen()
                                return False
                        if botao_c.checkForInput(selecao_mouse):
                            print("Alternativa C")
                            if self.resposta_correta == "c":
                                screen_manager.pop_screen()
                                return True
                            else:
                                screen_manager.pop_screen()
                                return False
                        if botao_d.checkForInput(selecao_mouse):
                            print("Alternativa D")
                            if self.resposta_correta == "d":
                                screen_manager.pop_screen()
                                return True
                            else:
                                screen_manager.pop_screen()
                                return False

            pygame.display.update()

class Escrita:
    def __init__(self, pos:tuple[float, float], text:str):
        self.pos = pos
        self.text = text

    def draw(self, surface):
        text_surface = base_font.render(self.text, True, ("white"))
        text_rect = text_surface.get_rect(topleft=self.pos)
        surface.blit(text_surface, text_rect)