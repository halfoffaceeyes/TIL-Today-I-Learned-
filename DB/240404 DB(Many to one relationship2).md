# User와 다른 모델 간의 모델 관계 설정
N쪽에 외래키를 작성
1. Article(N)-User(1)
    * 0개이상의 게시글은 1명의 회원에 의해 작성될 수 있다.
2. Comment(N)-User(1)
    * 0개 이상의 댓글은 1명의 회원에 의해 작성될 수 있다.

# 모델 관계 설정
## Article & User
* user 외래키 정의

    ![모델관계설정](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240404/%EB%AA%A8%EB%8D%B8%EA%B4%80%EA%B3%84%EC%84%A4%EC%A0%95.PNG)

* User 모델을 참조하는 2가지 방법
    * django 프로젝트'내부적인 구동 순서'와 '반환 값'에 따라 다름 > models.py 구동이 빠르기 때문에 그 안에 들어있는 get_user_model()을 사용한다면 구동이 될때 User 객체를 반환을 할 수 없음(User 객체가 아직 안만들어져서 에러가 남) => 문자열로 미리 만들어주어야하므로 settings.AUTH_USER_MODEL을 사용

||get_user_model()|settings.AUTH_USER_MODEL|
|---|---|---|
|반환 값|User Object(객체)|'accounts.User'(문자열)|
|사용 위치|models.py가 아닌 다른 모든 위치|models.py|

* 외래 키 설정 이후 Migration하는 과정에서 아래와 같은 과정이 나옴.
    * 기존에 테이블이 있는 상황에서 필드를 추가하려기 때문에 발생하는 과정
    * 기본적으로 모든 필드에는 NOT NULL 제약조건이 있기 때문에 데이터가 없이는 새로운 필드가 추가되지 못함
    * '1'을 입력하고 Enter 진행

    ![Migration1](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240404/migration1.PNG)

* 추가하는 외래 키 필드에 어떤 데이터를 넣을 것인지 직접입력이 필요
* 외래키는 증가하는 정수 형태로 입력해야하므로 아무정수를 입력해도 상관없음
    * '1'을 입력하고 진행
* 기존에 작성된 게시글이 있다면 모두 1번 회원이 작성한 것으로 처리됨

    ![Migration2](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240404/migration2.PNG)

* migrate를 진행완료하면 articles_article 테이블에 user_id 필드 생성

    ![Migration3](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240404/migration3.PNG)

### 게시글 CREATE
* 기존 ArticleForm 출력 변화 확인
* User 모델에 대한 외래키 데이터 입력을 받기 위해 불필요한 input이 출력되므로 ArticleForm 출력 필드 수정

    ![게시글 create1](<../이미지/240404/게시글 create1.PNG>)
    ![게시글 create2](<../이미지/240404/게시글 create2.PNG>)

* 불필요한 input을 제외하여 user_id 정보가 제외됨 => view함수에서 추가

    ![게시글 create3](<../이미지/240404/게시글 create3.PNG>)
    ![게시글 create4](<../이미지/240404/게시글 create4.PNG>)


### 게시글 READ
* 각 게시글의 작성자 이름 출력
* user객체에 magicmethod(__str__)를 통해 username을 출력할수 있음.
```py
class User(AbstractUser):
    def __str__(self):
        return self.username
```
![게시글 READ1](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240404/%EA%B2%8C%EC%8B%9C%EA%B8%80READ1.PNG)
![게시글 READ2](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240404/%EA%B2%8C%EC%8B%9C%EA%B8%80READ2.PNG)

### 게시글 UPDATE
* 본인의 게시글만 수정할 수 있도록 하기
    - 게시글 수정 요청 사용자와 게시글 작성자를 비교 후 해당 게시글의 작성자가 아니라면, 수정/삭제 버튼을 출력하지 않도록 하기

![게시글 UPDATE1](<../이미지/240404/게시글 update1.PNG>)

![게시글 UPDATE2](<../이미지/240404/게시글 update2.PNG>)

### 게시글 DELETE
* 본인의 게시글만 삭제할 수 있도록 하기
    - 삭제를 요청하려는 사용자와 게시글을 작성한 사용자를 비교

![게시글 DELETE](<../이미지/240404/게시글 DELETE.PNG>)


## Comment & User
* user 외래키 정의

    ![외래키 설정](<../이미지/240404/Comment user 외래키.PNG>)

* Migration (Article-user와 동일)

### 댓글 Create
* 댓글 작성시 작성자 정보가 함께 저장될 수 있도록 작성

    ![댓글 Create](<../이미지/240404/댓글 create1.PNG>)

### 댓글 READ
* 댓글 출력 시 댓글 작성자와 함께 출력

    ![댓글 READ](<../이미지/240404/댓글 READ.PNG>)

### 댓글 DELETE
* 본인의 댓글만 삭제할 수 있도록 하기
    - 댓글 삭제 요청 사용자와 댓글 작성 사용자를 비교

    ![댓글 DELETE1](<../이미지/240404/댓글 DELETE1.PNG>)

* 해당 댓글의 작성자가 아니라면, 댓글 삭제 버튼을 출력하지 않도록 함

    ![댓글 DELETE2](<../이미지/240404/댓글 DELETE2.PNG>)

# 참고
## 인증된 사용자만 댓글 작성 및 삭제
![인증된 사용자](<../이미지/240404/인증된 사용자만 댓글 삭제.PNG>)

## ERD
Entity Relationship Diagram 개체 관계 다이어그램 

    ![ERD](<../이미지/240404/ERD 예제.PNG>)

* ERD에서 1:N을 표현할 때 까마귀발로 표현(1쪽은 pipeline으로 표기, N 쪽은 0개이상의 관계를 나타냄)

## GET POST만 요청받기
* 데코레이터를 응용
* 함수에 접근하는 여러개의 method의 목록으로 작성
```py
from django.views.decorattors.http import require_http_methods
@require_http_methods(["GET", "POST"])
```
## View decorator 확인
 https://docs.djangoproject.com/en/5.0/topics/http/decorators/