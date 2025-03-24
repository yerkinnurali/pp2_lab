import pygame,random,time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((400,600))
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
grey = pygame.Color(128, 128, 128)
red = pygame.Color(255, 0, 0)
speed=1
score=0
score_coin=0
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)
score_show = font.render(f"Money:{score_coin}", True, black)
background = pygame.image.load("doroga.jpg")
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(image, (44,96))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 400:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale(image, (60,80))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,360), 0)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if (self.rect.top > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), 0)

    def respawn(self):
        self.rect.center = (random.randint(40, 360),0)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if (self.rect.top > 600):

            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
#create sprites
P1=Player()
E1=Enemy()
C1=Coin()
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:

     for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
        if event.type == INC_SPEED:
            speed += 1

     screen.blit(background, (0, 0))
     scores = font_small.render(str(score), True, black)
     screen.blit(scores, (10, 10))
     score_text = font_small.render(str(score_coin), True, black)
     screen.blit(score_text, (360, 10))
     for entity in all_sprites:
         screen.blit(entity.image, entity.rect)
         entity.move()
     for entity in coins:
         entity.move()
         screen.blit(entity.image, entity.rect)
     if pygame.sprite.spritecollideany(P1, coins):
         score_coin += 1
         C1.respawn()

     if pygame.sprite.spritecollideany(P1, enemies):
         pygame.mixer.Sound('crash.wav').play()
         screen.fill(red)
         screen.blit(game_over, (30, 200))
         score_show = font.render(f"Money: {score_coin}", True, black)
         screen.blit(score_show, (30, 250))
         pygame.display.update()
         for entity in all_sprites:
             entity.kill()
         time.sleep(2)
         pygame.quit()


     pygame.display.update()
     pygame.time.Clock().tick(60)
     screen.fill(white)
