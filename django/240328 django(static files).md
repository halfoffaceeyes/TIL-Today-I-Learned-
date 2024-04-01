# Static fiels
* 정적 파일
* 서버 측에서 변경되지 않고 고정적으로 제공되는 파일(이미지, JS, CSS 파일 등)
* 처음부터 준비되어 제공되는 파일

## 웹서버와 정적 파일
* 웹서버의 기본동작은 특정위치(URL)에 있는 자원을 요청(HTTP request) 받아서 응답(HTTP response)을 처리하고 제공하는 것
* 이는 자원에 접근 가능한 주소가 있다는 것을 의미== static file에 대한 온라인 URL 주소를 생성해야한다.
* 웹서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공함
* 정적 파일을 제공하기 위한 경로(URL 주소)가 있어야함

![웹서버](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240328/%EC%9B%B9%EC%84%9C%EB%B2%84.PNG)

## Static files 제공하기
1. 기본 경로에서 제공하기(app폴더/static/)
- 원하는 static file을 올바른 경로(app폴더/static/폴더명/)에 위치

![static 경로지정](<../이미지/240328/static 경로 지정.PNG>)

- static file을 불러올 HTML 파일에서 경로 제공
    - load tag를 이용하여 static을 불러오는 걸 설정 후 static file의 주소를 static tag를 이용하여 불러옴(이때 확장자명까지 입력해야함) == url tag랑 비슷함

![static 불러오기](<../이미지/240328/static 불러오기.PNG>)

![static file 예시](<../이미지/240328/static files 불러오기 예시.PNG>)
- STATIC_URL을 확인("http://127.0.0.1:8000/static/articles/sample-1.png" 로 만들어져 있음)
- 이미지를 불러왔다는 것은 URL 주소가 만들어 진것 == django가 알아서 이미지의 URL을 형성하여서 URL만 이용해도 이미지를 불러올 수 있음

### STATIC_URL
* 기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL
* 실제 파일이나 디렉토리가 아니며, URL로만 존재
* settings.py의 맨아래에 위치하고 있음
![staticURL](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240328/static_URL.PNG)

이 때, static/ 가 기본 값으로 설정되어 있어서 static file을 작업자 도구로 확인할 경우 주소가 127.0.0.1:8000/static이 기본으로 들어가게 되는 것

![static_URL](<../이미지/240328/static URL 경로.PNG>)


2. 추가 경로에서 제공하기
* STATICFILES_DIRS 
    * 정적 파일의 기본경로 외에 추가적인 경로 목록을 정의하는 리스트
    * STATICFILES_DIRS에 문자열 값으로 추가 경로 설정(리스트형식으로 작성)

![STATICFILES 경로 설정](<../이미지/240328/STATICFILES_DIRS 설정.PNG>)
* 보통 settings.py의 static_URL아래에 작성하고, base_dir기준으로 폴더 경로를 적어주면 됨

![static 추가 경로 설정](<../이미지/240328/static추가경로 설정.PNG>)
![static 추가 경로 설정](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240328/static%EC%B6%94%EA%B0%80%EA%B2%BD%EB%A1%9C.PNG)

* load tag 주의사항 
    * extends tag 주의사항이 제일 위에 있어야하는 것. 따라서 load는 extends아래에 tag를 입력해주어야한다.
    * load tag를 부모 템플릿에 사용해도 자식 템플릿에 적용이 안되므로 각각 load해주어야함


# Media files
* 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)
* 전달할 때 form tag의 enctype을 설정을 꼭 해줘야함(multipart/form-dat, HTML mdn form 가이드- 데이터주고받기로 검색)
* save 할때 ArticleForm에서 request.FILES를 추가
## 이미지 업로드
### imageField()
* 이미지 업로드에 사용하는 모델 필드
* 이미지 객체가 직접 저장되는 것이 아닌 '이미지 파일의 경로'가 문자열로 DB에 저장

### 미디어 파일 제공을 위한 사전준비
* https://docs.djangoproject.com/en/4.2/howto/static-files/#serving-fils-uploaded-by-a-user-during-development

* django static으로 검색하면 media file 사용 방법이 나옴

1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정

* MEDIA_ROOT : 실제 미디어 파일들이 위치하는 디렉토리의 절대 경로
![MEDIA_ROOT](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240328/MEDIA_ROOT.PNG)

* MEDIA_URL : MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성(STATIC_URL과 동일한 역할)
![MEDIA_URL](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240328/MEDIA_URL.PNG)

2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 URL 지정
    * 업로드 된 파일을 제공하는 URL == settings.MEDIA_URL
    * 위 URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT
    * path함수와 비슷하게 생각할 것

    ![MEDIA_ROOT와 MEDIA_URL에 대한 URL 지정](<../이미지/240328/MEDIA_ROOT와 MEDIAURL에 대한 url 지정.PNG>)

### 이미지 업로드
* blank= True 속성을 작성해 빈 문자열이 저장될 수 있도록 제약 조건 설정
* 게시글 작성 시 이미지 없이 작성할 수 있도록
![이미지업로드](<../이미지/240328/이미지 업로드.PNG>)
* 이때 모델에서 기존 필드 사이에 작성해도 실제 테이블에서는 가장 우측에 추가됨

* ImageField를 사용하려면 Pillow 라이브러리가 필요
![pillow 설치](<../이미지/240328/pip pillow.PNG>)

* form 요소의 enctype 속성 추가
![enctype 설정](<../이미지/240328/enctype 설정.PNG>)

* view 함수에서 업로드 파일에 대한 추가 코드 작성
    * 이미지 파일은 POST에 전달이 안되고 FILES에 전달됨

![VIEW 함수 수정](<../이미지/240328/이미지 view함수 수정.PNG>)

* 업로드가 되면 media 폴더가 생기고 그 안에 image파일이 들어감
* 실제 이미지를 업로드하면 이미지 파일이 업로드된다기 보다는 경로가 저장되는 형태임

### 업로드 이미지 제공하기
* url 속성을 통해 업로드 파일의 경로 값을 얻을 수 있음
* article.image.url : 업로드 파일경로
* article.image : 업로드 파일의 파일 이름

![업로드 이미지 제공하기](<../이미지/240328/업로드 이미지 제공.PNG>)

![이미지 업로드 확인](<../이미지/240328/이미지 업로드 확인.PNG>)

* 이미지를 업로드하지 않은 게시물의 경우에는 템플릿을 렌더링 할 수 없으므로 이미지가 있는 경우만 이미지를 출력할 수 있도록 처리

{% if article.image %}<br>
    \<img src>~~<br>
{%endif%}<br>

* update html, view 함수도 동일하게 추가코드를 작성해야함
![update 수정](<../이미지/240328/update 수정.PNG>)

![update view함수 수정](<../이미지/240328/updateview 수정.PNG>)

* 동일한 파일명이 업로드되는 경우 django가 알아서 뒤에 랜덤명을 붙여서 media 폴더에 저장
* 새로 수정한다고 해서 이전에 저장된 파일들이 지워지는 것이 아님. 여러번 수정하게 되거나 이미지가 쌓이면 용량이 증가하게 되는데 이미지를 관리하는 라이브러리를 통해 안쓰는 이미지를 제거가능함.
# 참고
* media_ROOT 경로는 부득이하게 리스트 형식이 아니라 하나로만 경로 지정이 가능함

* 따라서 media의 내부경로를 지정해주고 싶을 경우에 imagefield에서 upload_to를 이용하여 만들수 있음 == username 별로 media파일 관리가 가능
* 함수를 형성하여 미디어파일 관리할 경우 models.py(model과 같은경로)에서 작성하여 사용

* ImageField()의 upload_to 인자를 사용해 미디어 파일 추가 경로 설정
![mediaroot경로 설정](<../이미지/240328/image mediaroot경로 설정.PNG>)

## request.FILES가 두번째 위치 인자인 이유
* ModelForm 상위 클래스 BaseModelForm의 생성자 함수 키워드 인자 참고(순서가 첫번째 data, 두번째 files여서)
![baseModelForm](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240328/requestfiles%EC%88%9C%EC%84%9C.PNG)

## 1급객체
함수에 인자로 엄기기, 변수에 대입하기, 결과값을 리턴할 수 있는 객체