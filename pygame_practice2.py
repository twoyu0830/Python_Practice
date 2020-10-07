import pygame
# 1. 게임 초기화
pygame.init()

# 2. 게임창 옵션 설정
size = [400, 700]
screen = pygame.display.set_mode(size)

title = 'Shooting Game'
pygame.display.set_caption(title)

# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()
white = (255, 255, 255)

ss = pygame.image.load('C:/Users/ygyg0/Google 드라이브/배움/python_practice/ss.png').convert_alpha()
ss = pygame.transform.scale(ss, (50, 80))
ss_sx, ss_sy = ss.get_size()
ss_x = round(size[0] / 2 - ss_sx / 2)
ss_y = size[1] - ss_sy - 10
# 4. 메인 이벤트
SB = 0
while SB == 0:
    
    # 4-1. FPS 설정
    clock.tick(60)
 
    # 4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1
 
    # 4-3. 입력, 시간에 따른 변화
    

    # 4-4. 그리기
    screen.fill(white)
    screen.blit(ss, (ss_x, ss_y))
 
    # 4-5 업데이트
    pygame.display.flip()

# 5. 게임 종료
pygame.quit()