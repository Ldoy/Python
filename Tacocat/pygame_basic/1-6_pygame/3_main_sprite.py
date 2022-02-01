##make pygame basic(뼈대)
import pygame
from pygame import image
from pygame.constants import QUIT

# 초기화 
pygame.init()

# 화면 크기 설정
screen_width  = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption('Basic Game')

# 백그라운드 이미지 불러오기 
background = pygame.image.load('/Users/joy/Projects/python_Exercise/Python/Tacocat/pygame_basic/background.jpg')

# 캐릭터 불러오기 
## 캐릭터 이미지 로드, 캐릭터 사이즈 정하기 
## get_rect().size -> 배열로 가로, 세로반환 
charater_image = pygame.image.load('/Users/joy/Projects/python_Exercise/Python/Tacocat/pygame_basic/character.jpg')
charater_size = charater_image.get_rect().size
character_width = charater_size[0]
charater_height = charater_size[1]


## 캐릭터의 위치 정하기 가로,세로 모두 
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - charater_height


# 동작검사하는 이벤트 루프가 실행되어야 창이 꺼지지 않음 
flag = True
while flag:
     #사용자의 이벤트를 체크하는 것
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            # 창을 끄는 버튼을 누르면 해당 이벤트가 발생

    # fill, 과 blit의 순서 바뀌면 fill만 보여짐. 당연한 듯      
    screen.blit(background, (0,0))
    screen.blit(charater_image, (character_x_pos, character_y_pos))
    # while 문에서 계속 프레임을 그려주어야함 
    pygame.display.update()

# 게임 종료 시 처리 
pygame.quit()
