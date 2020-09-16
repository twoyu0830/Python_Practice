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

#9.이윤규의 총점과 평균을 구하시오.
score = []
score.append({'이름': '이윤규', '국어': 98, '영어': 100, '수학': 100})
score.append({'이름': '김도희', '국어': 93, '영어': 100, '수학': 95})
score.append({'이름': '이정환', '국어': 90, '영어': 100, '수학': 100})
score.append({'이름': '이윤지', '국어': 100, '영어': 100, '수학': 99})

tot = score[0]['국어'] + score[0]['영어'] + score[0]['수학']
print('총점: ', tot)
print('평균: ', tot / 3)

#10. 이 사람들의 국어 점수의 총합을 구하시오.
score = []
score.append({'이름': '이윤규', '국어': 98, '영어': 100, '수학': 100})
score.append({'이름': '김도희', '국어': 93, '영어': 100, '수학': 95})
score.append({'이름': '이정환', '국어': 90, '영어': 100, '수학': 100})
score.append({'이름': '이윤지', '국어': 100, '영어': 100, '수학': 99})

kor_tot = score[0]['국어'] +  score[1]['국어'] +  score[2]['국어'] +  score[3]['국어'] #1)이차원 리스트 접근
print(kor_tot)

kor_tot = 0 #2) 리스트 안의 딕셔너리들을 i로
for i in score:
    kor_tot += i['국어'] #딕셔너리의 키로 접근
print('국어 점수의 총합: ', kor_tot)

kor_tot = 0 #3) 리스트 길이의 숫자를 i로
for i in range(len(score)):
    kor_tot += score[i]['국어'] #이차원 리스트 접근
print('국어 점수의 총합: ', kor_tot)


#11. 이 반에서 모든 과목 중 가장 점수가 낮은 사람의 이름을 출력하시오.
score = []
score.append({'이름': '이윤규', '국어': 98, '영어': 100, '수학': 100})
score.append({'이름': '김도희', '국어': 93, '영어': 100, '수학': 95})
score.append({'이름': '이정환', '국어': 90, '영어': 100, '수학': 100})
score.append({'이름': '이윤지', '국어': 100, '영어': 100, '수학': 99})

mini = 100
for i in score:
    min = 0
    if i['국어'] < i['영어'] and i['국어'] < i['수학']: #각 사람별 가장 낮은 점수 구하기
        min = i['국어']
    elif i['영어'] < i['국어'] and i['영어'] < i['수학']:
        min = i['영어']
    else:
        min = i['수학']
    print('min: ', min) 
    if min < mini: #사람들 한 바뀌 돌 때 마다 비교해서 가장 낮은 것 갱신시킴
        mini = min
print('최소점수: ', mini)

#11. '이'씨들의 국어 점수의 총합을 구하시오.
score = []
score.append({'이름': '이윤규', '국어': 98, '영어': 100, '수학': 100})
score.append({'이름': '김도희', '국어': 93, '영어': 100, '수학': 95})
score.append({'이름': '이정환', '국어': 90, '영어': 100, '수학': 100})
score.append({'이름': '이윤지', '국어': 100, '영어': 100, '수학': 99})

lee_kor_tot = 0
for i in range(len(score)):
    if '이' in score[i]['이름']:
        lee_kor_tot += score[i]['국어']
print(lee_kor_tot)


#12. 수학이 100점인 사람들을 삭제하시오.
score = []
score.append({'이름': '이윤규', '국어': 98, '영어': 100, '수학': 100})
score.append({'이름': '김도희', '국어': 93, '영어': 100, '수학': 95})
score.append({'이름': '이정환', '국어': 90, '영어': 100, '수학': 100})
score.append({'이름': '이윤지', '국어': 100, '영어': 100, '수학': 99})

for i in score: #1) 리스트 안의 딕셔너리들을 i로
    if i['수학'] == 100: #딕셔너리의 키로 접근
        score.remove(i) #i는 딕셔너리들이다.
print(score)

for i in range(len(score)): #2) 리스트 길이의 숫자를 i로
    if score[i]['수학'] == 100: #이차원 리스트 접근
       del score[i] #i는 그냥 숫자다.
print(score)














