import pygame
from pygame import K_SPACE,KEYDOWN,K_RIGHT,K_LEFT

pygame.init()
tracks = ["Secunda.mp3","ambient.mp3"]
i = 0
play=False
pygame.mixer.init()
pygame.mixer.music.load(tracks[i])
screen = pygame.display.set_mode((800, 600))
run=True
font = pygame.font.Font(None, 50)
while run:
    screen.fill((30, 30, 30))


    track_text = font.render(f"Track: {tracks[i]}", True, (255, 255, 255))
    screen.blit(track_text, (100, 50))


    play_text = font.render("Play/Pause [SPACE]", True, (0, 255, 0))
    next_text = font.render("Next Track [->]", True, (0, 255, 255))

    screen.blit(play_text, (100, 200))
    screen.blit(next_text, (100, 300))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type ==KEYDOWN:
            if event.key==K_SPACE:
              if play==True:
                  pygame.mixer.music.pause()
                  play==False
              else:
                     pygame.mixer.music.play()

            elif event.key == K_RIGHT:
             i = (i+ 1) % len(tracks)

            elif event.key == K_LEFT:
             i = (i-1) % len(tracks)
            pygame.mixer.music.load(tracks[i])
            pygame.mixer.music.play()
