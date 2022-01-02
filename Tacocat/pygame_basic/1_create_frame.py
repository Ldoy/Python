import pygame
##make pygame basic(뼈대)

pygame.init() 

# 화면 크기 설정

screen_width = 480 
screen_height = 640 
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption('Nado Game')

# 동작검사하는 이벤트 루프가 실행되어야 창이 꺼지지 않음 
running = True
while running:
    for event in pygame.event.get():
        #사용자의 이벤트를 체크하는 것
        if event.type == pygame.QUIT: 
            # 창을 끄는 버튼을 누르면 해당 이벤트가 발생
            running = False 


# 게임 종료 시 처리 
pygame.quit()
