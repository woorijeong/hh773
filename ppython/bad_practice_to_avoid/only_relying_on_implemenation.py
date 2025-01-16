# 구현체 타입에만 의존하는 것 
# --> 자바랑 동일하게 추상화한 인터페이스에 의존하게 해서 유연한 구조를 가져간다. 
# --> 파이썬에서 인터페이스 만드는 방법 
'''
##### Protocol 클래스를 상속받으면 된다. 
##### ==> 구현체 클래스 시그니처에 부모 클래스 명시 X
##### ==> 그냥 추상메소드를 오버라이드하면 구현체로 인식 O

파이썬은 다중상속을 허용하지만 사용하지 X > 결합도가 높아지고 동일한 시그니처의 메소드가 부모들에 존재할 가능성 O
'''

from dataclasses import dataclass

@dataclass     # entity용 클래스 생성에 적합, 데이터 이동용
class Order:   # getter, setter는 안 만들어줌
    __customer_email: str
    __product_id: int
    __quantity: int

    @property
    def customer_email(self) -> str:
        return self.__customer_email




# bad example
class SmtpEmailService:
    def connect_to_smtp_server(self) -> None:
        print("Connection to SMTP Server,,,")


    def send_email(self, recipient: str, message: str) -> None:
        print(f"Sending email to {recipient}: {message}")


def process_order(order: Order) -> None:
    email_service = SmtpEmailService()
    email_service.connect_to_smtp_server()
    email_service.send_email(order.customer_email, "Your order has been processed!")


def main() -> None:
    order = Order("wrjeong@github.com",1,6) # private로 정의한 속성은 키워드 인자 방법으로 파라미터 할당이 안된다.
    process_order(order)




# pythonic example
from typing import Protocol

class EmailService(Protocol):
    def send_email(self, recipient: str, message: str) -> None:
        ... # 추상메소드 정의하는 방법, 인터페이스에서 정의해도 self인자가 들어간다.


def new_process_order(email_sender: EmailService, order: Order) -> None: # 내부에서 서비스 인스턴스 생성 X -> DI
    #... 주문
    email_sender.send_email(order.customer_email, "Your order has been processed new way!")

def main2() -> None:
    email_sender = SmtpEmailService()
    email_sender.connect_to_smtp_server()

    order = Order("wrjeong@github.com",2,3)

    new_process_order(email_sender, order)



if __name__ == "__main__":
    main2()


# https://www.youtube.com/watch?v=yFLY0SVutgM



