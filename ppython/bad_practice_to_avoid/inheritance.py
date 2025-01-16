# composition instead of inheritance
# --> 자바랑 똑같다. 부모클래스와 자식클래스간의 결합도가 높아져 유지보수에 어려울 수 있으므로 참조 사용을 권장


# bad example
class Employee:
    def get_position(self) -> str:
        return "Employee"
    

class Manager(Employee):
    def get_position(self) -> str:
        return "Manager"
    

class SeniorManager(Employee):
    def get_position(self) -> str:
        return "Senior Manager"
    

class Director(SeniorManager):
    def get_position(self) -> str:
        return "Director"


def main() -> None:
    manager = Manager()
    senior_manager = SeniorManager()
    director = Director()
    print(manager.get_position())
    print(senior_manager.get_position())
    print(director.get_position())









# pythonic example
# position을 별도의 object로 분리해서 참조한다.

from enum import StrEnum, Enum 

class Position(StrEnum): # StrEnum은 value만 출력이되고, Enum은 Enum이름.value 로 출력된다.
    EMPLOYEE = "Employee"
    MANAGER = "Manager"
    SENIOR_MANAGER = "Senior Manager"
    DIRECTOR = "Director"



class AnotherEmployee:
    def __init__(self, position: Position) -> None:
        self.position = position

    def get_position(self) -> str:
        return self.position


def main2() -> None:
    manager = AnotherEmployee(Position.MANAGER)
    senior_manager = AnotherEmployee(Position.SENIOR_MANAGER)
    director = AnotherEmployee(Position.DIRECTOR)
    print(manager.get_position())
    print(senior_manager.get_position())
    print(director.get_position())


if __name__ == "__main__":
    main2()



# https://www.youtube.com/watch?v=yFLY0SVutgM