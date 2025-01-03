from datetime import date
from datetime import datetime
#자바에서 else if == elif
#파이썬은 들여쓰기가 중요, 중첩 if 사용시 단계별로 들여쓰기 사용

#range() >> IntSteam() 그런 느낌..인데, 3개의 파라미터까지 받을 수 있음
for x in range(1, 51, 10):
    print(f'{x}')


# 맵 == 딕셔너리 순회를 쉽게 돌 수 있음
diet_dict = {
    'morning' : 'cheese',
    'afternoon' : 'bread',
    'evening' : 'chicken',
    'dawn' : '삼겹살'
}

for k, v in diet_dict.items():
    if (k == 'evening'):
        print(f'다이어트 해야하니까 안 먹어요!')
        continue #작업 건너뛰기
    print(f'{k} 에는 {v}를 먹어요')


# continue 작업 건너뛰기
for x in range(30):
    if (x % 2 == 1):
        continue
    print(f'{x}')


# 리스트 컴프리핸션 | 가변인자 | 특정값 인자 | 기본값 인자 | 변수 힌트
## 리스트 컴프리핸션
list1 = [1,2,3,55,66,2,22,12]
list2 = [str(x) + '개' for x in list1 if x >= 3] ## [ ] 인거 주의!
print(list1)
print(list2)

## 기본값 인자 + 변수 힌트
# ...? 클래스..밖에서도 함수 정의가 가능..한데 이때는 self 안 받음
def hello(name:str='누구'):
    print(f'{name}님 안녕하세요! 좋은 아침이네용~ 달러가 1460원ㅋㅋㅋㅋㅋㅋ')

hello()
hello('우리')

## 특정값 인자
def new_employee(name:str='누구', age:int=24, department:str='미확정'):
    print(f'안녕하세요! {name}입니다! 나이는 {age}입니다. 앞으로 일하게 될 부서는 {department}입니다~ \n 자바도 이런거 있음 좋겠다~')

new_employee(name='우리', age=29)
new_employee(name='우리', age=29, department='IT부서')

d = date.today()
dt = datetime.now()
# >> 파이썬에서 Object를 String으로 보여주는 방법
# 1. str()사용 == print
print(str(d)) 
print(d)
# 2. 디버깅을 위해서 데이터 자체가 어떤 데이터인지 보여주는 방법 
#     >> repr() > 데이터 타입도 보여줌
print(repr(d))
# list == Object 라서 안에 있는 데이터가 어떤 데이터인지를 보여줌
print([d])

print(f'{datetime.now(): %Y-%m-%d}')
print(f'{datetime.now(): %Y-%B-%d}')
print(f'{datetime.now(): %y-%b-%d}')

##가변인자
#    > *visitors
#      인자로 튜플을 받는다는 얘기가 아니라, 함수 내부적으로 인자로 받은 값들이 튜플로 사용된다는 말이었다,...
def salon_visitors_hist(when:str=date.today(), *visitors):
    print(f'{when}에 방문한 사람들은 {visitors}입니다.')

salon_visitors_hist(date.today(), '우리', '돼지', '마녀', '지팡이', '가드')

## **visitors ?? >> 키워드 인자????
## >>>>> 가변인자는 받은 인자들을 함수 내에서 튜플로 사용
## >>>>> 키워드인자는 받은 인자들을 함수 내에서 딕셔너리로 사용
## >>>>> 키워드인자도 가변인자처럼 파라미터의 맨 뒤에 위치해야함
## >>>>> 가변인자를 키워드 인자처럼 사용 불가 ex. visitiors=['우리']

def salon_visitors_hist(**visitors):
    print(f'{datetime.now()}에 방문한 사람들은 {visitors}입니다.')


salon_visitors_hist(단골='우리', 첫손님='미향')