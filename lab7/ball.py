import pygame
pygame.init()

screen = pygame.display.set_mode((1920,1080))
x=960
y=540
s=20
r=True

while r:
    pygame.time.Clock().tick(60)
    for i in pygame.event.get():
        if i.type== pygame.QUIT:
            r=False
    m=pygame.key.get_pressed()
    if m[pygame.K_UP] and y>25:
        y=y-s
    if m[pygame.K_DOWN] and y<1055:
        y=y+s
    if m[pygame.K_RIGHT] and x<1895:
        x=x+s
    if m[pygame.K_LEFT] and x>25:
        x=x-s
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(255,0,0), (x,y),25)
    pygame.display.update()
