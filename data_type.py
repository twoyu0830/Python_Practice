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
print(li[4:0:-2]) #a부터 d까지인데, 한 칸식 역으로 건너뛰어서 출력
print(li[::2]) #첨부터 끝까지 중에 한 칸씩 건너뛰어서 출력
print(li[::-2]) #첨부터 끝까지 중에 한 칸씩 역으로 건너뛰어서 출력

li_ = 1
li.append(li_) #리스트에 단일요소 추가(끝에 들어감)
print(li)

li__ = [2, 3, 4]
li.append(li__) #리스트에 리스트 추가
print(li)

li1 = ['g', 'h']
li1.extend(li) #리스트 병합 방법1(주가 되는 것이 앞에)
print((li1))

li2 = ['i', 'j']
li1 += li2 #리스트 병합 방법2(주가 되는 것이 앞에)
print(li1)

li1.insert(2, 'x') #리스트 안의 원하는 위치에 요소 추가
print(li1)

del li1[0] #리스트 안의 요소 지우기(명령어 이용)
print(li1)

li1.remove('j') #리스트 안의 요소 지우기(함수 이용)
print(li1)

a = li1.pop(1) #pop함수(함수이지만 괄호 안에는 인덱스) 이용해 원하는 것 빼내고 그걸 다른 변수에 넣음.
print(li1, a)

print(li1.index('e')) #index함수 이용해 원하는 요소가 몇 번째 인덱스인지 확인

print('c' in li1) #해당 요소가 리스트에 있는지 확인

print(li1.count([2, 3, 4])) #해당 요소가  리스트에 몇 개 있는지 확인

li1.remove([2, 3, 4])
li1.remove(1)
print(li1)
print('-'.join(li1)) #리스트 요소들을 해당 문자가 사이에 오게 문자열로 합쳐버림(합치기 전에 리스트에서 int는 제거해야 함)

li1.sort() #리스트 요소들을 알파벳 순으로 정렬(이 때 할당을 안 해 줬으므로 li1자체가 아예 정렬이 돼서 바뀌어버리는 것이다.)
print(li1)

li1.sort(reverse = True) #알파벳 역순으로
print(li1)

li2 = ['a', 'c', 'd', 'r', 'h']
b = sorted(li2) #아예 li2자체를 바꾸지 않고, 할당을 해줘서 b가 정렬되고, 원본은 유지된다.
print(li2)
print(b)

li3 = li2 #같은 메모리 주소를 쓰겠다고 선언
li4 = ['j', 'n']
li2.extend(li4) #li2가 바뀌면? li3도 똑같이 바뀐다.(그리고 원본 li2는 그대로 사라져버린다.....)
print(li2)
print(li3) 

a = ['a', 'b', 'c']
b = a.copy() #이 세가지를 이용하면 '='사용할 때와 달리 원본 a의 내용은 b, c, d에 그대로 유지할 수 있다.
c = a[:]
d = list(a)
a.insert(0, 'change')
print(a)
print(b)
print(c)
print(d)







'''
튜플의 특징
1. 튜플은 작은 공간을 사용하므로 메모리 효율이 좋다.
2. 항목이 손상될 염려가 없다.(immutable)
3. 딕셔너리의 키로 사용할 수 있다.
4. 함수의 인자는 튜플로 전달된다.
'''

tu = () #소괄호 이용해 튜플 만들기              
print(tu)

tu = ('a') #요소 하나일 때는 아무리 소괄호 썼더라도 요소 뒤에 반점을 안 붙이면 튜플로 인식하지 않는다.
print(type(tu))

tu = ('a',) #괄호까지 붙여놔야 튜플로 인식
print(type(tu))

tu = 'a', 'b', 'c' #소괄호 안 붙여도 튜플로 인식하기는 한다.
print(type(tu))

tu = ('a', 'b', 'c')
tu1, tu2, tu3 = tu #튜플을 한번에 여러 변수에 할당(숫자 딱 맞춰야 함)
print(tu1, tu2, tu3)

a = 3
b = 5
a, b = b, a #스왑을 파이썬에서는 임시변수 t같은 것 없이도 구현 가능
print(a, b)

li = ['a', 'b', 'c', 'd']
print(tuple(li))
print(li)






___a = {} #딕셔너리
__a = set() #세트
print(type(__a))
print(type(___a))

a = {2, 3, 2, 1, 4, 3, 5, 2, 4, 5, 3, 3} #소괄호 이용해 세트 생성, 중복된 값들은 다 통합된다.
print(a) 

b = {2, 4, 6, 8} #세트는 순서가 없다.
print(b)

c = {'kor': 80, 'eng': 99, 'mat': 77}
d = set(c) #딕셔너리를 세트에 넣으면 키 값인 과목명들만 세트에 들어간다.
print(d)

e = {'경기도': {'수원', '고양', '용인', '성남'}, '경상도': {'부산', '울산', '대구', '경산'}} #value가 세트인 딕셔너리

a = {1, 2, 3}
b = {2, 3, 4}
print(a & b) #교집합
print(a | b) #합집합
print(a - b) #차집합
print(a ^ b) #대칭차집합(합집합 - 교집합)

sub = {'kor': 80, 'eng': 90, 'mat': 77}
print(sub['kor']) #딕셔너리의 특정 키의 값에 접근하는 방법

al = [['a', 'b'], ['c', 'd'], ['e', 'f']] #리스트 안의 요소들이 리스트(2차원)
print(dict(al)) #앞의 'a'가 키로, 'b'가 값으로 들어간다.

AL = (('a', 'b'), ('c', 'd'), ('e', 'f')) #튜플 안의 요소들이 튜플(2차원)
print(dict(AL)) #앞의 'a'가 키로, 'b'가 값으로 들어간다.

al_ = ['ab', 'bc', 'ca'] #문자열 리스트
print(dict(al_)) #각각의 문자열을 쪼개 각각 키, 값으로 들어감

sub = {'kor': 80, 'eng': 90, 'mat': 77}
sub['tot'] = 247 #딕셔너리에 새로운 값 추가(대괄호 사용하되, 인덱스는 사용X 키로 사용)
print(sub)

sub = {'kor': 80, 'eng': 90, 'mat': 77}
sub2 = {'kor2': 88, 'eng2': 99, 'mat2': 77}
sub2.update(sub) #딕셔너리 결합하기(주가 되는 것이 앞에)
print(sub2)

sub = {'kor': 80, 'eng': 90, 'mat': 77}
del sub['mat']
print(sub)

sub = {'kor': 80, 'eng': 90, 'mat': 77}
sub.clear() #딕셔너리 안의 모든 항목 삭제
print(sub)

sub = {'kor': 80, 'eng': 90, 'mat': 77}
print('kor' in sub) #딕셔너리 안의 항목 존재 여부 확인

sub = {'kor': 80, 'eng': 90, 'mat': 77}
sub.get('tot', 'XXX') #get함수(딕셔너리에 해당 값 있으면 앞에것 출력, 없으면 뒤에것 출력), 해당 값이 딕셔너리에 없으므로 'XXX'나옴
sub.get('kor', 'XXX') #해당 값이 딕셔너리에 있으므로 80나옴

sub = {'kor': 80, 'eng': 90, 'mat': 77}
list(sub.keys()) #보통 이렇게 리스트화 시켜서 사용한다.
list(sub.values())
list(sub.items())

sub = {'kor': 80, 'eng': 90, 'mat': 77}
m = list(sub.items())
print(m) #m을 먼저 찍어봐야한다.(m은 딕셔너리를 기반으로 만들어졌기 때문에, 항목들의 순서가 무작위로 나오기 때문.
print(m[2][0]) #눈으로 리스트 순서를 확인한 다음에 호출한다.

sub = {'kor': 80, 'eng': 90, 'mat': 77}
sub1 = sub.copy() #원본유지
sub['tot'] = 247
print(sub)
print(sub1) #원본유지







ju = '931223-167453' #나이 구하기
year = int(ju[0:2]) #문자열 슬라이싱
age = 2020 - 1900 - year + 1
print(age)

ju = '931223-167453' #태어난 달 구하기
month = ju[2:4]
print(month + '월')

ju = '931223-167453' #태어난 날짜 구하기
day = ju[4:6]
print(day + '일')

ju = '931223-167453' #성별 구하기
if int(ju[7]) % 2 == 0:
    print('여자입니다.')
else:
    print('남자입니다.')

ju = '931223-167453' #몇 년대 생인지 구하기
if int(ju[7]) in [1, 2]:
    print('1900년대 생입니다.')
else:
    print('2000년대 생입니다.')

ju = '031223-367453' #나이 구하기 최종
if int(ju[7]) in [1, 2]:
    print(2020 - 1900 - int(ju[0:2]) + 1)
else:
    print(2020 - 2000 - int(ju[0:2]) + 1)

s = '1-2-3-4-5-6-7-8-9' #문자열 안의 숫자들 합 구하기(map함수 이용)
t = s.split('-')
t = list(map(int, t)) #출처: https://shayete.tistory.com/entry/리스트의-문자열을-int-형태로-변환 [샤의 공간]
print(sum(t))

s = '1-2-3-4-5-6-7-8-9' #문자열 안의 숫자들 합 구하기(for문 이용)
t = s.split('-')
tot = 0
for i in t:
    tot += int(i)
print(tot)






















