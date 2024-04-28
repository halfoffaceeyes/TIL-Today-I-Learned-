# API - Application Programming Interface
* 두 소프트웨어가 서로 통신할 수 있게 하는 메커니즘
* 클라이언트-서버처럼 서로 다른 프로그램에서 요청과 응답을 받을 수 있도록 만든 체계

## API 예시
![API 예시](<../이미지/240411/API 예시.PNG>)
* 기상 데이터가 들어있는 기상청의 시스템
* 스마트 폰의 날씨 앱, 웹 사이트의 날씨 정보 등 다양한 서비스들이 이 기상청 시스템으로부터 데이터를 요청해서 받아 감
* 날씨 데이터를 얻기 위해서 - 기상청 시스템에는 정보들을 요청하여 지정된 형식이 있기 때문에 메뉴얼을 통해 필요한 정보를 요청해야함
* 소프트웨어와 소프트웨어 간 지정된 형식으로 소통하는 수단
* 스마트 폰의 날씨 앱은 기상청에서 제공하는 API를 통해 기상청 시스템과 대화하여 매일 최신 날씨 정보를 표시할 수 있음

## API 역할
* 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇가지 더 쉬운 구문을 제공
### Web API
* 웹 서버 또는 웹 브라우저를 위한 API
* 현대 웹 개발은 하나부터 열까지 직접 개발하기보다 여러 Open API들을 활용하는 추세
* 대표적인 Third Party Open API 서비스 목록
    - Youtube API
    - Google Map API
    - Naver Papago API
    - Kakao Map API

## REST - Representational State Transfer
* API Server를 개발하기 위한 일종의 소프트웨어 설계 '방법론'
* 모두가 API Server를 설계하는 구조가 다르니 방법을 제시 == 규칙이 아님

### RESTful API
* REST 원리를 따르는 시스템을 RESTful하다고 부름
* '자원(데이터)을 정의'하고 '자원(데이터)에 대한 주소를 지정'하는 전반적인 방법을 서술한 형태를 뜻함
* 각각의 API 서버 구조를 작성하는 모습이 너무 다르니 어느정도 약속을 만들어서 다같이 API 서버를 구성하기 위함

### REST API
* REST라는 설계 디자인 약속을 지켜 구현한 API
* 활용예시

![REST API 활용 예시](<../이미지/240411/REST API 활용 예시.PNG>)

#### REST에서 자원을 사용하는 법 3가지
1. 자원의 '식별' == 위치 : URL
2. 자원의 '행위' == 행동(CRUD) : HTTP Methods
3. 자원의 '표현' == 응답데이터 : JSON 데이터, 궁극적으로 표현되는 데이터 결과물

행위 + URI로 요청하면 서버는 JSON으로 응답

# 자원의 식별
## URI - Uniform Resource Identifier(통합자원 식별자)
* 인터넷에서 리소스(자원)를 식별하는 문자열
* URL의 상위 개념
* 가장 일반적인 URI는 웹 주소로 알려진 URL

### URL - Uniform Resource Locator(통합 자원 위치)
* 웹에서 주어진 리소스의 주소
* 네트워크 상에 리소스가 어디있는지를 알려주기 위한 약속

![URL](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240411/URL.PNG)

### Schema(or Protocol)
* 브라우저가 리소스를 요청하는 데 사용해야 하는 규약
* URL의 첫 부분은 브라우저가 어떤 규약을 사용하는지를 나타냄
* 기본적으로 웹은 http(s)를 요구하며 메일을 열기 위한 mailto:, 파일을 전송하기 위한 ftp: 등 다른 프로토콜도 존재

![schema](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240411/schema.PNG)

### Domain Name
* 요청 중인 웹 서버를 나타냄
* 어떤 웹 서버가 요구되는 지를 가리키며 직접 IP주소를 사용하는 것도 가능하지만, 사람이 외우기 어렵기 때문에 주로 Domain Name으로 사용(실제 주소는 IP 주소)
* 예를 들어 도메인 google.com의 IP 주소는 142.251.42.142

![Domain Name](<../이미지/240411/Domain Name.PNG>)

### Port
* 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문(Gate)
* HTTP 프로토콜의 표준 포트
    - HTTP - 80
        * 80포트예시 : django 80포트의 00번
    - HTTPS - 443
* 표준 포트만 작성 시 *생략 가능*

![Port](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240411/Port.PNG)

### Path
* 웹 서버의 리소스 경로
* 초기에는 실제 파일이 위치한 물리적 위치를 나타냈지만, 오늘날은 실제 위치가 아닌 추상화된 형태의 구조를 표현
* 예를 들어 /articles/create/라는 주소가 실제 articles/폴더 안에 create폴더안을 나타내는 것은 아님

![path](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240411/path.PNG)


### Parameters
* 웹 서버에 제공하는 추가적인 데이터
* URL로 전달되는 데이터(GET으로 데이터를 전달한 경우)
* '&' 기호로 구분되는 key-value 쌍 목록
* 서버는 리소스를 응답하기 전에 이러한 파라미터를 사용하여 추가 작업을 수행할 수 있음
* 서버에서 받아올 때도, get으로 가져와야함

![parameter](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240411/parameter.PNG)

### Anchor
* 일종의 '북마크'를 나타내며 브라우저에 해당 지점에 있는 콘텐츠를 표시
* fragment identifier(부분 식별자)라고 부르는 '#' 이후 부분은 서버에 전송되지 않음
* 엥커가 없으면 문서의 첫시작점부터 시작
* 설정한 ID의 위치로 이동시켜주는것(\<a href ='#ID명'>)
* 서버에서 받는 데이터가 아님 브라우저에서 해결하는 데이터
* https://docs.djangoproject.com/en/4.2/intro/install/#quick-install-guide
* 요청에서 #quick-install-guide는 서버에 전달되지 않고 브라우저에게 해당 지점으로 이동할 수 있도록 함

![anchor](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240411/anchor.PNG)

# 자원의 행위

## HTTP Request Methods
* 리소스에 대한 행위(수행하고자 하는 동작)를 정의
* HTTP verbs라고도 함
### 대표 HTTP Request Methods
1. GET
    - 서버에 리소스의 표현을 요청(조회에서만 사용)
    - GET을 사용하는 요청은 데이터만 검색해야 함
2. POST
    - 데이터를 지정된 리소스에 제출
    - 서버의 상태를 변경
    - Create에서만 사용
3. PUT
    - 요청한 주소의 리소스를 수정
4. DELETE
    - 지정된 리소스를 삭제

### HTTP response status codes
* 특정 HTTP 요청이 성공적으로 완료되었는지 여부를 나타냄
* 5개의 응답 그룹
    * Inforamtional responses(100-199)
    * Succuessful responses(200-299) : 정상적 응답
    * Redirection responses(300-399) : 리다이렉트 관련 응답
    * Client error responses(400-499) : 사용자 잘못, 요청이 잘못됨
    * Server error responses(500-599) : 서버 잘못

* 100~300번대 정상적 작동 관련응답, 400~500번대 에러관련 응답

# 자원의 표현
* 지금까지 Django 서버는 사용자에게 페이지(html)만 응답하고 있었음
* 하지만 그서버가 응답할 수 있는 것은 페이지 뿐만 아니라 다양한 데이터 타입을 응답할 수 있음
* REST API는 이 중에서도 JSON 타입으로 응답하는 것을 권장(String 형태의 딕셔너리)
* 페이지(html)만을 응답했던 서버 -> JSON데이터를 응답하는 REST API 서버로의 변환
* 변환되면서 Django는 더 이상 Template 부분에 대한 역할을 담당하지 않게 되며, 본격적으로 Front-end와 Back-end가 분리되어 구성 됨
* 이제부터 Django를 사용해 RESTful API 서버를 구축할 것(data만 전달하는 형태)

![RESTfulAPI](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240411/RESTAPI.PNG)

# DRF with Single Model
* data를 주고 받는것을 확인해보기
    * python으로 json응답받기

    ![python으로 json응답받기](<../이미지/240411/python으로 json 응답받기.PNG>)

## DRF = Django REST Framework
* Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
    * DRF는 설치 후 installed_apps에 등록도 해주어야함

![DRF설치](<../이미지/240411/DRF 설치.PNG>)

## Postman 설치 및 안내
* Postman 설치
    - https://www.postman.com/downloads/
* Postman이란?
    * API를 구축하고 사용하기 위한 플랫폼
    * API를 빠르게 만들 수 있는 여러 도구 및 기능을 제공
    * GET은 params에, POST는 HTTP의 BODY에 보내는 폼데이터로 구성

![Postman화면 구성](<../이미지/240411/Postman 화면 구성.PNG>)

![URL과 HTTP requests method 설계](<../이미지/240411/URL과 HTTP requests method 설계.PNG>)

## GET - list
### serializers.py 작성
* 게시글 데이터 목록 조회하기
* 게시글 데이터 목록을 제공하는 ArticleListSerializer 정의
* serializers.py의 위치나 파일명은 자유롭게 작성 가능
* ModelForm과 작성방법은 거의 동일

#### Serialization 직렬화
* 여러시스템에서 활용하기 위해 데이터 구조나 객체 상태를 *나중에 재구성할 수 있는 포맷으로 변환*하는 과정
* django에서 작성한 데이터가 java나 python과 같은 데이터로 변환하여 사용할 수 있도록 도와주는 과정
* 어떠한 언어나 환경에서도 나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정

![serialization](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240411/serialization.PNG)

#### Serializer
* Serialization을 진행하여 Serialized data를 반환해주는 클래스
* database를 직접 수정하지 않고 전환하여 반환
* 하나의 클래스에 데이터를 모아서 반환하기 위해 class로 작성
* DRF 이용자는 django의 사용자이므로 외부 라이브러리이지만 django 문법과 비슷하게 설계되어 있음

##### ModelSerializer
* Django 모델과 연결된 Serializer 클래스
* 일반 Serializer와 달리 사용자 입력 데이터를 받아 자동으로 모델 필드에 맞추어 Serialization을 진행


![serializer](<../이미지/240411/GET List.PNG>)

### url 및 view 함수 작성
* redirect할 일 이 거의 없으므로 appname과 name을 생략함
* Response : 응답을 전달할 함수

    ![GET List2](<../이미지/240411/GET List2.PNG>)
    * 여기서 정의된 serializer가 결국 serialized data를 의미함(serialization과정 참고)

* 응답 확인

    ![응답 확인](<../이미지/240411/GET List3.PNG>)

* ModelSerializer의 인자 및 속성
    * many 옵션
        - Serialize 대상이 QuerySet인 경우 입력
        - 생략하면 Queryset인 경우 에러가 발생함
    * data 속성
        - Serialized data 객체에서 실제 데이터를 추출

#### 과거 view 함수와의 비교
* 똑같은 데이터를 HTML에 출력되도록 페이지와 함께 응답했던 과거의 view 함수, JSON 데이터로 serialization하여 페이지 없이 응답하는 현재의 view 함수
* 과거 view함수

    ![과거 view함수](<../이미지/240411/view함수 과거.PNG>)
* 현재 view함수

    ![현재 view함수](<../이미지/240411/view함수 현재.PNG>)

#### 'api_view' decorator
* DRF view 함수에서는 필수로 작성되며 view함수를 실행하기 전 HTTP 메서드를 확인, 작성된 메서드만 허용
* 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답
* DRF view 함수가 응답해야하는 HTTP 메서드 목록을 작성

## GET- Detail
* 단일 게시글 데이터 조회하기
    - 각 게시글의 상세 정보를 제공하는 ArticleSerializer 정의

    ![GET Detail](<../이미지/240411/GET Detail.PNG>)

### url 및 view 함수 작성
![get detail url 작성](<../이미지/240411/GET Detail2.PNG>)

* 응답확인

    ![get detail 응답 확인](<../이미지/240411/detail 응답확인.PNG>)

## POST
* 게시글 데이터 생성하기
1. 데이터 생성이 성공했을 경우 201 Created 응답
2. 데이터 생성이 실패했을 경우 400 Bad request 응답

### view함수 구조 변경
* Method에 따른 분기 처리

    ![POST 구조 변경](<../이미지/240411/POST 요청.PNG>)

    * Modelserializer의 첫 인자는 이므로 data=를 적어주어야함

    * modelform과 헷갈리지 않기 위해 DRF에서 is_valid()함수와 save()함수의 이름을 똑같이 제공 실제로는 다른 기능
    * serializer.errors는 실패했을 경우에만 error객체가 형성됨

    * status == 응답 코드를 정리해놓은 모듈

* http://127.0.0.1:8000/api/v1/articles/ 응답확인
    * **데이터 추가시 body에서 데이터를 작성한 후 POST 요청으로 SEND하면 데이터가 생성됨**
    * 응답확인할 경우에는 항상 HTTP codes를 같이 확인할 것!

    ![POST 응답확인](<../이미지/240411/POST 응답.PNG>)
* 새로운 데이터확인은 GET 요청으로 진행

    ![POST 새로운데이터 확인](<../이미지/240411/POST 새데이터.PNG>)


## DELETE
* 게시글 데이터 삭제하기
    - 요청에 대한 데이터 삭제가 성공했을 경우는 204 No content 응답

    ![DELETE view함수](<../이미지/240411/DELETE view함수.PNG>)
* 응답확인

    ![Delete 응답 확인](<../이미지/240411/DELETE 응답확인.PNG>)

## PUT
* 게시글 데이터 수정하기
    * 요청에 대한 데이터 수정이 성공했을 경우는 200 OK 응답
    * partial =True , 부분수정을 위한 인자

    ![PUT view 함수](<../이미지/240411/PUT view 함수.PNG>)

    ![PUT 응답확인](<../이미지/240411/PUT 응답확인.PNG>)
    
    ![PUT 수정 데이터 확인](<../이미지/240411/PUT 데이터확인.PNG>)

### 'partial' argument
* 부분 업데이트를 허용하기 위한 인자
* 예를 들어 partial 인자 값이 False일 경우 게시글 title만을 수정하려고 해도 반드시 content 값도 요청시 함께 전송해야 함
* 기본적으로 serializer는 모든 필수 필드에 대한 값을 전달 받기 때문
    * 즉, 수정하지 않는 다른 필드 데이터도 모두 전송해야 하며 그렇지 않으면 유효성 검사에서 오류가 발생
    
![partial argument](<../이미지/240411/partial argument.PNG>)

# 참고
## raise_exception
* is_valid()의 선택인자
* 유효성 검사를 통과하지 못할 경우 ValidationError 예외를 발생시킴
* DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답을 반환

    ![raise_exception](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240411/raise_exception.PNG)