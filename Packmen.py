import pygame
import sys
from pygame.color import THECOLORS

#TODO узнать что такое тернарный оператор
class Packmen:
    def __init__(self):
        pygame.init()
        self.score = 0
        self.color = (255, 255, 0)
        self.WINDOW_WIDTH = 700
        self.WINDOW_HEIGHT = 800
        self.radius = 25
        self.x = 350
        self.y = 750
        self.pill = 4
        self.is_over = False
        self.score = 0
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.fps = 25
        self.health = 100
        self.damage_pill = 1
        self.pakmen = pygame.draw.circle(self.screen, self.color, (self.x,self.y), self.radius,0)
        self.sprite = pygame.image.load("pakmen.png")

    def draw_pakmen(self):
        pygame.draw.circle(self.screen, self.color, (self.x,self.y), self.radius,0)
        pygame.display.flip()

    def start(self):
        while True:
            self.draw_pakmen()
            self.move()
            self.scor()
            self.sprite()


    def move(self):
        #TODO добавить обработку столкновений
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.x = self.x - self.fps
                        if event.key == pygame.K_RIGHT:
                            self.x = self.x + self.fps
                        if event.key == pygame.K_UP:
                            self.y = self.y - self.fps
                        if event.key == pygame.K_DOWN:
                            self.y = self.y + self.fps
            self.screen.fill(THECOLORS['black'])

            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius, 0)
            pygame.display.flip()
        #TODO надо сделать рекурсию



    #def dead(self, ghosts):
        #TODO сделать смерть пакмена


    def sprite(self):
        self.screen.blit(self.sprite, (350, 750))

    def scor(self):
        f1 = pygame.font.Font("arial", 36)
        text1 = f1.render('Score:', True,
                          (180, 0, 0))

        self.screen.blit(text1, (500, 30))
        pygame.display.update()

pakmen = Packmen()
pakmen.start()
