#1. a = [1, 2, 5, 4, 3]를 순서대로 만들어보세요.
a = [1, 2, 5, 4, 3]
a.sort()
print(a)

#2. a= [1, 2, 5, 4, 3]를 a = [5, 4, 3, 2, 1]로 만들어보세요.
a = [1, 2, 5, 4, 3]
a.sort(reverse = True)
print(a)

#3. a = ['h', 'e', 'l', 'l', 'o']를 a = 'hello'로 만들어보세요.
a = ['h', 'e', 'l', 'l', 'o']
b = ''.join(a)
print(b)

#4. '경기도 평택시 중앙로 176 101동 706호'를 빈 칸을 기준으로 분리시킨 후(리스트 안에서) 각각 출력하시오
a = '경기도 평택시 중앙로 176 101동 706호'
b = a.split(' ')
for i in b:
    print(i, end = ' ')

#5. a = (1, 2, 3)에 4를 추가하시오.
a = (1, 2, 3)
print(a + (4,))

#6. dic = {'a': 2, 'b': 3, 'c' : 4}를 이용해 del과 pop의 차이점을 보이시오.
dic = {'a': 2, 'b': 3, 'c' : 4}
del dic['b']
print(dic)

dic = {'a': 2, 'b': 3, 'c' : 4}
dic1 = dic.pop('b')
print(dic1)
print(dic)

#7. a = [1, 1, 3, 3, 2, 2, 3, 1, 2, 3, 2, 1]을 a = [1, 2, 3]으로 바꾸시오.
a = set(a)
a = list(a)
print(a)

#8. [1, 4, 9, 16, 25]를 출력하시오.
b = [] #for문 이용
for i in range(1, 6):
    a = i ** 2
    b.append(a)
print(b)
    
a = 1 #while문 이용
b = []
while a <= 5:
    b.append(a ** 2)
    a += 1
print(b)


