k = int(input("구분? 1. 주간, 2. 야간")) #중첩 if문(경우의 수)
m = int(input("대상? 1. 대인, 2. 소인"))
if k == 1:
    if m == 1:
        fee = 40000
    else:
        fee = 30000
else:
    if m == 1:
        fee = 30000
    else:
        fee = 20000
print(fee)


c = 1
while c <= 10: #이 문장을 만족 시킬 경우에만 아래 문장 실행(단지 if + 범위), 보통 정확한 횟수 모를 때 while문 사용함
    print(c)
    c += 1 #while문에서는 보통 이게 들어감.

while True: #무조건 만족시키는 무한루프 만들기(유효성 판단할 때)
    score = int(input('Enter your score.'))
    if score >= 0 and score <= 100: #목표하는 조건들
        break #위의 목표하는 조건들을 만족시켰을 때만 더 이상 물어보지 않는다(무한루프 종료)
print(score)

while True:
    digits = input('Enter.')
    if len(digits) == 4: #자릿수가 4자리일 때가 목표하는 조건들
        break #목표하는 조건들 만족시켰을 때 더 이상 물어보지 않음.
print(digits)

print(list(range(5))) #range 안의 내용은 리스트의 슬라이싱과 비슷하다. but range(5) != [5]
print(list(range(1, 5)))
print(list(range(1, 5, 2)))

for i in range(1, 10):
    print('3 * ' + str(i) + '=' + str(3 * i)) #구구단 계산

for i in range(5): #중첩 for문(많은 반복 구현할 때), i가 1일 때 밑의 for문과 print 수행, i가 2일 때 밑의 for문과 print 수행......반복
    for k in range(5):
        print(k)
    
for i in range(7): #'*'이 아래로 49번 찍히는 것이어서 보기 힘듦
    for k in range(7):
        print('*')

for i in range(7):
    for k in range(7):
        print('*', end = '') #'*'이 옆으로 써짐
    print() #줄바꿈 역할 자동으로
        
for i in range(1, 10): #구구단
    for k in range(1, 10):
        print(str(i) + '*' + str(k) + '=' + str(i * k))

star = '*' #for과 while형식 짬뽕시켜 만든 별탑
for i in range(5): # *
    print(star)    # **
    star += '*'    # ***
                   # ****
                   # *****
for i in range(5): #중첩 for문 이용 별탑
    for k in range(i + 1):
        print('*', end = '')
    print()

for i in range(1, 6): #간단한 for문 이용 별탑
    print('*' * i)

star = '*' #while문 이용 별탑
while len(star) <= 5:
    print(star)
    star += '*'

for i in range(1, 6): #별탑 위아래 뒤집기
    for k in range(1, 7 - i):
        print('*', end = '')
    print()

for i in range(5, 0, -1): #간단한 별탑 위아래 뒤집기
    print('*' * i)


 for i in range(1, 6): #별탑 좌우로 뒤집기
     for k in range(1, 6 - i):
         print(' ', end = '') 
     for j in range(1, 1 + i ):
         print('*', end = '')
     print()

for i in range(5, 0, -1): #간단한 별탑 좌우로 뒤집기
    print(' ' * (i - 1), '*' * (6 - i))
 
 for i in range(1, 5): #1357별탑
     for k in range(1, 5 - i):
         print(' ', end = '')
     for j in range(1, i * 2 ):
         print('*', end = '')
     for u in range(1, 5 - i):
         print(' ', end = '')
     print()

 for i in range(1, 5): #간단한 1357별탑
     print(' ' * (4 - i), '*' * (i * 2 -1))


for i in range(1, 6): #1,12, 123, 1234, 12345탑
    for k in range(1, 1 + i):
        print(k , end = '')
    print()

for i in range(1, 6): #1,22, 333, 4444, 55555탑
    for k in range(1, 1 + i):
        print(i, end = '')
    print()

for i in range(1, 6):
    print(i * )
        
 
 
