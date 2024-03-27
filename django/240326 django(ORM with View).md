url 흐름을 알고 있는 것이 MVC 패턴의 모든 플랫폼을 사용하는 데 도움이 됨.

# Read

* url을 통해 요청하고 db를 조회하고 db로 부터 나온 데이터를 받아서 다시 사용자에게 돌려주는 과정


1. 전체 게시글 조회

![전체 게시글 조회](<../이미지/240326/전체 게시글 조회.PNG>)

![전체 게시글](<../이미지/240326/전체 게시글 조회 예시.PNG>)

2. 단일 게시글 조회
* get메서드를 사용하기 위해서는 고유한 값을 갖는 키가 필요 == pk 
* 단일 데이터 조회를 할 경우에는 pk정보가 필요함
    - 주소에 변수가 있기 때문에 pk정보가 필요
    - variable routing을 이용해야함(공백으로 표기)
    
{%url "articles:detail" aritcle.pk %}

![단일 게시글 조회](<../이미지/240326/단일 게시글 조회.PNG>)

![단일 게시글](<../이미지/240326/단일 게시글 조회 예시.PNG>)

![단일 게시글 페이지 링크](<../이미지/240326/단일 게시글 페이지 링크 조회.PNG>)

![단일 게시클 페이지 링크 예시](<../이미지/240326/단일 게시글 페이지 링크 예시.PNG>)

요청 시점 == 시작 시점
링크 태그 만들고 urls.py 수정 -> views.py 수정 -> redirect

url tag 입력시 article.pk를 입력하지 않으면 No Reversed Match 발생

# Create
* Create 로직을 구현하기 위해 필요한 view 함수
    * new: 사용자 입력 데이터를 받을 페이지를 렌더링
    * create : 사용자가 입력한 데이터를 받아 DB에 저장

## new 기능 구현
![new 구현](<../이미지/240326/new 구현.PNG>)
* textarea tag는 input tag랑 비슷하지만 내용을 입력하기위해 조금더 넓은 공간을 제공함
* 데이터는 키-값 쌍으로 전송되므로 name을 입력해줌

![new 구현 예시](<../이미지/240326/new 구현 예시.PNG>)

* new 페이지로 이동할 수 있는 하이퍼링크 추가

![new 하이퍼 링크 추가](<../이미지/240326/new 구현 예시2.PNG>)

## create 구현
![create 구현](<../이미지/240326/create 구현.PNG>)
![create 구현2](<../이미지/240326/create 구현2.PNG>)
![create 구현 예시](<../이미지/240326/create 구현 예시.PNG>)


# HTTP request method
## HTTP
* 네트워크 상에서 데이터를 주고 받기 위한 약속
## HTTP request methods
* 데이터(리소스)에 어떤 요청(행동)을 원하는 지를 나타내는 것
> GET & POST
### GET Mehtod
* 특정 리소스를 조회하는 요청(데이터를 보여주는 식의 조회할 때만 사용)
* 데이터를 전달할 때 URL에서 Query String 형식으로 보내짐
    * ex) http://127.0.0.1:8000/articles/create/?title=제목&content=내용
### POST Method
* 특정 리소스에 변경(생성,수정,삭제)을 요구하는 요청
* 데이터는 전달할 때 HTTP Body에 담겨 보내짐 == 실제로 노출 되지 않음
* 이 과정은 DB를 수정하는 과정이라 보안이 중요함
    * CSRF Token이 반드시 필요

![POST 메서드 적용](<../이미지/240326/post 메서드 적용.PNG>)

* POST 메서드는 적용만 한다면 403 응답이 발생(CSRF Token이 없기 때문)

![403 예시](<../이미지/240326/403 응답.PNG>)

post 방식은 코드를 줌??

#### HTTP response status code
* 특정 HTTP 요청이 성공적으로 완료되었는지를 3자리 숫자로 표현하기로 약속한 것

* 400번대 client 잘못, 500번대 server잘못
* 403 Forbidden
    * 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미
    * 거절 이유 : CSRF token 누락
* 404 = page not found

* CSRF : Cross-Site-Request-Forgery
    * 사이트 간 요청 위조 : 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법=가짜사이트를 제공하여 해킹을 시도

* CSRF Token 적용
    * DTL의 csrf_token 태그를 사용해 손쉽게 사용자에게 토큰 값 부여 가능
    * 요청 시 토큰 값도 함께 서버로 전송될 수 있도록 하는 것

![csrf token](<../이미지/240326/csrf token 적용.PNG>)

* 요청시 CSRF Token을 함께 보내야 하는 이유
    * Django 서버는 해당 요청이 DB에 데이터를 하나 생성하는(DB에 영향을 주는) 요청에 대해 'Django가 직접 제공한 페이지에서 요청을 보낸것인지'에 대한 확인 수단이 필요한 것
    * 겉모습이 똑같은 위조 사이트나 정상적이지 않은 요청에 대한 방어 수단
* POST만 Token을 확인하는 이유?
    * POST는 단순 조회를 위한 GET과 달리 특정 리소스에 변경(생성,수정,삭제)을 요구하는 의미와 기술적인 부분을 가지고 있기 때문
    * DB에 조작을 가하는 요청은 반드시 인증 수단이 필요

    > 데이터베이스에 대한 병경사항을 만드는 요청이기 때문에 토큰을 사용해 최소한의 신원 확인을 하는 것

* 게시글 작성 결과
    * 게시글 생성 후 개발자 도구를 사용해 Form Data가 전송되는 것 확인
    * 더 이상 URL에 Query String 형태로 보냈던 데이터가 표기되지 않음
![게시글 작성결과](<../이미지/240326/게시글 작성 CSRF토큰.PNG>)

# Redirect
* 데이터 저장 후 페이지를 주는 것이 아닌 다른 페이지로 사용자를 보내야하는 경우에 사용
* 클라이언트가 인자에 작성된 주소로 다시 요청을 보내도록 하는 함수
## Render vs Redirect
render : HTML을 보여줄 필요가 있을 경우 사용
redirect : 보여줄 HTML이 이미 정의가 되어있을 경우= 이미 있는 것을 그대로 사용하고 싶은 경우 사용, 모든 주소가 GET으로 요청이 감

![redirect 적용](<../이미지/240326/redirect()함수 적용.PNG>)

* redirect 특징
    * 해당 redirect에서 클라이언트는 detail url로 요청을 다시 보내게 됨
    * 결과적으로 detail view 함수가 호출되어 detail view 함수의 반환 결과인 detail 페이지를 응답 받음
    * 결국 사용자는 게시글 작성 후 작성된 게시글의 detail페이지로 이동하는 것으로 느끼게 되는 것

```py
from django.shortcuts import render, redirect

def create(request):
    return redirect('articles:detail', article.pk)

```
![redirect 결과](<../이미지/240326/redirect 결과.PNG>)

# Delete 기능 구현
조회 후 삭제!
![delete](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240326/delete.PNG)

# Update
* 2개의 view함수가 필요
    * edit : 사용자 입력 데이터를 받을 페이지를 렌더링
    * update : 사용자가 입력한 데이터를 받아 DB에 저장

* edit

![edit 코드](<../이미지/240326/edit 코드.PNG>)

![edit 구현](<../이미지/240326/edit 구현.PNG>)

![edit 작성후 template 수정](<../이미지/240326/edit 템플릿.PNG>)

![edit 이동](<../이미지/240326/edit 이동 코드.PNG>)

* update

![update](<../이미지/240326/update 코드.PNG>)

![update 작성후 템플릿 수정](<../이미지/240326/update 템플릿 수정.PNG>)

# GET과 POST

* 'GET'Method
로그인에서는 get을 사용하지 않음
* 로그인에서는 post를 사용
* 왜냐하면 get함수를 사용하면 조회를 url로 보내고 post는 조회를 body에 담음

* post는 DB의 구조를 직접적으로 바꿈
![POST GET](<../이미지/240326/GET POST.PNG>)

## GET 요청이 필요한 경우
* 캐싱 및 성능
    * GET 요청은 캐시(Cache)될 수 있고, 이전에 요청한 정보를 새로 요청하지 않고 사용할 수 있음
    * 특히, 동일한 검색 결과를 여러번 요청하는 경우 GET 요청은 캐시를 활용하여 더 빠르게 응답할 수 있음

* 가시성 및 공유
    * GET 요청은 URL에 데이터가 노출되어 있기 때문에 사용자가 해당 URL을 북마크하거나 다른 사람과 공유하기 용이

* RESTful API 설계
    * HTTP 메서드의 의미에 따라 동작하도록 디자인된 API의 일관성을 유지할 수 있음

## 캐시(Cache)
* 데이터나 정보를 임시로 저장해두는 메모리나 디스크 공간
* 이전에 접근한 데이터를 빠르게 검색하고 접근할 수 있도록 함

* HTTP request methods를 활용한 효율적인 URL 구성
https://developer.themoviedb.org/reference/intro/getting-started



