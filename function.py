def add(): #함수 안에 return이 없는 무반환형 함수, print 안 붙이고 호출만하면 그 함수 내에서 다 수행하고 정해진 결과(print의 결과) 내보냄
    a = 7
    b = 8
    print(a + b)
add()
add()
add()

def add1(a, b): #인자들을 넣으면 자기가 원하는 수로 계산 가능
    print(a + b)
add1(70, 80)

def add1(a, b):
    return a + b #print대신 return 넣으면 add1(70, 80)와 return 값이 같아짐. 그것을 print하면 none이 출력이 안 되고 이쁘게 나옴
print(add1(70, 80))

from calc import * #모듈 호출방식
c = add(70, 80) #모듈 호출해서 함수 사용하는 방법
d = sub(70, 80)
print(c, d)

from datetime import * #파이썬 내장 모듈 이용
d = date(2020, 9, 13) ####날짜 보여주는 클래스
print(d)

from datetime import * 
d = date(2020, 9, 13) 
print(d.weekday()) #요일을 숫자로 출력해주는 함수(월요일 = 0, 일요일 = 6)

from datetime import * #weekday함수 실사용 예시
d = date(2020, 9, 13)
y = {0: '월', 1: '화', 2: '수', 3: '목', 4: '금', 5: '토', 6: '일'}
print('{}요일입니다^^'.format(y[d.weekday()]))

from datetime import * 
d = date.today() #현재날짜 보여주는 함수
print(d)

from datetime import * 
d = datetime(2020, 9, 13, 19, 2, 20) ####날짜와 시간까지 보여주는 클래스
print(d)

from datetime import * 
d = datetime.now() #현재날짜와 시간 보여주는 함수
print(d)

from datetime import * 
d = time(19, 2, 20) ####시간만 보여주는 클래스
print(d)

from random import * #파이썬 내장 모듈
li = choice(range(1, 46) #한 개 선택해주는 함수(choice(뽑을 것들))
print(li)

from random import * #파이썬 내장 모듈
family = ['윤규', '윤지', '도희', '정환'] 
li = choice(family) #한 개 선택해주는 함수(choice(뽑을 것들))
print(li)

from random import * #파이썬 내장 모듈
li = sample(range(1, 46), 6) #순서 없이 무작위로 몇 개 선택해주는 함수(sample(뽑을 것들, 뽑을 개수))
print(li)

from random import * #파이썬 내장 모듈
family = ['윤규', '윤지', '도희', '정환']
li = sample(family, 1) #순서 없이 무작위로 몇 개 선택해주는 함수(sample(뽑을 것들, 뽑을 개수))
print(li)

from random import * #파이썬 내장 모듈
li = sample(range(1, 6), 5) #뽑을 것들 수와 뽑을 개수 같게 해주면 순서 정할 때 사용할 수 있다.
print(li)




def menu(w1, w2, w3):
    return {'red': w1, 'yellow': w2, 'blue': w3} #함수가 딕셔너리형을 리턴할 수도 있다.
print((menu('빨강', '노랑', '파랑'))

def menu(ar, result=[]): #디폴트 매개변수(함수 호출할 때 명시한 게 없으면 이게 기본값으로 들어감)
    result.append(ar)
    return result
print(menu('a'))
print(menu('b')) #둘이 디폴트 매개변수를 공유함

def menu(ar, result = 7): #디폴트 매개변수(함수 호출할 때 명시한 게 없으면 이게 기본값으로 들어감)
    return result
print(menu('a'))
print(menu('b', 5))

def menu(*text): #튜플 가변 매개변수
    result = ''
    for s in text:
        result += s
    return result
print((menu('a', 'b', 'c', 'd'))

def menu(*text): #튜플을 받아주는 가변 매개변수
    result = 0
    for i in text:
        result += i
    return result
print(menu(1, 2, 3, 4))

def menu(**text): #딕셔너리를 받아주는 가변 매개변수
    for i in text.keys():
        print('{0} = {1}'.format(i, text[i]))
menu(kor = 90, eng = 80, mat = 70)

def menu(**text): #딕셔너리를 받아주는 가변 매개변수
    tot = 0
    for i in text.keys():
        print('{0} = {1}'.format(i, text[i]))
        tot += text[i]
    print(tot)
menu(kor = 90, eng = 80, mat = 70)

















