import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
score = 0
level = 1
speed = 10

font_small = pygame.font.SysFont("Verdana", 20)

snake = [(200, 200)]
direction = (20, 0)

#GENERATE FOOD
def generate_food():
    while True:
        new_food = (random.randrange(0, 800, 20), random.randrange(0, 600, 20))
        if new_food not in snake:
            return new_food


food = generate_food()

#CHECK BORDER AND SNAKE TOUCH
def check_collision():
    head = snake[0]
    if head[0] < 0 or head[0] >= 800 or head[1] < 0 or head[1] >= 600:
        return True
    if head in snake[1:]:
        return True
    return False

#DEATH SCREEN
def game_over():
    screen.fill((0, 0, 0))
    text = font_small.render("GAME OVER", True, (255, 0, 0))
    screen.blit(text, (330, 250))
    score_text = font_small.render(f"Final Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (340, 280))
    pygame.display.flip()

    pygame.time.delay(2000)
    sys.exit()

#GAME CYCLE
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #MOTION WAY
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 20):
                direction = (0, -20)
            if event.key == pygame.K_DOWN and direction != (0, -20):
                direction = (0, 20)
            if event.key == pygame.K_LEFT and direction != (20, 0):
                direction = (-20, 0)
            if event.key == pygame.K_RIGHT and direction != (-20, 0):
                direction = (20, 0)

    if check_collision():
        game_over()

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
#IF SNEAK EATS APPLE
    if new_head == food:
        food = generate_food()
        snake.append(snake[-1])
        score += 1


        if score % 3 == 0:
            level += 1
            speed += 2

    snake = [new_head] + snake[:-1]

    screen.fill((50, 205, 50))
    #SHOWS STATISTICS
    score_text = font_small.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font_small.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (700, 10))
    screen.blit(level_text, (700, 30))
#DRAW SNAKE
    for segment in snake:
        pygame.draw.rect(screen, (0, 0, 255), (*segment, 20, 20))
#DRAW APPLE
    pygame.draw.rect(screen, (255, 0, 0), (*food, 20, 20))

    pygame.display.flip()
    clock.tick(speed)