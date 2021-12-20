import pygame
import sys



class Packmen:
    def __init__(self):
        pygame.init()
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

    def draw_pakmen(self):
        pygame.draw.circle(self.screen, self.color, (self.x,self.y), self.radius,0)
        pygame.display.flip()

    def start(self):
        while True:
            self.get_keys()
            self.draw_pakmen()
            self.move()
            self.scor()

    def get_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def dead(self, ghosts):
        ...
    def scor(self):
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render('Score:', True,
                          (180, 0, 0))

        self.screen.blit(text1, (500, 50))
        pygame.display.update()

    def eat_ghosts(self):
        if self.pill < 4:
            self.damage_pill = 100
            self.health = 1



    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x = self.x - self.fps
                if event.key == pygame.K_RIGHT:
                    self.x = self.x + self.fps
                if event.key == pygame.K_UP:
                    self.y = self.y - self.fps
                if event.key == pygame.K_DOWN:
                    self.y = self.y + self.fps


pakmen = Packmen()
pakmen.start()
