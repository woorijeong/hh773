# @dataclass : data oriendted structure <> behaviour oriented structure having several methods.
# @dataclass 로 부터 어떤 도움은 받는가?
# 1. toString 역할 > 사실은 repr메소드가 생성됨. (디버깅을 위해 타입까지 표시하는 메소드, 문자열로 출력하는 방법 중 하나)
# 2. 클래스 필드 정의가 간편하다
# 3. comparing objects for sorting
# 4. 초기화
# >>>> @dataclass == @lombok

import random
import string
from dataclasses import dataclass, field

def generate_id() -> None: # 메소드가 아니니까 self X
    return "".join(random.choices(string.ascii_uppercase, k=10))

@dataclass(frozen=False, kw_only=True, slots=True) # decorator annotation # frozen=True로 설정하면 불변객체가 된다. (false가 default) # kw_only=True로 설정하면 객체 생성 시 생성자에
#인자 전달할 때 키워드를 반드시 써서 생성해주어야 함. ex. name='우리' > new in python3.10
class Person:
    name: str
    address: str
    active: bool = True # 파이썬에서 boolean 타입은 앞 문자가 반드시 대문자여야 함 >> 얘는 primitive라서 ㄱㅊ은데??,,, static?? 엥 얘는 인스턴스 변순데?
    # email_addresses: list[str] = [] # 문제생기는 코드 > 이거는 데이터클래스 데코레이터가 발생시키는 문제인거 같음
    another_email_addresses: list[str] = field(default_factory=list) # 이럴때는 팩토리함수를 사용한다. field도 데이터클래스에서 온 거임
                                                                     # list는 타입이 아니고 함수임. !!! >> 이거 근데 어차피 field로 안 하면 에러남
    __id: str = field(init=False, default_factory=generate_id) # 우히히히히히히히히히
                                                   # id는 private으로 설정하거나, field의 init 인자를 False로 주면 생성ㅇ자를 통해 값을 주입할 수 없게 된다.
    __search_string: str = field(init=False, repr=False) # repr를 False로 하면 출력이 되지 않는다.

    def __post_init__(self): # frozen=Ture를 하면 post_init 실행이 안됌.
        self.__search_string = f'{self.name} {self.address}' # 다른 인스턴스 변수로 부터 인스턴스의 값을 설정하고 싶을 때 

    def get_active(self) -> bool:
        return self.active
    
    def set_active(self, state: bool) -> None:
        self.active = state

    


# @dataclass 단점 : 클래스변수와 인스턴스변수의 정의가 모호하다.
# ???....... @dataclass를 정의하지 않으면 모두 클래변수가 된다 인스턴스 변수가 아니고? 뭐래갭까치네기자나렁론이뢍노라ㅣㅇ노리ㅏㅇ노린로이나ㅗ링노리
# 엥 진짜 이 상태로 되네?
class Adult:
    def __init__(self, name, address, age) -> None:
        self.name = name
        self.address = address
        self.age = age
    
    def __str__(self) -> str:
        return f'{self.name} {self.age} {self.address}'


def main() -> None:
    person1 = Person(name='우리', address='성내동 233-1') # 생성자가 생성된것
    person2 = Person(name='미향', address='성내동 233-1') # 생성자가 생성된것
    print(person1) # repr이 생성된것
    print(person2)

    person1.set_active(False)
    print(person1)
    print(person2) ## 뭐여 인스턴스 변수자네

    # 당연하지만.. default 값은 다른 값으로도 가넝..
    # private 값은 생성자 인자로도 안됌,,,,?????????????????????????
    person3 = Person(name='연주', address='성내동 233-1', active=False)
    print(person3)

    # person4 = Person('하나', '성내동 200-12') # kw_only=True면 이렇게 생성이 되지 않음


    adult = Adult("마이구미", "LA 24단지 89", 22)
    print(adult.__dict__["name"])
  

if __name__ == '__main__':
    main()


# 다른 장점 - default value 정의 되는데 primitive type에 대해서만 잘 동작, 리스트 이런건 잘 안됌
# 엥 아니 존나이상함 미친거아님 왜 새로 생성 안하고 공유함? ???????????????????????????????/미친언어새끼거지ㅣ같애시바러알ㅈ갲짜걸
# email_addresses: list[str] = [] 이렇게 하면 모든 인스턴스가 해당 리스트를 공유 > static처럼 동작함
# 움.. 자바에서 new같은거랑은 다른..방식으로 []가 동작하나봄 개짜증남진짜거지같움화남

# 파이썬은 primtive 타입에 불변 메커니즘이 없움. != 자바

# dunder = double under = 특수메소드 == 매직메소드 ex. repr, str, init, dict
# 파이썬에서는 객체 삭제도 된다 ex. del person1 > 이 명령어 실행 시 Person 클래스 내 정의된 __del__(self)이 실행된다.
# __eq__(self, other)는 객체를 ==으로 비교할 때 사용된다. 
# dir(int), dir(str)을 하면 int, str 클래스가 가진 매직 메소드들을 확인할 수 있다. 

# slots 옵션 > new in python 3.10 >> 기존 __dict__ 보다 much more directly >> faster >> 이거는 @dataclass로만 가능
# 그러면은 얘가 __dict__ 대신에 slot객체를 사용해 접근한다 >> slots=False 가 default
#  파이썬 클래스의 인스턴스를 만들면 내부적으로 __dict__ 객체가 생긴다. 이는 인스턴스 변수를 바탕으로 생성된 딕셔너리이다.
# 해당 딕셔너리로 인스턴스 변수에 접근할 경우 direct로 접근하기 때문에 더 빠르게 접근이 가능하다. 이걸 더 빠르게 한 매커니즘을 slot이라고 한다. 
# The default classes use the Dunder dict to access instace variables
# > 근데 slot이 안먹힐떄가 있음. > 다중상속 할 떄 

#@dataclass 의 match_args 속성 > new in python3.10
# 인스턴스 생성 시 매직 메소드 __match_ags__가 생성되고 structual pattern matching 에 사용된다?
#@dataclass는 디폴트로 match arg가 true이다. 대외적으로 지원한다고 말한셈.

