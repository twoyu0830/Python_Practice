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
cat2.info() #인스턴스의 매소드 호출.

