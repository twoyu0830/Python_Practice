def add(): #무반환형 함수, 언제든 호출만하면 그 함수 내에서 다 수행하고 정해진 결과 내보냄.
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
    return a + b #print대신 return 넣으면 함수밖에서 print써도 none 안 나옴.
print(add1(70, 80))

def add1(a, b): #실제 함수 활용 예시
    return a + b
c = add1(70, 80)
print(c * 1.1)

from calc import * #모듈 호출방식
c = add(70, 80) #모듈 호출해서 함수 사용하는 방법
d = sub(70, 80)
print(c, d)





