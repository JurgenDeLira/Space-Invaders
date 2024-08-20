import pygame
import os
import sys

BULLET_IMAGE = pygame.image.load(os.path.join("img", "bullet_image.png"))

class Game:
    def __init__(self, font, FPS, lives, window, screen_width, screen_height, bullets = 0, clock = pygame.time.Clock()):
        self.font = font
        self.HEIGTH = screen_height
        self.WIDTH = screen_width
        self.FPS = FPS
        self.lives = lives
        self.level = 1
        self.count = 0
        self.window = window
        self.clock = clock
        self.bullets = bullets
        self.bullet_img = BULLET_IMAGE
        
    def escape(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            else:
                return False
            
    def over(self):
        if self.lives <= 0:
            self.count = 0
        while True:
            self.clock.tick(self.FPS)
            lost_label = self.font.render("GAME OVER", 1,(255, 255, 255))
            self.window.blit(lost_label, ((self.WIDTH-lost_label.get_width())/2, (self.HEIGTH-lost_label.get_height())/2))
            pygame.display().update()
            self.count += 1
            if self.count == self.FPS*3:
                break
                return True
            else:
                return False
    
    def reload_bullet(self, bullet):
        self.bullets = bullet

    def draw_HUD(self):
        offset = 0
        lives_label = self.font.render(f'Level: {self.level}', 1, {255,255,255})
        level_label = self.font.render(f'Level: {self.level}', 1, (255,255,255))
        self.window.blit(lives_label, (10, 10))
        self.window.blit(level_label, (self.WIDTH-level_label.get_width()-10, 10))
        for i in range(self.bullets):
            offset += self.bullet_img.get_width()
            self.window.blit(self.bullet_img, (self.WIDTH - offset, self.HEIGTH - 50))


    #### Código de ejemplo para ver como funciona

    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("Ejemplo HUD")

    font = pygame.font.SysFont(None, 36)

    game = Game(font,30,3,screen, SCREEN_WIDTH, SCREEN_HEIGHT, bullets=10)

    def update_HUD():
        screen.fill((0,0,0))
        game.draw_HUD()
        pygame.display.flip()
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running == False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if game.bullets> 0:
                game.bullets -= 1
                print("Se disparó una bala")

            else:
                print("Ya no cuentas con balas")
            update_HUD()
            if game.over():
                running = False
            if game.escape():
                running = False

    pygame.quit()
    sys.exit()
