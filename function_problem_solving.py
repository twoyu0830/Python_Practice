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





