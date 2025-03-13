from tkinter.constants import CENTER
from PIL import Image, ImageDraw
import pygame,datetime
from datetime import datetime
pygame.init()
screen=pygame.display.set_mode((782,800))
r=True
background = pygame.image.load("img.png")
font=pygame.font.Font(None,35)
strelka_s = pygame.image.load("sss-Photoroom.png")
strelka_m=pygame.image.load("minut.png")
strelka_h=pygame.image.load("sagat.png")
#strelka = pygame.transform.scale(strelka, (100, 400))

while r:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            r = False
    screen.blit(background, (0, 0))
    now=datetime.now()
    secunds=now.second
    hour=now.hour%12
    minuts=now.minute
    ang_s=secunds*6
    ang_m=minuts*6+secunds*0.1
    ang_h=hour*30+minuts*0.5
    rotated_s=pygame.transform.rotate(strelka_s,-ang_s)
    rotated_ss = rotated_s.get_rect(center=(391,400))
    screen.blit(rotated_s,rotated_ss)
    rotated_m=pygame.transform.rotate(strelka_m,-ang_m)
    rotated_mm=rotated_m.get_rect(center=(391,400))
    screen.blit(rotated_m,rotated_mm)
    rotated_h=pygame.transform.rotate(strelka_h,-ang_h)
    rotated_hh=rotated_h.get_rect(center=(391,400))
    screen.blit(rotated_h,rotated_hh)



    pygame.display.update()







