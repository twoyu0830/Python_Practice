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
b = sorted(li2) #아예 li2자체를 바꾸지 않고, 할당을 해줘서 원본은 유지하고 정렬된 것은 b에 있다.
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




