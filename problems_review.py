#1. a = [1, 2, 5, 4, 3]를 순서대로 만들어보세요.
a = [1, 2, 5, 4, 3]
a = list(set(a))
print(a)

a = [1, 2, 5, 4, 3]
a.sort()
print(a)

###############2. a= [1, 2, 5, 4, 3]를 a = [5, 4, 3, 2, 1]로 만들어보세요.
 a= [1, 2, 5, 4, 3]
 a.sort(reverse = True)
 print(a)


#3. a = ['h', 'e', 'l', 'l', 'o']를 a = 'hello'로 만들어보세요.
a = ['h', 'e', 'l', 'l', 'o']
a = ''.join(a)
print(a)

################4. '경기도 평택시 중앙로 176 101동 706호'를 빈 칸을 기준으로 분리시킨 후(리스트 안에서) 각각 출력하시오
add = '경기도 평택시 중앙로 176 101동 706호'
add1 = add.split(' ')
for i in range(len(add1)):
    print(add1[i])

#5. a = (1, 2, 3)에 4를 추가하시오.
a = (1, 2, 3)
a = a + (4,)
print(a)

#######################6. dic = {'a': 2, 'b': 3, 'c' : 4}를 이용해 del과 pop의 차이점을 보이시오.
dic = {'a': 2, 'b': 3, 'c' : 4}
del dic['a']
print(dic)

dic = {'a': 2, 'b': 3, 'c' : 4}
dic1 = dic.pop('a')
print(dic1)
print(dic)



#7. a = [1, 1, 3, 3, 2, 2, 3, 1, 2, 3, 2, 1]을 a = [1, 2, 3]으로 바꾸시오.
a = [1, 1, 3, 3, 2, 2, 3, 1, 2, 3, 2, 1]
a = list(set(a))
print(a)

#8. [1, 4, 9, 16, 25]를 출력하시오.
squ_list = []
for i in range(1, 6):
    num = i ** 2
    squ_list.append(num)
print(squ_list)

############9.이윤규의 총점과 평균을 구하시오.
score = []
score.append({'이름': '이윤규', '국어': 98, '영어': 100, '수학': 100})
score.append({'이름': '김도희', '국어': 93, '영어': 100, '수학': 95})
score.append({'이름': '이정환', '국어': 90, '영어': 100, '수학': 100})
score.append({'이름': '이윤지', '국어': 100, '영어': 100, '수학': 99})

tot = score[0]['국어'] + score[0]['영어'] + score[0]['수학']
avg = tot / 3
print(tot, avg)

sco = []
sco.append(score[0]['국어'])
sco.append(score[0]['수학'])
sco.append(score[0]['영어'])
print(sum(sco), sum(sco) / len(sco))



#10. 이 사람들의 국어 점수의 총합을 구하시오.
score = []
score.append({'이름': '이윤규', '국어': 98, '영어': 100, '수학': 100})
score.append({'이름': '김도희', '국어': 93, '영어': 100, '수학': 95})
score.append({'이름': '이정환', '국어': 90, '영어': 100, '수학': 100})
score.append({'이름': '이윤지', '국어': 100, '영어': 100, '수학': 99})

tot_kor = []
for i in range(len(score)):
    tot_kor.append(score[i]['국어'])
print(sum(tot_kor))

tot_kor = 0
for i in range(len(score)):
    tot_kor += score[i]['국어']
print(tot_kor)

tot_kor = 0
for i in score:
    tot_kor += i['국어']
print(tot_kor)

############11. 이 반에서 모든 과목 중 가장 점수가 낮은 사람의 이름을 출력하시오.
score = []
score.append({'이름': '이윤규', '국어': 98, '영어': 100, '수학': 100})
score.append({'이름': '김도희', '국어': 93, '영어': 100, '수학': 95})
score.append({'이름': '이정환', '국어': 90, '영어': 100, '수학': 100})
score.append({'이름': '이윤지', '국어': 100, '영어': 100, '수학': 99})

min1 = 0
min2 = 100
for i in range(len(score)):
    if score[i]['국어'] < score[i]['영어'] and score[i]['국어'] < score[i]['수학']:
        min1 = score[i]['국어']
    elif score[i]['영어'] < score[i]['국어'] and score[i]['영어'] < score[i]['수학']:
        min1 = score[i]['영어']
    elif score[i]['수학'] < score[i]['국어'] and score[i]['수학'] < score[i]['영어']:
        min1 = score[i]['수학']
    
    if min1 < min2:
        min2 = min1

for i in range(len(score)):
    if min2 in score[i]:
        print(score[i]['이름'])


    
   
        

score[i][j]
###########12. '이'씨들의 국어 점수의 총합을 구하시오.
score = []
score.append({'이름': '이윤규', '국어': 98, '영어': 100, '수학': 100})
score.append({'이름': '김도희', '국어': 93, '영어': 100, '수학': 95})
score.append({'이름': '이정환', '국어': 90, '영어': 100, '수학': 100})
score.append({'이름': '이윤지', '국어': 100, '영어': 100, '수학': 99})

lee_kor = []
for i in range(len(score)):
    if '이' in score[i]['이름']:
        lee_kor.append(score[i]['국어'])
print(sum(lee_kor))

###########13. 수학이 100점인 사람들을 삭제하시오.
score = []
score.append({'이름': '이윤규', '국어': 98, '영어': 100, '수학': 100})
score.append({'이름': '김도희', '국어': 93, '영어': 100, '수학': 95})
score.append({'이름': '이정환', '국어': 90, '영어': 100, '수학': 100})
score.append({'이름': '이윤지', '국어': 100, '영어': 100, '수학': 99})

for i in range(len(score)):
    if score[i]['수학'] == 100:
        del score[i]
print(score)

#14. 오늘 날짜 중 연도만 출력하시오.
import datetime
d = datetime.date.today()
print(d.year)

#15. 오늘로부터 2일후를 출력하시오.
import datetime
d = datetime.date.today()
t = timedelta(days = 2)
print(d + t)

#16. 2021년 1월 1일까지는 몇 일 남았는지 쓰시오.
import datetime
d = datetime.date.today()
t = datetime.date(2021, 1, 1)
print(t - d)

#17. 시간을 설정하고 출력하시오.
import datetime
d = datetime.time(21, 11, 35)
print(d)

#18. 시간을 설정하고 시, 분, 초를 출력하시오.
import datetime
d = datetime.time(21, 11, 35)
print(d.hour)
print(d.minute)
print(d.second)

#19. 날짜와 시간을 설정하고 출력해보세요.
import datetime
d = datetime.datetime(2012, 3, 7, 14, 24, 1)
print(d)

#20. 오늘 날짜와 시간을 출력하시오.
import datetime
d = datetime.datetime.now()
print(d)

##########21. 함수를 이용하여 단을 입력받아 해당 단의 구구단을 출력하는 프로그램을 작성하시오.
def gugudan():
    gu = int(input('몇 단을 출력할까요?'))
    for i in range(1, 20):
        print('{} * {} = {}'.format(gu, i, gu * i))
gugudan()


#22. 두 수를 입력 받아 두 수 사이의 수들의 합을 구하시오.(함수 사용)
def delta_sum():
    fir = int(input('Enter the first number: '))
    sec = int(input('Enter the second number: '))
    if fir <= sec:
        delta_sum_ = 0
        for i in range(fir + 1, sec):
            delta_sum_ += i
        print(delta_sum_)
    else:
        delta_sum_ = 0
        for i in range(sec + 1, fir):
            delta_sum_ += i
        print(delta_sum_)
delta_sum()

#23. 두 수를 입력받아 큰 수를 출력하시오.
def two_comparison():
    fir = int(input('첫 번째 수를 입력하시오: '))
    sec = int(input('두 번째 수를 입력하시오: '))
    if fir > sec:
        return fir
    elif fir == sec:
        return 'same'
    else:
        return sec
comparison()

#24. 세 수를 입력받아 가장 큰 값을 출력하시오.
def three_comparison():
    fir = int(input('첫 번째 수를 입력하시오: '))
    sec = int(input('두 번째 수를 입력하시오: '))
    thi = int(input('세 번째 수를 입력하시오: '))
    if fir > sec and fir > thi:
        return fir
    elif sec > fir and sec > thi:
        return sec
    elif thi > fir and thi > sec:
        return thi
    else:
        return 'none'
three_comparison()

#25.
class Human:
    def __init__(self, name, age, gen):
        self.name = name
        self.age = age
        self.gen = gen
    
    def who(self):
        print('이름: {}, 나이: {}, 성별: {}'.format(self.name, self.age, self.gen))
    
areum = Human('아름', 25, '여자')
print(areum.name)
print(areum.age)
print(areum.gen)

print(Human.who(areum))


    





