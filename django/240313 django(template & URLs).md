# Template System
## Django Template system
* 데이터 표현을 제어하면서, 표현과 관련된 부분을 담당
* HTML의 콘텐츠를 변수값에 따라 바꾸고 싶다면?
* render의 3번째인자에 딕셔너리 형태의 데이터를 넘겨주어야함
* 이 때, 값 표현은 {{}}로 표기
* ![HTML변수설정](<../이미지/240313/HTML콘텐츠 변수설정.PNG>)

## Django Template Language(DTL)
* Template에서 조건, 반복, 변수 등의 프로그래밍 적 기능을 제공하는 시스템
* HTML 쓸때 DTL 문법을 주석처리해도 작동하기 때문에 주석처리시 조심
* DTL Syntax
  * template에서는 과도한 로직을 사용 지양(html에서 로직을 사용시 파이썬==django가 연산을 하고 다시 가져와서 연결하는 구조여서 속도가 느림, 구조를 갖추는 정도만 사용할 것, 알고리즘과 같은 계산은 파이썬(django)에서 진행)
  * Variable
    * render 함수의 세번째 인자로 딕셔너리 데이터를 사용
    * 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
    * **dot('.')를 사용하여 변수 속성**에 접근할 수 있음
    * {{variable}
    * {{variable.attribute}}}
    * ex) list: arr[0]== arr.0, dict : dict.'a'
  * Filters
    * 표시할 변수를 수정할 때 사용(변수 + '|'+ 필터)
    * chained(연결)이 가능하며 일부 필터는 인자를 받기도 함
    * 60개의 built-in template filters를 제공
    * {{variable|filter}}
    * {{name|trincatewords:30}}
    * filter 사용시 == 앞뒤의 띄어쓰기 주의, variable|filter사이에는 띄어쓰기 없음
  * Tags
    * 반복 또는 논리를 수행하여 제어 흐름을 만듦
    * 일부 태그는 시작과 종료 태그가 필요
    * 약 24개의 built-in template tags를 제공
    * {% tag %}
    * {% if %}{% endif %}
  * Comments
    * DTL에서 주석
    * \<h1>Hello,{#name#}\</h1>
    * {%comment%}<br>
        ... <br>
     {%endcomment%}

### DTL 예시
![DTL 예시](<../이미지/240313/DTL 예시.PNG>)

![DTL 예시 코드](<../이미지/240313/DTL 예시 코드.PNG>)


* Django 공식 문서를 검색할 때, google에 django documment+ 공식 문서 내용로 검색
* 공식문서내에서는 목차의 대주제를 확인해서 필요한 내용만 읽어보는 연습을 할 것

# 템플릿 상속
* 기본 템플릿 구조의 한계
  * 만약 모든 템플릿에 bootstrap을 적용하려면?=템플릿 상속을 사용하면 일일이 bootstrap CDN을 작성안해도 상관 없음
* 템플릿 상속이란
  * 페이지의 공통요소를 포함하고, 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 'skeleton' 템플릿을 작성하여 상속 구조를 구축
## 상속 구조 만들기
* skeleton 역할을 하게되는 상위 템플릿을 작성
  * bootstrap CDN코드에 block이라는 영역을 만듦

![상속구조만들기1](<../이미지/240313/상속구조 만들기1.PNG>)
![상속구조만들기2](<../이미지/240313/상속구조 만들기2.PNG>)

* 'extends' tag
  * 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림
  * 반드시 자식 템플릿 최상단에 작성되어야 함(2개이상 사용 불가)
* 'block' tag
  * 하위템플릿에서 재정의 할 수 있는 블록을 정의
  * 상위 템플릿에 작성하며 하위 템플릿이 작성할 수 있는 공간을 지정하는 것
  
![block영역](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240313/block%EC%98%81%EC%97%AD.PNG)

# HTML form(요청과 응답)
* 데이터를 보내고 가져오기(Sending and Retrieving form data)
  * HTML 'form' element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기
  * HTML'form'은 HTTP 요청을 서버로 보내는 가장 편리한 방법
![form 예시](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240313/form%EC%98%88%EC%8B%9C.PNG)
![실제 Form 사용예시](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240313/%EC%8B%A4%EC%A0%9Cform%EC%98%88%EC%8B%9C.PNG)

## 'form' element
* 사용자로부터 할당된 데이터를 서버로 전송
* 웹에서 사용자 정보를 입력하는 여러방식(text,password,checkbox 등)을 제공

### fake Naver 실습

![fake naver](<../이미지/240313/fake naver.PNG>)

![fake naver2](<../이미지/240313/fake naver2.PNG>)

![fake naver3](<../이미지/240313/fake naver3.PNG>)
* 주소값을 보면 key=value 형태인 것을 알 수 있음

![fake naver4](<../이미지/240313/fake naver4.PNG>)

## 'action' & 'method'
* form의 핵심 속성 2가지
* 데이터를 어디(action)로 어떤 방식(method)으로 요청할지
* action
  * 입력데이터가 전송될 URL(목적지)
  * 만약 이속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
* method
  * 데이터를 어떤 방식으로 보낼것인지 정의
  * 데이터의 HTTP request methods(GET,POST)를 지정
* 'input' element
  * 사용자의 데이터를 입력 받을 수 있는 요소
  * type 속성 값에 따라 다양한 유형의 입력 데이터를 받음
* 'name' attribute
  * input의 핵심속성
  * 입력한 데이터에 붙이는 이름(key)
  * 데이터를 제출했을 때 서버는 name속성에 설정된 값을 통해서 사용자가 입력한 데이터에 접근할 수 있음
* Query String Parameters
  * 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보내는 방법
  * 문자열은 앰퍼샌드('&')로 연결된 key=value 쌍으로 구성되며, 기본 URL과는 물음표('?')로 구분됨
  * 예시
    * http://host:port/path?key=value&key=value
  
# form 활용
![활용예시 서버만들기](<../이미지/240313/사용자 입력데이러를 출력하는 서버만들기.PNG>)

![Throw작성](<../이미지/240313/throw 작성.PNG>)

![Throw 예시](<../이미지/240313/Throw 예시.PNG>)

![catch 작성](<../이미지/240313/catch 작성.PNG>)

* HTTP request 객체
  * form으로 전송한 데이터 뿐만 아니라 모든 요청 관련 데이터가 담겨 있음(view함수의 첫번째인자)

![request객체](<../이미지/240313/request객체 살펴보기.PNG>)

* form 데이터를 가져오는 방법 get method 활용(딕셔너리 형태의 데이터이기 때문)

![method활용해서 딕셔너리 데이터 가져오기](<../이미지/240313/form method.PNG>)

![catch 마무리](<../이미지/240313/catch 마무리.PNG>)

![catch 실행 결과](<../이미지/240313/catch 예시.PNG>)

# 참고
* 추가 템플릿 경로 지정
  * 템플릿 기본 경로 외 커스텀 경로 추가하기

![추가 템플릿 경로 지정](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240313/template%EA%B2%BD%EB%A1%9C%EC%A7%80%EC%A0%95.PNG)

![추가 템플릿 경로 지정2](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240313/template%EA%B2%BD%EB%A1%9C%EC%A7%80%EC%A0%952.PNG)
* BASE_DIR(manage.py의 부모 폴더)
  * settings에서 경로지정을 편하게 하기 위해 최상단 지점을 지정 해놓은 변수
  * 'DIRS' : [BASE_DIR / 'templates'(, 'templates2')]
  * 'DIRS': app 폴더 외부에서도 html 파일을 찾을 수 있도록 설정, 기본설정은 app 폴더에서 탐색, 딕셔너리 형태이므로 여러 형태를 콤마로 연결 가능(templates2처럼)
![basedir](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240313/BASE_DIR.PNG)

* 파이썬 문법의 객체 지향적인 경로 표기는 OS마다 다른 것을 알아서 변환해줌

* DTL 주의사항
  * python처럼 일부 프로그래밍 구조(if,for 등)를 사용할 수 있지만 명칭을 그렇게 설계했을 뿐 python 코드로 실행되는것이 아니며 python과는 관련 없음
  * 프로그래밍적 로직이 아니라 표현을 위한 것임을 명심하기
  * 프로그래밍적 로직은 되도록 view 함수에서 작성 및 처리할 것
  * 공식문서를 참고해 다양한 태그와 필터 사용해보기
    * http://docs.djangoproject.com/en/4.2/ref/templates/builtins/

# Django URLs
* 요청과 응답에서 Django URLs의 역할

![django의 역할](<../이미지/240313/django URL의 역할.PNG>)

* URL dispatcher
  * URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view함수를 연결(매핑)
## 변수와 URL
* 현재 URL 관리의 문제점
  * 템플릿의 많은 부분이 중복되고, URL의 일부만 변경되는 상황이라면 계속해서 비슷한 URL
* Varialbe Routing을 통해 해결 가능
### Variable Routing
* URL 일부에 변수를 포함시키는 것(변수는 view 함수의 인자로 전달할 수 있음)
* varibale routing 작성법: <>사용

![variable routing](<../이미지/240313/variable routing.PNG>)

* Path converters
  * URL 변수의 타입을 지정(str,int 등 5가지 타입 지원)
  * http://docs.djangoproject.com/en/4.2/topics/http/urls/#path-converters
  
* Variable routing 실습

![Variable routing 실습1](<../이미지/240313/variable routing 실습.PNG>)

![Variable routing 실습2](<../이미지/240313/variable routing 실습2.PNG>)

* Trailing Slashes
  * Django는 URL 끝에 '/'가 없다면 자동으로 붙임
  * "기술적인 측면에서, foo.com/bar와 foo.com/bar/는 서로 다른 URL"
    * 검색 엔진 로봇이나 웹트래픽 분석 도구에서는 이 두주소를 서로 다른 페이지로 보기 때문
  * 그래서 Django는 검색 엔진이 혼동하지 않게 하기 위해 무조건 붙이는 것을 선택한 것
  * 그러나 모든 프레임워크가 이렇게 동작하는 것은 아니니 주의