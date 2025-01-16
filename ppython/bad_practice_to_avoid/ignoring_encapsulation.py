# 캡슐화
# --> 무분별한 getter, setter 지양 
# --> + 접근제어자 사용 
'''
파이썬은 접근제어자 따로 없고 개발자들간의 약속만 있는데 
실제 __로 정의한 private 필드를 클래스 바깥에서 사용하려고 하면 런타임시 에러남 


__xxx : private
_xxx : package
xxx : public
__xxx__ : public

private 필드는 키워드 인자 방법으로 사용할 수 없다
'''

# bad example
class BackAccount:
    def __init__(self, balance: int) -> None: # int 보다는 Decimal(소수점) 패키지 사용이 더 적절, 보다 정수 계산이 ..
        self.balance = balance 


def main() -> None:
    account = BackAccount(1000000)
    print(account.balance)

    account.balance += 10
    print(account.balance)

    account.balance -= 50000
    print(account.balance)

if __name__ == "__main__":
    main()



# pythonic example
from decimal import Decimal

class NewBackAccount:
    def __init__(self, deposited: Decimal, balance: Decimal) -> None:
        self.__deposited = deposited
        self.__balance = balance
    
    @property
    def deposited(self) -> None:
        return self.__deposited
    
    @property
    def balance(self) -> None:
        return self.__balance
    
    def interest(self) -> Decimal:
        interested = self.__deposited + (self.__deposited * self.__balance)
        print(f"이자가 붙은 후 금액 : {interested}")
        return interested
    
    def deposit(self, amount: Decimal) -> None:
        if amount < Decimal(0):
            raise ValueError("입금하고자 하는 값은 0보다 커야 합니다.") # 필드에 직접접근하지 않으면 validation 가능
        
        self.__deposited += amount
    
    def withdraw(self, amount: Decimal) -> None:
        if self.deposited < amount:
            raise ValueError("입금된 금액보다 큰 금액을 출금할 수 없습니다.")
        
        self.__deposited -= amount
    

def main2() -> None:
    account = NewBackAccount(Decimal(1000000), Decimal(0.01))
    print(f"deposited={account.deposited}")
    print(f"balance={account.balance}")

    print(f"interested={account.interest()}")

    account.withdraw(Decimal(2000000))

if __name__ == "__main__":
    main2()    



# https://www.youtube.com/watch?v=yFLY0SVutgM