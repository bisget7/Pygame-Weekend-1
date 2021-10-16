import pygame
import sys
import random


pygame.init()
screen_size=(800, 600)
width=screen_size[0]
height=screen_size[1]
screen = pygame.display.set_mode(screen_size)
Backgroud_colour=(0, 0, 0)
player_colour=(255, 0, 0)
player_size=[50, 50]
enemy_size=[50, 50]
enemy_colour=(random.randint(0, 255), random.randint(0, 255),random.randint(0, 255))
enemy_positions=[[random.randint(0, width - enemy_size[0]), enemy_size[0]]]
player_position=[width/2, height-2*player_size[1]]
enemy_speed=10
FPS=20
SCORE=0
clock=pygame.time.Clock()

myfont=pygame.font.SysFont("monospace", 35)

def set_level(SCORE):
    SPEED= SCORE/5  + 5
    return SPEED

def detect_collision(player_position, enemy_posititions):
    p_x=player_position[0]
    p_y=player_position[1]
    for enemy_position in enemy_positions:
        e_x=enemy_position[0]
        e_y=enemy_position[1]
        if (p_x > e_x and p_x <= e_x+enemy_size[0]) or (e_x >p_x and e_x <= p_x + player_size[0]):
            if (p_y > e_y and p_y <= e_y+enemy_size[1]) or (e_y > p_y and e_y <= p_y + player_size[1]):
                return True
    return False

def update_enemies(enemy_positions):
    if len(enemy_positions)<10:
        y=random.random()
        if y>0.8:
            enem_x=random.randint(0, width - enemy_size[0])
            enem_y=enemy_size[0]
            enemy_positions.append([enem_x, enem_y])


def draw_enemies(enemy_positions, enemy_size):
    for enemy_position in enemy_positions:
        pygame.draw.rect(screen, enemy_colour, (enemy_position[0], enemy_position[1], enemy_size[0], enemy_size[1]))
def drop_enemies(enemy_positions, SCORE):
    for inde, enemy_position in enumerate(enemy_positions):
        if enemy_position[1] > 0 and enemy_position[1] <= height:
            enemy_position[1]+=enemy_speed+random.randint(0, 5)
        else:
            SCORE=SCORE+1
            x=random.random()
            if x > 0.5:
                enemy_position[1]=enemy_size[0]
                enemy_position[0]=random.randint(0, width- enemy_size[0])
            else:
                enemy_positions.pop(inde)
    return SCORE
     

game_over =False

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            x=player_position[0]
            y=player_position[1]
            if event.key==pygame.K_LEFT:
                x-=player_size[0]/2
            elif event.key==pygame.K_RIGHT:
                x+=player_size[0]/2
            player_position=[x, y]
    screen.fill(Backgroud_colour)

    if detect_collision(player_position, enemy_positions):
        game_over = True
        break
    enemy_speed=set_level(SCORE)
    update_enemies(enemy_positions)
    SCORE=drop_enemies(enemy_positions, SCORE)
    pygame.draw.rect(screen, player_colour, (player_position[0], player_position[1], player_size[0], player_size[1]))
    draw_enemies(enemy_positions, enemy_size)
    print(SCORE)
    text="SCORE: " + str(SCORE)
    label=myfont.render(text, 2, (255, 255, 0))
    screen.blit(label, (width-200, height-40))

    clock.tick(FPS)
    pygame.display.update()
print(SCORE)