import pygame
import sys
from components.Button import Button
from components.SpriteSheet import SpriteSheet
from screens.screen import Screen, Screen_manager
from backend.connector import connector

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()
cnx = connector()

class Delete:
    tipo: str

    def __init__(self, tipo):
        self.tipo = tipo
        self.selected_item_id = None  # Adiciona um atributo para armazenar o ID selecionado

    def select_delete(self):
        running = True

        # IMAGEM DO BOTÃO
        fundo_button = SpriteSheet().cria_fundo_botao(250)

        # IMAGEM PAINEL
        fundo_painel = SpriteSheet().cria_painel(SCREEN_WIDTH - 100)

        while running:
            try:
                selecao_mouse = pygame.mouse.get_pos()

                if self.tipo == 'turmas':
                    pygame.display.set_caption("Turmas")
                    if hasattr(cnx, 'solicitar_turma'):
                        items = cnx.solicitar_turma()
                    else:
                        raise AttributeError("The connector object does not have a method 'solicitar_turma'")
                elif self.tipo == 'contas':
                    pygame.display.set_caption("Contas")
                    if hasattr(cnx, 'solicitar_aluno'):
                        items = cnx.solicitar_aluno()
                    else:
                        raise AttributeError("The connector object does not have a method 'solicitar_aluno'")
                else:
                    continue

                x = 200
                y = 150
                x_max = 800
                buttons = []
                button_to_id = {}  # Dicionário para mapear botões para IDs

                # Criação dos botões para cada item
                for item in items:
                    item_id = item[0] if isinstance(item, (list, tuple)) else item
                    btn = Button(image=fundo_button, pos=(x, y), text_input=item[1] if isinstance(item, (list, tuple)) else item)
                    buttons.append(btn)
                    button_to_id[btn] = item_id  # Mapeia o botão para o ID do item
                    x += 280
                    if x >= x_max:
                        y += 150
                        x = 200 # Redefine x para 200

                screen.blit(fundo_painel, (50, 20))

                botao_delete = Button(image=fundo_button, pos=(SCREEN_WIDTH / 2 + 150, 650), text_input="DELETAR")
                botao_voltar = Button(image=fundo_button, pos=(SCREEN_WIDTH / 2 - 150, 650), text_input="VOLTAR")

                for button in [botao_delete, botao_voltar]:
                    button.changeColor(selecao_mouse)
                    button.update(screen)

                # Atualização dos botões na tela
                for btn in buttons:
                    btn.changeColor(selecao_mouse)
                    btn.update(screen)

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for btn in buttons:
                            if btn.checkForInput(selecao_mouse):
                                self.selected_item_id = button_to_id[btn]  # Armazena o ID do item selecionado
                        if botao_delete.checkForInput(selecao_mouse):
                            if self.selected_item_id is not None:
                                if self.tipo == 'turmas' and hasattr(cnx, 'deletar_turma'):
                                    cnx.deletar_turma(id=self.selected_item_id)  # Usa o ID do item selecionado
                                elif self.tipo == 'contas' and hasattr(cnx, 'deletar_aluno'):
                                    cnx.deletar_aluno(id=self.selected_item_id)  # Usa o ID do item selecionado
                        if botao_voltar.checkForInput(selecao_mouse):
                            screen_manager.pop_screen()
                            running = False
            except Exception as e:
                print(f"An error occurred: {e}")
                pygame.quit()
                sys.exit()
