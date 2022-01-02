##make pygame basic(뼈대)
import pygame

pygame.init() 

# 화면 크기 설정

screen_width = 480 
screen_height = 640 
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption('Nado Game')

background = pygame.image.load('/Users/joy/Projects/python_Exercise/Python/Tacocat/pygame_basic/background.jpg')

# 동작검사하는 이벤트 루프가 실행되어야 창이 꺼지지 않음 
running = True
while running:
    for event in pygame.event.get():
        #사용자의 이벤트를 체크하는 것
        if event.type == pygame.QUIT: 
            # 창을 끄는 버튼을 누르면 해당 이벤트가 발생
            running = False 

    # fill, 과 blit의 순서 바뀌면 fill만 보여짐. 당연한 듯        
    screen.fill((0, 0, 255))
    screen.blit(background, (20, 0))
    ## while 문에서 계속 프레임을 그려주어야함 
    pygame.display.update()

# 게임 종료 시 처리 
pygame.quit()

# 배경 넣기 

