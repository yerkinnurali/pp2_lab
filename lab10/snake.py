import pygame, sys, random, psycopg2

#connect to database
conn = psycopg2.connect(
    host="localhost",
    database="snake_game.db",
    user="postgres",
    password="******"
)
cur = conn.cursor()

# Player name
username = input("Your name: ")

# search player
cur.execute("SELECT id, score, level FROM players WHERE username = %s;", (username,))
player = cur.fetchone()

#
if player is None:
    cur.execute("INSERT INTO players (username) VALUES (%s) RETURNING id, score, level;", (username,))
    user_id, score, level = cur.fetchone()
    conn.commit()
    print("New user created.")
else:
    user_id, score, level = player
    print("Welcome,", username)

# speed
speed = 10 + (level - 1) * 2



pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

snake = [(100, 100)]
direction = (20, 0)


def make_food():
    x = random.randint(0, 39) * 20
    y = random.randint(0, 29) * 20
    return x, y


food = make_food()


def game_over():
    cur.execute("UPDATE players SET score = %s, level = %s WHERE id = %s;", (score, level, user_id))
    conn.commit()
    cur.close()
    conn.close()

    pygame.quit()
    print("Game Over. Score:", score)
    sys.exit()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 20):
                direction = (0, -20)
            if event.key == pygame.K_DOWN and direction != (0, -20):
                direction = (0, 20)
            if event.key == pygame.K_LEFT and direction != (20, 0):
                direction = (-20, 0)
            if event.key == pygame.K_RIGHT and direction != (-20, 0):
                direction = (20, 0)
            if event.key == pygame.K_p:
                cur.execute("UPDATE players SET score = %s, level = %s WHERE id = %s;", (score, level, user_id))
                conn.commit()
                print("Game paused. Press P again.")
                paused = True
                while paused:
                    for e in pygame.event.get():
                        if e.type == pygame.KEYDOWN and e.key == pygame.K_p:
                            paused = False


    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    if head[0] < 0 or head[0] >= 800 or head[1] < 0 or head[1] >= 600 or head in snake:
        game_over()

    snake = [head] + snake

    if head == food:
        score += 1
        if score % 3 == 0:
            level += 1
            speed += 2
        food = make_food()
    else:
        snake.pop()


    screen.fill((0, 0, 0))
    for s in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*s, 20, 20))
    pygame.draw.rect(screen, (255, 0, 0), (*food, 20, 20))


    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))

    pygame.display.flip()
    clock.tick(speed)
