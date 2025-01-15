from pathlib import Path

#bad example1
# 아래 예시는 클래스가 메소드 홀더 정도로 사용되고 있어서 클래스 정의가 불필요한 상황.
'''
파이썬은 OOP긴 한데, 자바처럼 무조건 class를 생성해야 하는 것이 아니므로,
꼭 필요한 경우에만 class를 생성하도록 하자
--> 
1. @dataclass 목적
2. 다수의 인스턴스 생성이 필요한 경우
3. 인스턴스 필드와 직접적으로 다루는 메소드가 필요한 경우


'''
class DataLoader:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path
    
    def load(self) -> str:
        with open(self.file_path, "r", encoding="UTF-8") as file_data:
            return file_data.read()

    def store(self) -> None:
        with open(self.file_path, "w", encoding="UTF-8") as file_data:
            file_data.write("샤브샤브 삼겹살 김밥 먹고싶다.")
        


def main() -> None:
    data_loader = DataLoader("./ppython/bad_practice_to_avoid/meal.txt")
    data_loader.store()
    print(data_loader.load())



# pythonic example1
def load(file_path:Path) -> str:
    with open(file_path, "r", encoding="UTF-8") as file_data:
        return file_data.read()

def store(file_path:Path, content:str) -> None:
    with open(file_path, "w", encoding="UTF-8") as file_data:
        file_data.write(content)


def main2() -> None:
    file_path = Path("./ppython/bad_practice_to_avoid/meal.txt") # 주의 Path에서 .경로는 현재 작업중인 파일이 존재하는 폴더가 X / IDE에서 연 최상단 폴더 경로 O
    store(file_path, "샤브샤브 삼겹살 김밥 먹고싶다. 정말루..")
    print(load(file_path))



# bad example2
class StringProcessor:
    vowels = 'aeiouAEIOU' # class 변수

    @staticmethod
    def reverse(s: str) -> str:
        return s[::-1]
    
    @staticmethod
    def upper(s: str) -> str:
        return s.upper()
    
    @staticmethod
    def remove_vowels(s: str) -> str:
        return "".join([char for char in s if char not in StringProcessor.vowels]) # vowels로 클래스 변수 참조 못 함
        

def main3() -> None:
    s = 'yeobgi chicken soup what i want is!'
    print(StringProcessor.reverse(s))
    print(StringProcessor.upper(s))
    print(StringProcessor.remove_vowels(s))



# pythonic example2

from StringProcessor import reverse, upper, remove_vowels # 실제로 최상단부에 한 번에 import 해주는게 좋다

def main4() -> None:
    s = 'yeobgi chicken soup what i want is!'
    print(reverse(s))
    print(upper(s))
    print(remove_vowels(s))



if __name__ == '__main__':
    main4()

# https://www.youtube.com/watch?v=yFLY0SVutgM

