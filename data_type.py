print(2 > 3 or 3 < 5) #둘 중에 하나라도 참이면 참
print(2 > 3 and 3 < 5) #둘 다 참이여야 참

print('abcd\nefg') #\n은 줄바꿈

print('''
abcd
efgh
ijk
''') #문자열을 이렇게 print도 가능

print(len('abcdef')) #문자열만 len함수 사용 가능

name = 'swplay'
name1 = 'SWPLAY'
var1 = '재미있는 파이썬공부'
print(name.upper()) #문자열 모두 대문자로 바꾸기
print(name1.lower()) #문자열 모두 소문자로 바꾸기
print(var1.replace('공부', 'study')) #replace(삭제하고 싶은 것, 그 삭제한 자리에 넣고 싶은 것)

a = 10 
b = int('10') #형변환을 해 줘야 둘끼리 연산이 됨.
print(a + b)

a = 10
b = '10'
print(a + int(b)) # 마지막에 형변환

a = str(10) #형변환
b = '10'
print(a + b)

a = 10
b = '10'
print(str(a) + b) #마지막에 형변환

em = [] #대괄호 이용해 리스트 만들기
print(em)

em = list() #List Fuction 이용해 리스트 만들기
print(em)

color = ['red', 'blue', 'black', 'white'] #리스트의 기본 형식(mutable)
print(type(color))
color[0] = 'yellow' #재설정 형식(인덱스 이용)
print(color)

h_list = list('hope') #문자열을 리스트화 시키면?
print(h_list) #글자 하나하나 쪼개져서 리스트로 들어간다.
print(h_list[3]) #인덱싱도 가능하다.

m = ('a', 'b', 'c') #튜플의 기본 형식(unmutable)
print(type(m))

n = list(m) #튜플의 리스트화
print(type(n))
print(n[0])

day = '2020-09-05'
day_list = day.split('-') #리스트화 시키는 동시에 괄호 안의 것으로 리스트 요소를 구분시킴.
print(day_list)

li = ['a', 'b', 'c', 'd', 'e']
print(li[0:2]) #a부터 c까지일 것 같지만 a부터 b까지이다. start부터 end -1까지 출력한다.
print(li[:]) #처음과 끝이 없으므로 전체이다.
print(li[0:4:2]) #a부터 d까지인데, 한 칸식 건너뛰어서 출력
print(li[0:4:-2]) #a부터 d까지인데, 한 칸식 역으로 건너뛰어서 출력
print(li[::2]) #첨부터 끝까지 중에 한 칸씩 건너뛰어서 출력
print(li[::-2]) #첨부터 끝까지 중에 한 칸씩 역으로 건너뛰어서 출력


