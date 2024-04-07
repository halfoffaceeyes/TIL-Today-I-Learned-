# Authentication System
## Cookie & Session
### HTTP
HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 규약
> 웹(WWW)에서 이루어지는 모든 데이터 교환의 기초

* HTTP 특징
    * 비연결 지향(connectionless) : 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
        * 서버와 클라이언트가 지속적으로 연결되어 있지 않고 단순 요청과 응답의 형태로 구성
    * 무상태(stateless) : 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음

상태가 없다는 것 == 장바구니에 담은 상품을 유지할 수 없음, 로그인 상태를 유지할 수 없음, 상태를 유지하기 위한 기술이 필요

### 쿠키
* 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각 = 다음 요청을 위해 클라이언트에 저장
> 클라이언트 측에서 저장되는 작은 데이터 파일이며, 사용자 인증, 추적, 상태 유지 등에 사용되는 데이터 저장 방식

![Cookie](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240329/Cookie.PNG)
* 매 요청마다 상태를 제공(로그인 여부를 계속제공 == HTTP는 상태를 저장할 수 없기 때문에)

#### 쿠키 사용 원리
1. 브라우저(클라이언트)는 쿠키를 Key-Value의 데이터 형식으로 저장
2. 이렇게 쿠키를 저장해 놓았다가, 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송
- 쿠키는 두요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때, 주로 사용됨
    - 이를 이용해 사용자의 로그인 상태를 유지할 수 있음
    - 상태가 없는(stateless) HTTP 프로토콜에서 상태 정보를 기억시켜 주기 때문

* 쿠키는 상태를 저장하기 위해 사용하는 것!

#### 쿠키를 이용한 장바구니 예시
* 장바구니에 상품 담기
    * 개발자 도구- Network 탭 - cartView.pang 확인
    * 서버는 응답과 함께 Set-Cookie 응답 헤더(Response-Header)를 브라우저에게 전송
        - 이 헤더 중 Set-Cokie는 클라이언트에게 쿠키를 저장하라고 전달하는 것

![쿠키 이용예시](<../이미지/240329/쿠키 이용 예시.PNG>)
* 메인페이지 이동해도 장바구니 유지
* 만약 쿠키를 지운다면 장바구니가 사라짐

#### 쿠키 사용 목적
상태가 없는 HTTP에서 상태를 만들어준다!
1. 세션 관리(Session management)
- 로그인, 아이디 자동완성, 공지 하루 안보기, 팝업체크, 장바구니 등의 정보 관리
2. 개인화(Personalization)
- 사용자 선호ㅡ 테마 등의 설정
3. 트래킹(Tracking)
- 사용자 행동을 기록 및 분석

* 시크릿모드는 추적 쿠키를 저장하지 않는다는 것

### 세션
* 서버 측에서 생성되어 클라이언트와 서버간의 상태를 유지 상태 정보를 저장하는 데이터 저장 방식
- 쿠키에 세션 데이터를 저장하여 매 요청시마다 세션 데이터를 함께 보냄
- 쿠키 데이터 중 상태를 담당하는 데이터

#### 세션 작동 원리
1. 클라이언트가 로그인을 하면 서버가 session 데이터를 생성 후 저장
2. 생성된 session 데이터에 인증 할 수 있는 session id를 발급
3. 발급한 session id를 클라이언트에게 응답
4. 클라이언트는 응답 받은 session id를 쿠키에 저장
5. 클라이언트는 다시 동일한 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달
6. 쿠키는 요청 때마다 서버에 함께 전송 되므로 서버에서 session id를 확인해 로그인 되어있다는 것을 알도록 함

* 서버측에서는 세션 데이터를 생성 후 저장하고 이 데이터에 접근할 수 있는 세션 ID(key 역할)를 생성
* 이 ID를 클라이언트 측으로 전달하고, 클라이언트는 쿠키에 이 ID를 저장

* 이후 클라이언트가 같은 서버에 재요청 시마다 저장해 두었던 쿠키도 요청과 함께 전송
    * 예를 들어 로그인 상태 유지를 위해 로그인 되어 있다는 사실을 입증하는 데이터를 매 요청마다 계속해서 보내는 것

* 쿠키와 세션은 서버와 클라이언트 간의 '상태'를 유지하려는 목적으로 사용
* 로그아웃하면 세션 데이터를 제거

### 쿠키 종류별 Lifetime(수명)
* 서버에서 세션데이터는 기한을 둘 수 있음
1. Session cookie
- 현재 세션(current session)이 종료되면 삭제됨
- 브라우저 종료와 함께 세션이 삭제됨
2. Persistent cookies
- Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨
- 30분 지나면 자동 로그아웃

### 세션 in Django
* Django는 'database-backed sessions'저장 방식을 기본 값으로 사용
* session 정보는 DB의 django_session 테이블에 저장됨
* django는 요청안에 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session 데이터를 알아냄
* Django는 우리가 session 메커니즘(복잡한 동작원리)에 대부분을 생각하지 않게끔 많은 도움을 줌

# Authentication System
## Django Authentication System(인증 시스템)
사용자 인증과 관련된 기능을 모아 놓은 시스템
### Authentication
사용자가 자신이 누구인지 확인하는 것(신원 확인)

* 사전 준비
    * 두번째 app accounts 생성 및 등록
    * 두번째 app accounts 생성 및 등록
        * auth와 관련한 경로나 키워드들을 django 내부적으로 accounts라는 이름으로 사용하고 있기 때문에 되도록 'accounts'로 지정하는 것을 권장

## Custom User model
### User model 대체하기
* Custom User model로 대체하기
    * django가 기본적으로 제공하는 User model이 아닌 직접 작성한 User model을 사용하기 위해 

* User 클래스를 대체하는 이유
    * 우리는 지금까지 별도의 User 클래스 정의 없이 내장된 auth 앱에 작성된 User 클래스를 사용했음
    * 별도의 설정 없이 사용할 수 있어 간편하지만, 개발자가 직접 수정할 수 없는 문제가 존재(기존의 user클래스와 동일하게 변경 후 필요시 커스터마이징)

https://github.com/django/django/blob/main/django/contrib/auth/models.py#L406

![내장된 auth 앱](<../이미지/240329/내장된 auth app.PNG>)

#### 대체하기
* AbstractUser 클래스를 상속받는 커스텀 User 클래스 작성

* 기존 User클래스도 AbstactUser를 상속받기 때문에 이렇게 하면 커스텀 User클래스도 기존 User 클래스와 완전히 같은 모습을 가지게 됨(내장 User클래스 == Abstractuser)
![auth 대체하기1](<../이미지/240329/auth 대체1.PNG>)
* django 프로젝트가 사용하는 기본 User 모델을 우리가 작성한 User 모델로 지정(수정전 기본값 auth.User)
![auth 대체하기2](<../이미지/240329/auth 대체2.PNG>)
* admin site에 대체한 User 모델 등록
* 기본 User 모델이 아니기 때문에 등록하지 않으면 출력되지 않기 때문에
![auth 대체하기3](<../이미지/240329/auth 대체3.PNG>)

* AUTH_USER_MODEL
    - Django 프로젝트의 User를 나타내는 데 사용하는 모델을 지정
    - https://docs.djangoproject.com/en/4.2/ref/settings/#auth-user-model

* 프로젝트 중간에 AUTH_USER_MODEL을 변경할 수 없음
- 이미 프로젝트가 진행되고 있을 경우 데이터베이스 초기화 후 진행
![사용하는 User테이블의 변화](<../이미지/240329/사용하는 User 테이블의 변화.PNG>)

* 프로젝트를 시작하며 반드시 User 모델을 대체해야한다.
    * 필요없어도 진행하는 것을 권장(나중에 필요한 경우를 위해서)
    * Django는 새 프로젝트를 시작하는 경우(기본 User 모델이 충분하더라도) 커스텀 User모델을 설정하는 것을 강력하게 권장하고 있음
    * 커스텀 User 모델은 기본 User 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문
    * 단, User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함

### 데이터 베이스 초기화 방법
1. migrations 안의 설계도만 지우고
2. DB를 지워주면 됨(db.sqlite를 제거)

# Login
* Session을 Create하는 과정

* AuthenticationForm()
    * 로그인 인증에 사용할 데이터를 입력 받는 built-in form(받은 데이터를 DB에 저장하지 않기 위해서 form 사용 <-> ModelForm은 DB에 저장을 함)
    * 로그인 정보 (id/password)는 인증에만 필요하기 때문에 built-in-form 을 사용

## 로그인 페이지 작성
==create와 동일한 과정
![로그인 페이지 작성](<../이미지/240329/로그인 페이지 작성.PNG>)
![로그인 페이지 작성2](<../이미지/240329/로그인 페이지 작성 2.PNG>)

* AuthenticationForm은 ModelForm이 아니라 일반 Form이기 때문에 첫번째인자로 data(request.POST)가 아닌 request를 먼저 받음
![로그인 로직 작성](<../이미지/240329/로그인 로직 작성.PNG>)

* login(request,user)
    * AuthenticationForm을 통해 인증된 사용자를 로그인 하는 함수
* get_user()
    * AuthenticationForm의 인스턴스 메서드
    * **유효성 검사를 통과했을 경우** 로그인 한 사용자 객체를 반환


### 로그인이 됐는지 확인하는 방법
1. 로그인 후 발급받은 세션 확인 
* DB에서 session(django_session)이 만들어져 있는지 확인
![세션데이터확인](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240329/%EC%84%B8%EC%85%98%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%99%95%EC%9D%B81.PNG)

2. 브라우저에서 확인
* 개발자도구 - Application - Cookies

![세션데이터확인2](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240329/%EC%84%B8%EC%85%98%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%99%95%EC%9D%B82.PNG)

![로그인 링크 작성](<../이미지/240329/로그인 링크 작성.PNG>)

# Logout
* Session을 Delete하는 과정

## logout(request)
* 현재 요청에 대한 Session Data를 DB에서 삭제하는 함수
* 클라이언트의 쿠키에서도 Session Id를 삭제

![로그아웃 로직 작성](<../이미지/240329/로그아웃 로직 작성.PNG>)

![로그아웃 결과](<../이미지/240329/로그아웃 페이지.PNG>)
* 로그아웃을 하면 쿠키에서 session ID가 삭제되고 DB에서도 session ID가 삭제됨

# Template with Authentication data
* 템플릿과 인증 데이터를 출력하는 방법

## 현재 로그인 되어 있는 유저 정보를 출력하기
* user라는 context데이터를 사용할 수 있는 이유는?
django가 미리 준비한 context데이터가 존재하기 때문(context processors에서 auth관련 context==settings.py의 templates의 option에서 확인가능)

![현재 로그인된 유저정보 출력](<../이미지/240329/현재 로그인된 유저정보 출력.PNG>)

* context processors
    * 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
    * 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함됨
    * django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드해 둔것

![context processor](<../이미지/240329/context processor.PNG>)

* 내부적으로 비로그인 유저 클래스가 존재 == AnonymousUser
    * AnonymousUser.username = None 값

# 참고
## github 코드 참고
* AuthenticationForm()
    - https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L286 
* AuthenticationForm()의 get_user() 인스턴스 메서드
    - https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L356 

## User 모델 상속 관계
![user모델 상속관계](<../이미지/240329/userModel 상속.PNG>)

### 'AbstarctUser' class
"관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본 클래스"
* 실제로 존재하지 않는 클래스

* Abstract base classes(추상 기본 클래스)
    * 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스(도장같은 역할, 기본기능만 제공하는 클래스)
    * 데이터베이스 테이블을 만드는 데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가 됨
    * https://docs.python.org/3/library/abc.html
    
* User모델 대체하기 Tip
    * User 모델을 대체하는 순서를 숙지하기 어려울 경우 해당 공식 문서를 보며 순서대로 진행하는 것을 권장
    * https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model