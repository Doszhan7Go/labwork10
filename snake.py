import pygame
from random import randrange
import psycopg2
from config import config

score_last = 4

print("Enter your username: ")
username = input()


sql = """
    SELECT * FROM snake_game_users WHERE username = %s;
    """
update = """
        UPDATE snake_game_score
        SET last_score = %s
        WHERE username = %s
    """
    
conn = None
try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, [username])
        
        dt = cur.fetchone()
        
        if dt == None:
            insert = f"""
            INSERT INTO snake_game_users VALUES(%s, {score_last});
            """
            cur.execute(insert, [username])
            conn.commit()
        
        cur.execute(sql, [username])
        dt = cur.fetchone()
        
except Exception as e:
        print(str(e))
finally:
        if conn is not None:
            conn.close()



res = 400
size = 20
line = (50,50,50)


x, y = randrange(0,res,size), randrange(0,res, size)
apple = randrange(0,res, size), randrange(0, res, size)

dirs = {'W': True,'S': True,'A': True,'D': True}

lenght = 1
snake = [(x,y)]
score = 0
dx,dy = 0,0

fps = 5
                   

pygame.init()
sc = pygame.display.set_mode([res,res])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial',26, bold = True)
font_end = pygame.font.SysFont('Arial',66, bold = True)

while True:    
    sc.fill(pygame.Color('black'))
    [(pygame.draw.rect(sc,pygame.Color('green'),( i , j , size - 2 , size- 2))) for i ,j in snake]
    pygame.draw.rect(sc,pygame.Color('red'),(*apple,size,size))

    render_score = font_score.render(f'SCORE: {score}',1, pygame.Color('blue'))
    sc.blit(render_score,(5,5))

    x += dx * size
    y += dy * size
    snake.append((x,y))
    snake = snake[-lenght:]

    if snake[-1] == apple:
        apple = randrange(0,res,size),randrange(0,res,size)
        lenght += 1
        score+=1
        if lenght % 5 == 0:
            fps+= 3   
    if x < 0 or x > res - size or y < 0 or y > res - size or  len(snake) != len(set(snake)) :
        while True:
            render_end = font_end.render('GAME OVER',1,pygame.Color('blue'))
            sc.blit(render_end,(res // 2 -200, res//3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx,dy = 0,-1
        dirs = {'W': True,'S': False,'A': True,'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx,dy = 0,1
        dirs = {'W': False,'S': True,'A': True,'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx,dy = -1, 0
        dirs = {'W': True,'S': True,'A': True,'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx,dy = 1,0
        dirs = {'W': True,'S': True,'A': False,'D': True}