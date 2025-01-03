print('Hahahahaha')
#작은 따옴표와 큰 따옴표 차이
# 몫 : //, 거듭제곱 : **
# not : 반전 ==> !

# in도 연산자에 호홍
print('c' in 'cat')
print('c' not in 'cat')

#bool(xxx) > xxx에 값이 있는지 없는지 
# '', 0, None 은 빈 값으로 판단

'''
여러줄 주석?
'''
print(len('qqqqqqqqqq'))

longStr = '''sdfdf
sfdsf
sdfdsfs
sdfs'''

print(len(longStr))

letter = 'how are You?'
print(letter.lower())
print(letter.upper())
print(letter.capitalize())
print(letter.swapcase())
print(letter.title())
print(letter.split())
print(letter.count('You'))
print(letter.center(16, '*'))

apple = '사과'
banana = '바나나'
fruit_format = '{0} 랑 {1} 주세요.'

print(fruit_format.format(apple, banana))
print(f'{banana} + {apple} = 주황')

#얘네 하나의 리스트에 여러 타입의 값을 넣을 수 있음.. > 이렇게 안 쓸거임
# 리스트 조작 == 문자열 조작
# 리스트 append 메소드는 무조건 맨 마지막에 삽입하는거 같고, remove는 값을 기준으로 삭제하기 때문에 성능에 안 좋을 거 같음
# 그래서 인덱스를 알고있다면 pop을 사용하고, 다른 인덱스 위치에 넣고 싶으면 insert 사용
alist = [1,'a','A',False]

#   ()로 감싸면 튜플인데 unmodifiable list임
btuple = ('a',1,'b','Q') # 튜플 선언 ==> 패킹이라고 함
# 만든 튜플을 다시 나눠서 저장하는 것을 언패킹이라고 함
(one, *other, q) = btuple
print(one)
print(other) #나머지를 저장할 경우 튜플이 아닌 리스트로 저장이 된다 ****
print(q)


# set > 자바랑 비슷함 > 중복 안돼고 순서 없음
# 리스트 >> 중복되고 순서있음
# 리스트랑 튜플은 인덱스 사용이 가능한데 셋은 순서가 없어서 인덱스 사용이 안됌 > 단순 추가, 삭제만 가능함

#del list, del tuple, del set 은 변수 자체를 삭제함 > None == null
# .clear()는 변수는 존재하는데 내용을 비우는 거

#set은 집합 연산에 주로 사용하는 것으로 보임
my = {'치즈닭갈비'}
friend = {'파스타', '치즈닭갈비', '삼겹살', '마라탕', '뇨끼'}

print(my.intersection(friend))
print(my.union(friend))
print(my.isdisjoint(friend))
print(friend.issuperset(my)) #superset > param으로 돌아오는 셋을 포함하는 건지 ( 엄마 셋..? )
print(my.difference(friend))
print(my.difference_update(friend))
print(my.update(friend))


#my[1], my[3] = '감자탕' >> 불가능

#딕셔너리 == 맵, key 중복 안됌
_who1 = {
    '이름' : '박나리',
    '나이' : 7,
    '성별' : '여',
    '키' : 97
}

# 존재하지 않는 키로 접근 시 에러가 발생하나, get 메소드를 사용하면 에러 발생하지 않고 None을 리턴
print(_who1.get('별명'))
#print(_who1['별명'])

#여러 키의 값을 한 번에 바꿀 수 있음
_who1.update({'나이':9, '키':105})
print(_who1)
print(_who1.pop('키'))
print(_who1)
#_who1.keys(), _who1.values()m _who1.items()

print(_who1.setdefault('메롱', '매롱롱ㅇ')) #딕셔너리에 첫번째 인자에 해당하는 키에 대한 값이 없으면, 두번쨰 인자의 값을 리턴해라
print(_who1.setdefault('나이', 0))
print(_who1.fromkeys("1")) #엥 신기해 근데 키의 길이가 1인거 밖에 안됌 > char
print(_who1.fromkeys('음', '이것도')) #ㅋㅋㅋㅋ뭐야이게

#자료형 변환 >> 컬렉션끼리 변환
#1. 튜플에 값 수정하기
my_tuple = ('A', "B", "AB")
my_list = list(my_tuple)
my_list.append("O")
my_tuple = tuple(my_list)
print(my_tuple)

#2. 리스트에 중복제거, 순서보장하지 않고
my_list = ['초코파이', '몽쉘', '몽쉘', '몽쉘', '바나니킥', '초코파이']
my_set1 = set(my_list)
my_set2 = set(my_list)
my_set3 = set(my_list)
print(my_set1)
print(my_set2)
print(my_set3)

#3. 순서를 보장하고 중복을 제거해야 한다면 딕셔너리 사용
my_dict = dict.fromkeys(my_list) ##
print(my_dict)
my_list = list(my_dict)
print(my_list) # 딕셔너리의 키만 뽑아서 리스트로 만듬