import pygame 
import os
pygame.init()
screen = pygame.display.set_mode((544,320))
BACKGROUND_IMGS = [pygame.transform.scale2x(pygame.image.load("imgs\\bg1.png")),
    pygame.transform.scale2x(pygame.image.load("imgs\\bg2.png")),
    pygame.transform.scale2x(pygame.image.load("imgs\\bg3.png")),
    pygame.transform.scale2x(pygame.image.load("imgs\\bg5.png")),
    pygame.transform.scale2x(pygame.image.load("imgs\\bg4.png"))]

class Background:
    def __init__(self):
        self.IMGS = BACKGROUND_IMGS
        self.IMGS1 = BACKGROUND_IMGS
        self.X = [0.0,0.0,0.0,0.0,0.0]
        self.X1 = []
        for i in range(len(BACKGROUND_IMGS)):
            self.X1.append(self.IMGS[i].get_width())
        #self.X1 = [self.IMGS[0].get_width(),self.IMGS[1].get_width(),self.IMGS[2].get_width(),self.IMGS[3].get_width(),self.IMGS[4].get_width()]
        self.Y = 0
        self.velo = [.0,.6,.9,1.2,1.5]
    def draw(self):
        for i in range(len(BACKGROUND_IMGS)):
            screen.blit(self.IMGS[i],(self.X[i],self.Y))
            screen.blit(self.IMGS1[i],(self.X1[i],self.Y))
    def move(self):
        for i in range(len(BACKGROUND_IMGS)):
            if self.X[i] < -self.IMGS[i].get_width():
                self.X[i] = self.IMGS[i].get_width()
            if self.X1[i] < -self.IMGS1[i].get_width():
                self.X1[i] = self.IMGS1[i].get_width()


            self.X[i] -= self.velo[i]
            self.X1[i] -= self.velo[i]




def main():
    bg = Background()
    clock = pygame.time.Clock()
    while True:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
        bg.draw()
        bg.move()
        pygame.display.update()

main()

