## 파이썬도 메이븐처럼 공용폴더에 설치된 라이브러리들이 존재한다. > pip install을 통한 패키지들

## 공용폴더랑 별개로 프로젝트 별로 가상환경을 구축해서 프로젝트 전용 라이브러리 환경을 구성할 수 있다
'''
--> python3 -m venv [가상환경이름] ( -m 은 사용할 모듈 이름 (venv)) 
프로젝트 폴더에 가상환경이름으로 가상환경과 관련된 폴더가 생성된다. 
--> 가상환경을 구성한 뒤 active를 해주어야 한다. source [가상환경이름]/bin/active
여기서 아무 패키지도 설치하지 않은 채 pip3 list를 하면 파이썬 기본 패키지만 나온다 ( => 공용영역에 있는 라이브러리가 보이지 않는다./사용할 수 없다.)
이때 vscode에도 해당 환경을 적용하기 위해서는 인터프리터를 변경해주어야 한다. 
'''


## Q. 왜 별도의 가상환경을 구축해서 작업해야할까?
'''
다수의 프로젝트를 하나의 PC에서 작업할 경우, 패키지들의 버전이 서로 호환이 되지 않는 경우가 존재하기 때문이다.
달라진 패키지 버전이 기존 프로젝트에 영향을 줄 수 있다.
'''

## Q. 파이썬의 공용 패키지를 공통으로 사용하고 임의의 프로젝트에 특정 패키지를 적용하고 싶은 경우에는 어떻게 하나?
'''
모듈을 통해 가상환경을 생성할 때, 옵션을 하나 더 주면 된다.
python3 -m venv [가상환경이름] --system-site-packages
이상태에서 activate 후에 pip3 list를 하면 공용공간에 있는 패키지가 모두 들어있다. 물론 이후 새로운 패키지를 설치해도 공용 공간에는 영향을 주지 않는다.
'''

## Q. 가상환경을 다시 active 취소하고 싶을 경우는 어떻게 하나?
'''
terminal에서 deactive 라고 명령어를 치면 된다. 
그리고 vscode에서 인터프리터를 기본 파이썬 인터프리터로 변경해주면 된다.
'''

## Q. 동료의 개발환경에 내가 가진 패키지 목록을 한 번에 세팅해줄 수 있는 방법은?
'''
pip3 freeze > requirement.txt 로 현재 내 개발환경에서 사용 중인 패키지 목록을 txt파일로 추출한다.
그리고 pip3 install -r requirement.txt 로 한 번에 파일 내 정의된 패키지를 설치할 수 있다.
'''