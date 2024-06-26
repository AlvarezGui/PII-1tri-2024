from random import randint
import time
import random
import pygame
from components.Button import Button
from backend.connector import connector
from components.SpriteSheet import SpriteSheet
from components.levels.jogador import Jogador
from components.levels.obstaculo import Obstaculo
from components.levels.perguntaBox import PerguntaBox
from components.levels.pergunta_jogo import PerguntaJogo
from screens.screen import Screen_manager, Screen
from pygame.sprite import Group

clock = pygame.time.Clock()
cnx = connector()

class Fase():
    def __init__(self, dific, model):
        self.dific = dific
        self.SCREEN_WIDTH = 1020
        self.SCREEN_HEIGHT = 800
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen_manager = Screen_manager()
        self.model = model
        self.all_sprites = Group()
        self.obstacles = Group()
        self.questions = Group()

        self.numero_de_perguntas = cnx.numero_de_perguntas()

        self.qnt_pontos = 0

        # FONTE
        self.CAMINHO_FONTE = "./m6x11plus.ttf"
        self.base_font = pygame.font.Font(self.CAMINHO_FONTE, 60)

    def desenhar_fase(self):
        running = True
        # CRIANDO IMAGENS
        fundo_image = Screen.cria_fundo(self.SCREEN_WIDTH)
        fundo_crono = SpriteSheet().cria_fundo_crono(150)

        # CRIANDO COMPONENTES DE FASE
        #JOGADOR
        jgdr = Jogador(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.screen, self.model)
        self.all_sprites.add(jgdr)
        # OBSTÁCULOS
        for i in range(self.dific):
            obs = Obstaculo(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.screen, self.dific)
            self.obstacles.add(obs)
            self.all_sprites.add(obs)
        # PERGUNTASBOX
        if self.dific > 5:
            for c in range(self.dific // 5):
                quest = PerguntaBox(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.screen)
                self.questions.add(quest)
                self.all_sprites.add(quest)

        botao_sair = Button(image=None, pos=(self.SCREEN_WIDTH * 2/3, 750), text_input="VOLTAR")

        #DEFININDO O TEMPO COMEÇO
        self.tempo_inicio = time.time()
        
        # SETANDO QUESTÕES COMO NÃO ATIVAS
        for q in self.questions:
            q.is_active = False
        
        y = 0
        fundo_height = fundo_image.get_height()

        while running:
            self.screen.fill((0, 0, 0))
            # Move o fundo para criar a ilusão de avanço
            y += 3  # Ajuste a velocidade de rolagem conforme necessário
            if y >= fundo_height:
                y = 0

            self.screen.blit(fundo_image, (0, y))
            self.screen.blit(fundo_image, (0, y - fundo_height))

            # SETANDO O CRONOMETRO
            self.tempo_atual = time.strftime("%M:%S", time.gmtime(time.time() - self.tempo_inicio))
            crono = self.base_font.render(self.tempo_atual, True, ('white'))
            self.screen.blit(fundo_crono, (25, 40))
            self.screen.blit(crono, (50, 50))

            label_vidas = pygame.font.Font(self.CAMINHO_FONTE, 20).render("VIDAS", True, ("white"))
            self.screen.blit(label_vidas, (200, 30))
            vidas = self.base_font.render(str(jgdr.vida), True, ("white"))
            self.screen.blit(vidas, (200, 50))

            label_pontos = pygame.font.Font(self.CAMINHO_FONTE, 20).render("PONTOS", True, ("white"))
            self.screen.blit(label_pontos, (300, 30))
            pontos = self.base_font.render(str(self.qnt_pontos), True, ("white"))
            self.screen.blit(pontos, (300, 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    jogar_mouse = pygame.mouse.get_pos()
                    if botao_sair.checkForInput(jogar_mouse):
                        self.screen_manager.pop_screen()
                        running = False
                        return self.qnt_pontos

            if self.dific > 5:
                for quest in self.questions:
                    if not quest.is_active:
                        for obs in self.obstacles:
                            obs.update(jgdr)
                        
                        for quest in self.questions:
                            quest.update(jgdr)
                        keys = pygame.key.get_pressed()
                        jgdr.update(keys)
                    else:
                        escolha_pergunta = random.randrange(1, self.numero_de_perguntas + 1)
                        pergunta = cnx.solicitar_pergunta(escolha_pergunta)
                        enunciado = pergunta[1]
                        respostas = (pergunta[3], pergunta[4], pergunta[5], pergunta[6], pergunta[7])
                        alternativas = 5
                        resposta_correta = pergunta[2]
                        perg = PerguntaJogo(enunciado, alternativas, resposta_correta, respostas).run()
                        self.screen_manager.push_screen(perg)

                        # FAZENDO A PERGUNTA
                        perg = PerguntaJogo(enunciado, alternativas, resposta_correta, respostas).run()
                        self.screen_manager.push_screen(perg)
                        if perg:
                            self.qnt_pontos += 100
                            for q in self.questions:
                                q.is_active = False
                                q.respawn()
                            for o in self.obstacles:
                                o.respawn()
                        if not perg:
                            for q in self.questions:
                                q.is_active = False
                                q.respawn()
                            for o in self.obstacles:
                                o.respawn()
                            jgdr.tira_vida()
            else:
                for obs in self.obstacles:
                    obs.update(jgdr)

                keys = pygame.key.get_pressed()
                jgdr.update(keys)

            self.all_sprites.draw(self.screen)

            jogar_mouse = pygame.mouse.get_pos()
            botao_sair.changeColor(jogar_mouse)
            botao_sair.update(self.screen)

            pygame.display.update()
            if jgdr.vida <= 0:
                running = False
                self.screen_manager.pop_screen()
                return self.qnt_pontos
            clock.tick(60)
