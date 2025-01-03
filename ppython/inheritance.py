## 파이썬도 부모를 참조할 때 super()를 사용한다
## 파이썬은 부모의 메소드를 오버라이드 할 때 따로 어노테이션 없이 동일한 시그니처의 메소드를 그냥 재정의하면 된다.
## 파이썬은 클래스의 다중상속이 가능하다. 
## 부모로의 접근 > super()
## 아니 그리고 왜 지 함수를 호출하는데 꼭 self를 붙여야 함?

class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class VideoMaker:
    def make(self):
        print('비디오를 만들었습니다.')

class MailSender:
    def send(self):
        print('메일로 발송하였습니다.')

class TravelBlackBox(BlackBox, VideoMaker, MailSender):
    def __init__(self, name, price, storage):
        ## BlackBox.__init__(self, name, price) > 이렇게 부모 메소드 호출은 잘 사용 안 하는듯
        super().__init__(name, price) ## self 필요없음
        self.storage = storage

    def test(self):
        self.set_travel_mode(20)      
    def set_travel_mode(self, minute):
        print(str(minute) + '분 동안 여행모드 ON')
      



bb1 = TravelBlackBox('우리룽', 240000, '128GB')
bb1.test() # > NameError



#override
class AdvancedTravelBlackBox(TravelBlackBox):
    def set_travel_mode(self, minute):
        print(str(minute) + '분 동안 여행모드 ON')
        ## make()
        ## send() >> ...??????? 왜 이렇게 쓰면 안됌?.. 개거지같네 진짜 거지가같은 파이썬새끼 ㅈㄴ까 
        self.make()
        self.send()

abb1 = AdvancedTravelBlackBox('우리리룽', 300000, '128GB')
abb1.set_travel_mode(40)