##파이썬은 싱글스레드여서 에러가 발생하면 프로그램 자체가 멈추나??
### >> 싱글스레드면 그 스레드에서 에러가 발생하면 프로세스가 멈추는 건 맞음
### >>> 근데 보통 그렇게 안 쓰겠딩..
### >>> 1. 대안으로 멀티프로세스 + IPC로 사용 (ex. observer & subscriber)
### >>> 2. 실제 동작은 코어 하나만 사용하지만 스레드는 멀티스레드로 생성하는 경우 (ex. webapp)



##파이썬이 외부 모듈을 이용해 멀티스레드처럼 동작을 하려고 해도 안돼는 이유
'''
GC방식 때문이다.
cpython에서는 객체의 참조 횟수를 카운트해서 GC의 대상을 정하는데, 이때 정확한 값을 카운트하기 위해 인터프리터에서 GIL라는 것을 사용해
스레드를 제어한다. (Global Interpreter Lock)
인터프리터가 스레드에게 락을 획득과 해제를 해줌으로써 참조변수에 한 번에 하나의 스레드만 접근할 수 있도록 해준다.

그래서 I/O 발생(c호출)하거나 timesplice가 지나면 thread context switching을 하는 방식으로 다중스레드를 처리한다.

너무 많은 스레드의 개수는 많은 컨텍스트 스위칭을 유발하므로 성능에 좋지 않고
cpu 바운드보다 io 바운드에서 멀티스레드로 실행했을 때 속도가 더 향상될 수 있다. (***싱글스레드로 돌리기 전에 비해서임***)
'''



'''
memo )
일단 파이썬 자체는 멀티스레드 > 프로그램 실행하는 스레드 하나랑 가비지 컬럭터 역할을 하는 스레드 하나 > 2개
JVM에서 돌아가는 것 처럼 여러 CPU를 동시에 사용해서 찐 멀티 스레딩은 안돼고, 스레딩을 여러개 생성 가능하나 한 번에 하나의 CPU만 사용해서 처리됨
>> ?? 이건 아니다 ! 멀티 코어를 사용하긴 하는데 참고 객체 접근을 synchronized처럼 해야하는 거였음.
>> CPU 바운드 성능저하 
그 와중에 동시성을 위해 lock 매커니즘도 사용하긴 함> GIL > ..?? 삭제 된다는디 
>> GIL이 객체마다인지 스레드마다인지..?
>> 뮤텍스라고 했으니까 객체 아니까..?


파이썬은 멀티스레딩 < 멀티프로세싱 + IPC
event-driven에 효과적 > 처리 시간이 오래 걸리지 않는 

'''

print(__name__)
from cclass import One, Two ## 신기하다 import하면 해당 모듈에 존재하는 명령어들이 실행되는... >> 아..그래서 메인메소드로 호출하는구나..
one = One()
two = Two(2,99)

print(one)
print(two)




#파이썬에서 모든 에러의 부모 클래스는 Exception

#파이썬 try-catch
# try :
# except :
# else :  >> try 내 구문이 정상처리 되었을 때 실행
# finally :

try:
    result = 3 / '2'
    print(f'연산 결과는 {result}입니다.')
except ZeroDivisionError as err: 
    print('에러가 발생:', err)
except TypeError as err:
    print('에러가 발생:', err)
except Exception as err:
    print('에러가 발생:', err)

