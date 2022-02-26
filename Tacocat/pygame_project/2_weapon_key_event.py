##make pygame basic(뼈대)
import pygame
import random
import os
from pygame.time import get_ticks

# 초기화 
pygame.init()

# 화면 크기 설정
screen_width  = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption('Nado Pang')

# FPS
clock = pygame.time.Clock()

#1. 사용자 게임 초기화(배경화면, 등등)
current_path = os.path.dirname(__file__) # 현재파일의 위치를 반환
image_path = os.path.join(current_path, "images") #image폴더 위치 반환

#1.1 배경만들기
background = pygame.image.load(os.path.join(image_path, "paperBackground.jpg"))

#2. 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.jpg"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지 높이를 계산해서 공을 튕기는 것 조절하기 위해 

#3. 캐릭터 만들기
charcater = pygame.image.load(os.path.join(image_path, "character.jpg"))
charcater_size = charcater.get_rect().size
charcater_height = charcater_size[1]
character_width = charcater_size[0]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - stage_height - charcater_height

# 4. 캐릭터 이동방향과 이동 속도 만들기
character_to_x = 0
character_speed = 5

# 8. 무기만들기 - 한번에 여러번 발사 가능하도록 
weapon = pygame.image.load(os.path.join(image_path, "weapon.jpg"))
weapon_x_pos = 0
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapons = []

# 8.1 무기속도 정의하기, 
weapon_speed = 10

flag = True
while flag:
    delta = clock.tick(100)

     #사용자의 이벤트를 체크하는 것
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             # 창을 끄는 버튼을 누르면 해당 이벤트가 발생
            flag = False
            # 5. 이벤트 처리 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif  event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: # 무기발사
                weapon_x_pos = character_x_pos + character_width / 2 - weapon_width/2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0 
            
    # 6. 게임 캐릭터의 위치 정의
    character_x_pos += character_to_x

    #7. 경계값 처리 
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

    #9. 무기위치조정
    # w[0] - width, w[1] - height, 높이를 계속 줄임 
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    #10. 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # 2. 배경화면 그리기
    screen.blit(background, (0,0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(charcater, (character_x_pos, character_y_pos))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    pygame.display.update()

# 게임 종료 시 처리 
pygame.quit()

