# https://www.youtube.com/watch?v=yFLY0SVutgM

# 1. A function masquerading as a class
# 2. A module masquerading as a class
# --> function과 module로 안될 때 class 사용 (자바랑은 다른!)
#     임의의 데이터와 행동을 하나로 묶어야 하거나, 다수의 인스턴스가 필요한 경우에만 class로 정의 oop misleading
# 멤버변수 없이 단순히 메소드를 감싸기 위한 용도로 클래스 생성하지 X 
# --> 불필요하게 객체를 생성해야 하고 읽기 어려움

from pathlib import Path

#bad example
class DataLoader:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path
    
    def load(self) -> str:
        with open(self.file_path, "r", encoding="UTF-8") as file_data:
            return file_data.read()

    def store(self) -> None:
        with open(self.file_path, "w", encoding="UTF-8") as file_data:
            file_data.write("샤브샤브 삼겹살 김밥 먹고싶다.")
        

'''def main() -> None:
    data_loader = DataLoader("./ppython/bad_practice_to_avoid/meal.txt")
    data_loader.store()
    print(data_loader.load())

if __name__ == '__main__':
    main()
'''

# good example
def load(path: Path) -> str:
    with open(path, "r", encoding="UTF-8") as file_data:
        return file_data.read()

def store(path: Path, content: str) -> None:
    with open(path, "w", encoding="UTF-8") as file_data:
        file_data.write(content)

def main() -> None:
    store("./ppython/bad_practice_to_avoid/meal.txt", "샤브샤브 삼겹살 김밥 먹고싶다.")
    print(load("./ppython/bad_practice_to_avoid/meal.txt"))

if __name__ == '__main__':
    main()



# 3. 상속 
# --> 이건 자바랑 유사 
# 상속대신 참조/결합 (composition instead of inheritance.)

# 4. not relying on abstractions 오잉..?
# 뭐여... 메소드 안에서 객체 요상하게 만들고 있었눈디 움...
# 아......ㅋㅋㅋㅋㅋㅋ relying 권유엿음 ㅋㅋ > DI 추천
# Protocol ? > 헐 인터페이스 만드는 방법이랭 from typing import Protocol
# 군데 이상한게 인터페이스 상속받는 클래스는 움 클래스 시그니처에 알려주는게 아니고; 걍 메소드 똑같은 이름 구현해야 함..;;


# 5. not have encapsulation > 맞지맞지
# 보통 get은 그냥 @property로 선언해서 걍 접근하구 set은 별도로..
# 장점은.. 데이터 유효성 검증도 가능하구 내부적으로 로직 변경해도 밖엣는놈루모르르를,...
# 근디 파이썬에서도 int랑 decimal 구분하는듯 
 

#으아으ㅏ아으아으ㅏ 누가 제이슨을 그냥 스트링으로 디비에 넣냐
# 6. Excessive Use Of Getter and Setters
# data-focused class
# 암것도 안 하는디 걍 게터세터만 쓰는거 > 이럴때 ( 행동도 없을 때 ) @dataclass 사용 > data-focused >> 그 그..그 엔티티티티티티용
# 엥 근디 이러면은 setter 걍 없는디 > 불변 어케 써


# 7. heavily relying on mixins to add functionality to existing classes
# 이게모얌...
# 움.....템플릿 메소드 패턴같은거 같은디 엥 아닌거 같음
# python mixin = 상속 종류중에 하나, 클래스에 추가적인 속성이나 메소드를 제공하는 것 
# 아으앙 다중삭속!!!! 하지말라궁~
# 펑셔널인터페이스 같은ㄴ게 잇움


