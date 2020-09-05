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





