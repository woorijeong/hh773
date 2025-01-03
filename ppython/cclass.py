class One:
    pass ##형태만 만들어 놓을 때

one = One()
##one.direction = 'yeah'
##print(one.direction) >> 이딴거 쓰지말자 캡슐화 미친놈임
print(isinstance(one, One))
### >> 파이썬은 접근제한자가 있나?? 없다.. ㅈㄴ어이없다
### 필드 이름 컨벤션만 있다
### public : 걍 영어 ex. direction / protected : _ 1개 ex. _direction / private : _ 2개 ex. __direction
### 존나 어이없음 필드 이름 뒤에 _ 두 개 들어가면 다시 퍼블릭이 된단다.. ㅋㅋㅋㅋ
### ....? 근데 컨벤션이라고 해놓고 문법이 있는거 같긴 함... .......????

class Two:
    def __init__(self, one, two):
        self.__one = one
        self._two = two
        self.three = '3'

    @property
    def one(self):
        return self.__one

    def get_one(self):
        return self.__one

    def set_one(self, one):
        self.__one = one

    @one.setter ## property랑 같은 역할, 메소드를 안쓰게해줌, @필드명.setter > 필드명 틀리면 에러
    def one(self, one):
        self.__one = one

    def __str__(self) -> str: ##내장함수 toString과 같다
        return f'{self.__one} - {self._two} - {self.three} 가 있습니다.'
        


two = Two('1', '2')
#print(two.__one) ## 따로 접근제한자 없다고 했으면서 private 컨벤션으로 지정한 필드 호출하면 에러남; 개어이없음
print(two.one) ## 메소드에 @property 어노테이션을 지정하면 ()을 사용하지 않고 필드처럼 접근 가능
print(two.get_one()) ## 없으면 ()로 호출해줘야 함
two.set_one('8')
two.one = '9' 
print(two.get_one(), end='')
print()
print(two._two)
print(two.three)

two.new_mem = 'what?@?@?!!??!?!!'
print(two.new_mem) ## >>이딴거 쓰지 말자~, 클래스에 멤버변수를 추가하는게 아니고 객체에 멤버변수를 동적으로 추가하는 것..


## 파이썬에서는 메소드가 static 처럼 쓰...일순 없음, self가 필요하니까
print(two.get_one())
print(Two.get_one(two)) ## > 둘이 같은건데 클래스를 통해서 호출할 수도 았음, 근데 self도 전달해줘야 하긴 함
print(__name__)

