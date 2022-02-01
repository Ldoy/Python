##make pygame basic(뼈대)
import pygame
import random
from pygame.time import get_ticks

# 초기화 
pygame.init()

# 화면 크기 설정
screen_width  = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption('Basic Game')

# 백그라운드 이미지 불러오기 
background = pygame.image.load('/Users/joy/Projects/python_Exercise/Python/Tacocat/pygame_basic/7_quiz_images/paperBackground.jpg')

# 캐릭터 불러오기 
## 캐릭터 이미지 로드, 캐릭터 사이즈 정하기 
## get_rect().size -> 배열로 가로, 세로반환 
charater_image = pygame.image.load('/Users/joy/Projects/python_Exercise/Python/Tacocat/pygame_basic/7_quiz_images/dog.png')

charater_size = charater_image.get_rect().size
character_width = charater_size[0]
charater_height = charater_size[1]

## 캐릭터의 위치 정하기 가로,세로 모두 
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - charater_height

## 캐릭터가 이동할 좌표
to_x = 0
to_y = 0

# 6. collision
## enemy
enemy_image = pygame.image.load('/Users/joy/Projects/python_Exercise/Python/Tacocat/pygame_basic/7_quiz_images/poo.jpg')
enemy_size = enemy_image.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (character_width / 2)
enemy_y_pos = screen_height / 2

#5. FPS
clock = pygame.time.Clock()
character_speed = 0.6
# 동작검사하는 이벤트 루프가 실행되어야 창이 꺼지지 않음 
flag = True
poo_speed = 3
while flag:
    delta = clock.tick(100)
   # print("fps: " + str(delta.get_ticks()))

     #사용자의 이벤트를 체크하는 것
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             # 창을 끄는 버튼을 누르면 해당 이벤트가 발생
            flag = False
        
        if event.type == pygame.KEYDOWN:
            # 해당 경우에 캐릭터의 좌표를 바꿔주기 
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                ## 1. 위 아래 움직이지 않도록 함 
                to_y -= 0      
            elif event.key == pygame.K_DOWN: 
                to_y += 0
        # 키를 떼면 멈춰야하기 때문에 추가할 값 자체를 0으로 만듬 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    character_x_pos += to_x * delta
    character_y_pos += to_y * delta

    #border밖으로 안나가게 하기 
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height -  charater_height:
        character_y_pos = screen_height - charater_height

    character_rect = charater_image.get_rect()
    # print('1️⃣' + str(character_rect))
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    # print('2️⃣' + str(character_rect)) # 업데이트해줌 

    enemy_rect = enemy_image.get_rect()
    # print('3️⃣' + str(enemy_rect))
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    # print('4️⃣' + str(enemy_rect))

    if character_rect.colliderect(enemy_rect):
        flag = False
    else:
        enemy_y_pos += poo_speed
        if enemy_y_pos > screen_height:
            enemy_y_pos = 0
            enemy_x_pos = random.randrange(1, 480)
            

    # fill, 과 blit의 순서 바뀌면 fill만 보여짐. 당연한 듯      
    screen.blit(background, (0,0))
    screen.blit(charater_image, (character_x_pos, character_y_pos))

    screen.blit(enemy_image, (enemy_x_pos, enemy_y_pos))
    # while 문에서 계속 프레임을 그려주어야함 
    pygame.display.update()

# 게임 종료 시 처리 
pygame.quit()

# 1.위, 아래 이동 막기 
# 2. 캐릭터와 적이미지 바꾸기 
# 3. 똥이 아래로 내려오도록 하기 - 프레임마다 일정 속도로 내려오도록 하면 될 듯
# 4. 똥과 부딪혔을 때 게임 종료되도록 하기  