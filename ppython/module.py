# 파이썬에서의 모듈 == xxx.py 파일을 의미
# 패키지는 xxx.py 파일들이 담긴 폴더를 의미
# 모듈과 패키지를 임포트하는 방법은 동일하다. ==> from X import A, B
# 그런데 모듈을 임포트하면 해당 파일이 실행됨
# 그래서 if __name__ == '__main__': 
#           main()
# 구문을 이용해서 자체적으로 실행될 때만 main 함수가 실행되도록 한다.
#  __name__ ? >> 파이썬의 내장변수로 실행되는 모듈의 이름이 저장되어 있는데 자체적으로 실행되는 파일일 경우
#                __main__ 이란 값을 저장한다.
#                그런데 다른 파일에서 임포트되어 사용되는 경우 임포트된 파일에서 해당 값을 출력하면 클래스파일 명이 담겨있다.


