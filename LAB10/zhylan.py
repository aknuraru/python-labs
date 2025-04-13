import pygame
import random
import psycopg2
pygame.init()
#color
WHITE = (255,255,255)
RED = (255,0,0)
DARK_GREEN = (17,119,44)
GREEN = (0,255,0)
BLACK = (0,0,0)
YELLOW =(255, 191, 0)
#clock
clock = pygame.time.Clock()
FPS = 10
big_food = 10*FPS+1  # my time it is just cnt by FPS  10*FPS=10s
#screen
l, w = 1001, 601
screen = pygame.display.set_mode((l,w))
running = True
x_axis, y_axis = 0, 0
radius = 10
body = [[10, 10]]
snake_len=1
wall = []
wall_len = 0
kill_condition = False
last_key = str("")
#value
level_value = 1
score_value = 0
record = 0
#fonts
font = pygame.font.SysFont("comicsansms", 24)
font_Gameover = pygame.font.SysFont("comicsansms", 72)
text4 = font.render("YOU LOSE", True, BLACK)
#cordinate randomiser
def random_c():
    x_value = random.randrange(10, l-10)
    y_value = random.randrange(10, w-10)
    x1, y1 = 10 * round(x_value / 10), 10 * round(y_value /10)
    condition = True
    for i in range(len(body)):
        if body[i][0]==x1 and body[i][1] == y1:
            condition = False
            break
    if level_value == 1:
        for i in range(100,400):
            if x1 == 300 and y1 == i:
                condition = False
                break
    if condition == True:
        return x1, y1
    else:
        x1, y1 = random_c()
        return x1, y1
food_x, food_y = random_c()
BIG_FOOD_X, BIG_FOOD_Y = random_c()
def kill_yourself():
    global kill_condition
    for i in range(1,len(body)):
        if body[0][0] == body[i][0] and body[0][1] == body[i][1]:
            kill_condition = True
            break
    return kill_condition   
def tall_wall_kill():
    global kill_condition
    #Horizontal
    for i in range(100, 401):
        if body[0][0] == i and body[0][1] == 300:
            kill_condition = True
            break
    #Vertical
    if body[0][0] == 600 and 300 <= body[0][1] <= 500:
        kill_condition = True
    #Horizontal
    if 400 <= body[0][0] <= 700 and body[0][1] == 100:
        kill_condition = True
    return kill_condition
def wall_kill():  
    global kill_condition
    for i in range(len(wall)):
        if body[0][0] == wall[i][0] and body[0][1] == wall[i][1]:
            kill_condition = True
            break
    return kill_condition
#SQL
conn = psycopg2.connect(
	database="postgres",
	user='postgres',
	password='2007',
	host='localhost',
	port= '5432'
)
con = conn.cursor()
conn.autocommit = True
login_name = str(input('Enter your login: '))
sql = f"select * from snakedata where user_login =\'{login_name}\'"
con.execute(sql)
info = con.fetchall()
if len(info) > 0:
    print("Found an existing account, loading your data")
    score_value = info[0][1]
    level_value = info[0][2]
    FPS = info[0][3]
    snake_len = int(info[0][4])
    wall_len = int(info[0][5])
    body[0][0] = int(info[0][6])
    body[0][1] = int(info[0][7])
    x_axis = -10
    record = info[0][8]
    for i in range(1,snake_len):
        body.append([-i*200,-i*200])
    for j in range(wall_len):
        food_x2, food_y2 = random_c()
        wall.append([food_x2, food_y2])
    print(body)
else:
    print("this User isn't registered, So we created a new account")
    sql_insert = f"INSERT INTO snakedata(user_login, last_score, last_level, last_FPS, snake_len, wall_len, snake_x, snake_y, record) VALUES( \'{login_name}\',\'{score_value}\',\'{level_value}\',\'{FPS}\', \'{snake_len}\', \'{wall_len}\',\'{body[0][0]}\', \'{body[0][1]}\', \'{record}\' )"
    con.execute(sql_insert)
def game_over():
    global running
    global sql_insert1
    global score_value
    global record
    screen.fill(RED)
    screen.blit(text1, (850,5))
    screen.blit(text2, (850,35))
    screen.blit(text3, (850,65))
    screen.blit(text4, (425,225))
    sql_insert1 = f"UPDATE snakedata set  last_score = 0, last_level = 1, last_FPS = 10, snake_len = 1, wall_len = 0, snake_x=10, snake_y=10  where user_login = \'{login_name}\' "
    con.execute(sql_insert1)
    if score_value > record:
        sql_insert1 = f"UPDATE snakedata set record = \'{score_value}\'  where user_login = \'{login_name}\' "
        record = score_value
        con.execute(sql_insert1)
#main
while running:
    wall_len = len(wall)
    snake_len=len(body)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and last_key!="K_LEFT":
                x_axis = 10
                y_axis = 0
                last_key = "K_RIGHT"
            if event.key == pygame.K_LEFT and last_key!="K_RIGHT":
                x_axis = -10
                y_axis = 0
                last_key = "K_LEFT"
            if event.key == pygame.K_UP and last_key!="K_DOWN":
                x_axis = 0
                y_axis = -10
                last_key = "K_UP"
            if event.key == pygame.K_DOWN and last_key!="K_UP":
                x_axis = 0
                y_axis = 10
                last_key = "K_DOWN"
            if event.key == pygame.K_ESCAPE:
                print("PAUSE")
                sql_insert = f"UPDATE snakedata set last_score =\'{score_value}\',last_level =\'{level_value}\',last_FPS =\'{FPS}\',snake_len=\'{snake_len}\',wall_len=\'{wall_len}\', snake_x=\'{body[0][0]}\', snake_y=\'{body[0][1]}\', record = \'{record}\' where user_login = \'{login_name}\'; "
                con.execute(sql_insert)
                running = False                     
    #value 
    text1 = font.render("Score: "+str(score_value), True, WHITE)
    text2 = font.render("Level: "+str(level_value), True, WHITE)
    text3 = font.render("FPS: "+str(FPS), True, WHITE)
    text5 = font.render("Record: "+str(record), True, WHITE)
    #eating
    if body[0][0]==food_x and body[0][1]==food_y:
        food_x, food_y = random_c()
        body.append([0, 0])
        score_value += 10
        big_food = 10*FPS +1
    #eating BIF FOOD
    elif body[0][0]==BIG_FOOD_X and body[0][1]== BIG_FOOD_Y:
        body.append([0, 0])
        score_value += 30
        big_food = 10*FPS+1
    #level
    last_level = level_value
    level_value = 1 + score_value //50
    #body change
    for i in range(len(body) - 1, 0, -1):
        body[i][0] = body[i - 1][0]
        body[i][1] = body[i - 1][1]
    #return to screen
    if body[0][0] > l-11:
        body[0][0] = 10
    if body[0][1] > w-11:
        body[0][1] = 10
    if body[0][1] < 10:
        body[0][1] = w-11
    if body[0][0] < 10:
        body[0][0] = l-11
    #body coordination
    body[0][0] += x_axis
    body[0][1] += y_axis
    # main screen     
    screen.fill(BLACK)
    # Draw score level FPS
    screen.blit(text1, (850,5))
    screen.blit(text2, (850,35))
    screen.blit(text3, (850,65))
    screen.blit(text5, (850,95))
    # Draw food
    pygame.draw.circle(screen, WHITE, (food_x, food_y), radius-5)

    if big_food == 0:
        BIG_FOOD_X, BIG_FOOD_Y = random_c()

    if big_food <= 10*FPS:
        pygame.draw.circle(screen, YELLOW, (BIG_FOOD_X, BIG_FOOD_Y), radius)
        big_food += 1

    if big_food > 10*FPS:
        BIG_FOOD_X, BIG_FOOD_Y = -100, -100
    # Draw snake body
    for i, (x, y) in enumerate(body):
        if i!=0:
            pygame.draw.circle(screen, GREEN, (x, y), radius)
    # Draw snake head
    pygame.draw.circle(screen, DARK_GREEN, (body[0][0], body[0][1]), radius)
    # level 1
    if level_value == 1:
        pygame.draw.line(screen, RED, (100, 300), (400, 300), 10) #Horizontal
        pygame.draw.line(screen, RED, (600, 500), (600, 300), 10) #Vertical
        pygame.draw.line(screen, RED, (400, 100), (700, 100), 10) #Horizontal2
        if tall_wall_kill():
            print("You hit a tall wall!")
            game_over()

    # add wall circle & add FPS next level
    if last_level != level_value:
        FPS += 3
        food_x2, food_y2 = random_c()
        wall.append([food_x2, food_y2])
        big_food = 0

    if level_value > 1:
        for i in range(len(wall)):
            pygame.draw.circle(screen, RED, (wall[i][0], wall[i][1]), radius-5)
        if wall_kill()== True:
            print("You hit a small wall!")
            game_over()
    
    # Kill yourself
    if kill_yourself()==True:
        print("You died.")
        game_over
    pygame.display.flip()
    clock.tick(FPS)
conn.commit()
pygame.quit()