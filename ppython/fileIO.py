# 키보드 I/O
# input() 함수를 사용한다. 해당 값의 리턴 값은 무조건 str이다.
def ticket_amt_calc():
    # bool은 값의 존재여부 가지고 판단해서 적합하지 않음
    # isAdult:bool = bool(input("어른입니까?"))
    person_cnt:int = int(input("몇 명입니까?"))
    return 10000 * person_cnt


#print(ticket_amt_calc())

## 파이선에는 switch-case문이 없다. 그 이유는 필요없다고 생각해서인데, 파이썬 3.10 버전 이후부터
## match-case 가 새로 생겼다. > 사용법은 완전히 동일
## >> 필요 없다고 한 이유 : 1. ifelse 문을 사용 2. 딕셔너리를 사용해서 value에 람다식 넣기 3. 함수의 메소드를 케이스 별로 만들어서 사용하기
## 이 중에서 2번이 기존 스위치문과 행위가 유사

## 2.딕셔너리 사용 예시
calc_dict = {
    '+' : lambda x,y: x+y,
    '-' : lambda x,y: x-y,
    '*' : lambda x,y: x*y,
    '^' : lambda x,y: x**y
}

print(calc_dict.get('^')(3,5))


## 파이썬에서의 시퀀스 : 문자열, 리스트, 튜플을 의미합니다.

## 비교할 케이스가 많을 때, 성능 switch > ifelse 인 이유는??
'''
사실 케이스마다 다르긴 함
비교 케이스가 많으면 스위치문이 유리할 수 있는데
거의 대부분의 경우가 첫번째 케이스에서 조건을 만족해서 처리된다면 ifelse가 유리할 수 있다
물론 스위치문은 키워드 일치 조건일 경우에만 사용이 가능하다.

스위치문이 성능상 더 유리하다고 하는 이유는,
만약 케이스문의 세번째에 위치하는 조건문을 만족하는 경우가 있다고 하자.
스위치문은 컴파일시의 jump table의 형태로 컴파일 되는데, 
이는 case를 key로 하고 실행할 작업을 value로 갖는 자료구조를 의미한다.
그래서 로직에서 1번 조건부터 순차적으로 비교하지 않고 바로 case에 해당하는 처리로직을 점프해서 한 번에 갈 수 있다.
그러나 if-else문은 세번째까지의 비교문을 전부 비교하고 나서야 처리로직에 도달할 수 있어서 그렇다.
'''



## 파이썬 람다식 사용해보기
## 파이썬 3부터는 표현식이 적용된 리스트를 받기 위해서 list()로 감싸주어야 한다

#square 하기
square_list = list(map(lambda x: x**2, range(5)))
print(square_list)

#인원수 누적하기
people = ['윌슨', '남영', '도라지', '집', '언제', '가', '?']
from functools import reduce
##func1 = lambda x,y : 1+1
##p_cnt = reduce(func1, people) >> 이거 안대..누적이
##print(p_cnt)

##print('윌슨'.reverse()) >> 문자열은 리버스 없움
name = list('윌슨')
print(name)
name.reverse() ## 이거 return 값이 없음. 원본 데이터를 reverse함 > 메모리 사용량이 가장 작음
print(name) 

name2 = list('남영')
new_name = list(reversed(name2)) ## list에 속하지 않은 reversed는 return 값이 있으나 이터레이터이다. 그래서 list()로 변환이 필요하다
## 얘는 신규 리스트를 생성해주는 것
print(new_name)
print(name2) ## 원본 그대로 유지



#### 파일 I/O
### with 구문을 사용하면 close()가 자동이다
### r/w/a = 읽기/쓰기/이어서쓰기
with open('first.txt', 'w', encoding='UTF-8') as f1:
    f1.write('하잉')
    f1.write('처음이야!\n')
    f1.write('오늘은 모델이 말썽이야..흑흑')

with open('first.txt', 'r', encoding='UTF-8') as f2:
    for line in f2:
        print(line, end='') ##print의 end필드를 빈 값으로 하면 이상한 줄띄움이 없어짐
    

with open('first.txt', 'w', encoding='UTF-8') as f3:
    f3.write('만약  \n')
    f3.write('다시  \n')
    f3.write('write를 한다면?')


with open('first.txt', 'a', encoding='UTF-8') as f4:
    f4.write('\n 이어쓰기가 된다!!!!!')

