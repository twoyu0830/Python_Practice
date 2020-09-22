#클래스가 만들어진 이유: 다양한 것을 담고 싶어서, 추상화된 현실의 개념을 구체적인 파이썬 코드로 표현하기 위해, 빵틀과 빵의 관계 만들기 위해
class Cat: #대문자가 관습
    def __init__(self, name, color): #매소드(클래스의 함수), self는 인스턴스를 지칭함(cat1, cat2 각각) 이걸 통해 매소드 안의 내용을 구성할 수 있다.
        self.name = name #인스턴스 변수 name 생성
        self.color = color #인스턴스 변수 color 생성
    def info(self):
        print('고영이 이름은', self.name, '색깔은', self.color)  

cat1 = Cat('네로', '검정색') #인스턴스 생성(__init__매소드의 name, color에 들어감)
cat2 = Cat('미미', '갈색') #인스턴스 생성(__init__매소드의 name, color에 들어감)

cat1.info() #인스턴스의 매소드 호출
cat2.info() #인스턴스의 매소드 호출


class Person:
    def __init__(self): #__init__ 매소드는 초기값들을 넣어주는 매소드라는 의미에서 초기자라고 불린다.
        self.name = input('이름을 입력하시오: ')
        self.age = int(input('나이를 입력하시오: '))
    def info(self):
        print('{0}씨는 {1}세이십니다.'.format(self.name, self.age))

li = []
for i in range(4):
    li.append(Person()) #객체 생성할 개수만큼 append해둠(클래스에서 정보를 받아줄 거기 때문에 Person() 괄호 안에 아무 정보도 쓰지 말고)
for i in range(4):
    li[i].info() #매소드 호출



