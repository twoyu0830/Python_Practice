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
black = (0, 0, 0)

class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 0
    def put_img(self, address):
        if address[-3:] == 'png':
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)
            self.sx, self.sy = self.img.get_size()
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()
    def show(self):
        screen.blit(self.img, (self.x, self.y))

ss = obj()
ss.put_img('C:/Users/ygyg0/Google 드라이브/배움/python_practice/ss.png')
ss.change_size(50, 80)
ss.x = round(size[0] / 2 - ss.sx / 2)
ss.y = size[1] - ss.sy - 10
ss.move = 5


left_go = False
right_go = False
space_go = False
# 4. 메인 이벤트
SB = 0
while SB == 0:
    
    # 4-1. FPS 설정
    clock.tick(60)
 
    # 4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_go = True
            elif event.key == pygame.K_RIGHT:
                right_go = True
            elif event.key == pygame.K_SPACE:
                space_go = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_go = False
            elif event.key == pygame.K_RIGHT:
                right_go = False
            elif event.key == pygame.K_SPACE:
                space_go = False

 
 
    # 4-3. 입력, 시간에 따른 변화
    if left_go == True:
        ss.x -= ss.move
        if ss.x <= 0:
            ss.x = 0
    elif right_go == True:
        ss.x += ss.move
        if ss.x >= size[0] - ss.sx:
            ss.x = size[0] - ss.sx
    
    m_list = []
    if space_go == True:
        mm = obj()
        mm.put_img('C:/Users/ygyg0/Google 드라이브/배움/python_practice/mm.png')
        mm.change_size(5, 15)
        mm.x = round(ss.x + ss.sx / 2 - mm.sx / 2)
        mm.y = ss.y - mm.sy - 15
        mm.move = 15
        m_list.append(mm)
    
    d_list = []
    for i in range(len(m_list)):
        m = m_list[i]
        mm.y -= mm.move
        if mm.y <= -mm.sy:
            d_list.append(i)
    for d in d_list:
        del m_list[d]





    # 4-4. 그리기
    screen.fill(black)
    ss.show()
    for m in m_list:
        m.show()
  
    
 
    # 4-5 업데이트
    pygame.display.flip()

# 5. 게임 종료
pygame.quit()