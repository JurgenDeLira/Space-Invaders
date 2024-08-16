import pygame
import os
from GameClass import Game
from EnemyClass import Enemy
from ShipClass import Ship
from BulletClass import Bullet


current_dir = os.path.dirname(__file__)
BACKGROUND = pygame.image.load(os.path.join('img', "background.png"))
BULLET_IMAGE = pygame.image.load(os.path.join('img', 'bullet_image.png'))
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

class Drawing:
    def __init__(self, window):
        self.window = window

    def drawing(self,game, player,enemies, FPS):
        self.window.blit(BACKGROUND, (0,0))
        player.fire(self.window) # nueva línea
        for enemy in enemies[:]:
            enemy.draw(self.window)
        player.draw(self.window) #nueva línea
        game.draw_HUD()
        
        pygame.display.update()
        


#### Código de ejemplo

def main():
    run = True
    clock = pygame.time.Clock()
    drawing = Drawing(WIN)
    enemies = Enemy(4).create(50)
    game = Game(pygame.font.SysFont('comicsans', 30), 60, 3, WIN, WIDTH, HEIGHT, 4)
    bullet_example = Bullet(300, 400, BULLET_IMAGE)


    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            for enemy in enemies:
                enemy.move()
        player = ""
        drawing.drawing(game, player, enemies, 60)
        bullet_example.draw(WIN)
        pygame.display.update()
    pygame.quit()

pygame.init()
main()