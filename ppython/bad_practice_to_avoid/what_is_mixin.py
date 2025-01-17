'''
믹스인은 상속의 일종이라고 하는데
기존 상속과 가장 다른 점은 
기존 상속 : 부모가 핵심 클래스이고 자식은 부모를 상속받아 부가적인 행위를 추가한다.
믹스인 : 핵심 클래스가 부가적인 행위가 정의된 클래스들 여러개를 상속받아 부가적인 기능을 자신한테 추가한다.
--> 하나의 클래스가 하나의 책임만 갖도록
--> 믹스인 자체가 파이썬의 다중상속을 사용하고 있다..

자바에는 없는데(클래스는) 파이썬에서 다중상속을 할 경우에 가장 오른쪽에 선언한 클래스가 가장 부모클래스가 된다 
class A(B, C)
= A > B > C
'''

class Loggable:
    def __init__(self, msg: str) -> None:
        self.msg = msg
    
    def log(self) -> None: # 행위인 로깅과
        print(f"Log Message : {self.msg}")


class Connection:
    def __init__(self, server: str) -> None:
        self.server = server
    
    def connect(self) -> None: # 커넥트 메소드는 Database에서 오버라이드 하지 않고 그대로 가져와서 사용
        print(f"Connecting to database on {self.server2}")


class Database(Loggable, Connection):
    def __init__(self) -> None: # 이 클래스에서 Loggable과 Connection이 가진 __init__ 은 오버라이드
        self.msg = "Database conn demo"
        self.server2 = "127.0.0.1:8888"



def framework(item: Database) -> None:
    if isinstance(item, Loggable):
        item.log()
    if isinstance(item, Connection):
        item.connect()


def main() -> None:
    db = Database()
    framework(db)



#############################################################################################



class BaseTokenizer:
    def __init__(self, target: str) -> None:
        self.target = target

    def __iter__(self): # iterable 객체가 됨
        print("base")
        print(super())
        yield from self.target.split("-")


class UpperInterable:
    def __iter__(self): # iterable 객체가 됨
        print("upper")
        print(super())
        return map(str.upper, super().__iter__())
    

class UpperTokenizer(UpperInterable, BaseTokenizer): # 순서가 중요 > ['HI', 'HOW', 'ARE', 'YOU', '?']
# class UpperTokenizer(BaseTokenizer, UpperInterable): 가장 오른쪽이 가장 상위부모클래스 > ['hi', 'how', 'are', 'you', '?']     
    pass

def main2() -> None:
    tokenizer = UpperTokenizer("hi-how-are-you-?")
    print(list(tokenizer))
    

if __name__ == "__main__":
    main2()
    
