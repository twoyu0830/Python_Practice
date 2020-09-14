#1. 오늘 날짜 중 연도만 출력하시오.
from datetime import *
d = date.today()
print(d.year) #각각 쪼개서 출력도 가능
print(d.month)
print(d.day)

#2. 오늘 날짜와 2일을 출력하시오.
from datetime import *
d = date.today()
t = timedelta(days = 2) #특정 날짜에서 특정 일수를 더하면 무슨 날짜가 되는지 알고 싶을 때 사용
print(d + t)  

#3. 2021년 1월 1일까지는 몇 일 남았는지 쓰시오.
from datetime import *
d = date.today()
s = date(2021, 1, 1)
print(s - d) #몇 일 남았는지 계산 가능

#4. 시간을 설정하고 출력하시오.
from datetime import *
print(time(19, 42, 13))

#5. 시간을 설정하고 시, 분, 초를 출력하시오.
from datetime import *
d = time(19, 42, 13))
print(d.hour)
print(d.minute)
print(d.second)

#6. 날짜와 시간을 설정하고 출력해보세요.
from datetime import *
d = datetime(2020, 9, 13, 19, 46, 23)
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)

#7. 함수를 이용하여 단을 입력받아 해당 단의 구구단을 출력하는 프로그램을 작성하시오.
def gugudan(): #1)인자 없어도 된다. 껍대기만 함수
    dan = int(input('단을 입력하세요.'))
    for i in range(1, 10):
        print(dan, '*', i, '=', dan * i )
print(gugudan())

def gugudan(dan): #2)메인에서 입력받기
    for i in range(1, 10):
        print(dan, '*', i, '=', dan * i )
dan = int(input('단을 입력하세요.'))
print(gugudan(dan))

#8. 두 수를 입력 받아 두 수 사이의 수들의 합을 구하시오.(함수 사용)
def my_fun(start, end):
    sum=0
    for i in range(start, end + 1):
        sum = sum + i
    print ('합계', sum)
start = int(input('시작 값 : '))
end= int(input('끝 값 : '))
print(my_fun(start, end))

#9. 입력한 숫자만큼 별을 출력하시오.
def my_fun(start):
    return '*' * start 
start = int(input('별의 수: '))
print(my_fun(start))


#10. 두 수를 입력받아 큰 수를 출력하시오.
def comparison(f, s):
    if f > s:
        return f
    elif f == s:
        return 'Same'
    else:
        return s
f = int(input('f 값: '))
s = int(input('s 값: '))
print(comparison(f, s))

#11. 세 수를 입력받아 가장 큰 값을 출력하시오.
def big(f, s, t):
    if f > s and f > t:
        return f
    elif s > f and s > t:
        return s
    elif t > f and t > s:
        return t
    else:
        return 'none'
f = int(input('값을 입력하시오. '))
s = int(input('값을 입력하시오. '))
t = int(input('값을 입력하시오. '))
print(big(f, s, t))
