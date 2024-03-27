# URLs
![URLs의 역할](<../이미지/240314/URLs의 역할.PNG>)

## URL dispatcher
* URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결(매핑)

## App과 URL
* App URL mapping
  * 각 앱에 URL을 정의하는 것
  * 프로젝트와 각 앱이 URL을 나누어 관리를 편하게 하기 위함
* 2번째 앱을 생성후에 발생할 수 있는 문제(기존 app: articles, 새로 생성된 app : pages)
  * view 함수 이름이 같거나 같은 패턴의 URL 주소를 사용하게 되 경우
  * 코드를 통해 각각 따로 관리(from articles import views as articles_view)할 수 있으나 앱의 개수가 늘어나면 비효율적
  * URL을 각자 app에서 관리할 수 있게 만들면 됨

![변경된 URL 구조](<../이미지/240314/변경된 URL 구조.PNG>)

![변경된 URL 구조 코드](<../이미지/240314/url 구조 변화.PNG>)

### include(앱이름.url)
* 프로젝트 내부 앱들의 URL을 참조할 수 있도록 매핑하는 함수
* URL의 일치하는 부분까지 잘래내고, 남은 문자열 부분은 후속 처리를 위해 include된 URL로 전달

![변경후 url.py](<../이미지/240314/변경된 URL py.PNG>)

![변경후 app의 url.py](<../이미지/240314/변경된 app의 url py.PNG>)
* 명시적 상대경로(.)를 통해 자신의 함수를 받아옴

## URL 이름지정
* url 구조 변경에 따른 문제점
  * 기존 'articles/' 주소가 'articles/index/'로 번경됨에 따라 해당 주소를 사용하는 모든 위치를 찾아가 변경해야 함
  * 이것을 해결하기 위해 이름을 지어주면 됨
### Naming URL patterns
* URL에 이름을 지정하는 것(path 함수의 name인자를 정의해서 사용)

![Naming URL patterns](<../이미지/240314/naming URL pattern 적용.PNG>)

* URL 표기 변화
  * a 태그의 href 속성 값뿐만 아니라 form의 action 속성처럼 url을 작성하는 모든 위치에서 변경
![url 표기 변화](<../이미지/240314/url 표기 변화.PNG>)
* 'url' tag

![url 태그](<../이미지/240314/url tag.PNG>)
  * 주어진 URL 패턴의 이름과 일치하느 절대 경로

![url 태그 적용](<../이미지/240314/url tag 적용.PNG>)

* URL 이름 지정 후 남은 문제
  * articles 앱의 url이름과 pages앱의 url 이름이 같은 상황
  * 단순히 이름만으로는 완벽하게 분리할 수 없기 때문에 분리하기 위해 이름의 성의 역할을 해주는 key를 붙임
  * 'app_name' 속성지정
    * app_name은 이름을 그대로 써야함, 안그러면 에러 발생

![app_name](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240314/app_name.PNG)

* URL tag의 최종 변화
  * 마지막으로 url태그가 사용하는 모든 곳의 표기 변경이 필요

![URL tag 최종](<../이미지/240314/url tag 최종.PNG>)

# Model
* Model을 통한 DB 관리
  
![Model 구조](<../이미지/240314/Model 구조.PNG>)
## Django Model
* DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공
  * 테이블 구조를 설계하는 청사진(blueprint)역할
### Model 클래스 작성
```py
# articles/models.py

class Article(models.Model):# models라는 모듈의 내장된 Model클래스를 상속받고 있음
    title=models.CharField(max_length=10)
    content = models.TextField()
```

* 작성한 model 클래스는 최종적으로 DB에 다음과 같은 테이블 구조를 만듦
(id 필드는 django가 자동으로 생성)
![model class 살펴보기 1](<../이미지/240314/model class 살펴보기.PNG>)

* django.db.models 모듈의 Model이라는 부모 클래스를 상속받음
* Model은 model에 관련된 모든 코드가 이미 작성 되어있는 클래스
  * https://github.com/django/django/blob/main/django/db/models/base.py#L460
* 개발자는 가장 중요한 테이블 구조를 어떻게 설계할지에 대한 코드만 작성하도록 하기 위한 것(상속을 활용한 프레인워크의 기능 제공)
* 클래스 변수명
  * 테이블의 각 필드(열 이름)
* model Field 클래스
  * 테이블 필드의 데이터 타입
  * https://docs.djangoproject.com/en/4.2/ref/models/fields/
* model Field 클래스의 키워드 인자(필드 옵션)
  * 테이블 필드의 '제약조건' 관련 설정
  * https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-options
* 테이블만들때 3가지 조건
  * 필드이름
  * 필드 데이터 타입
  * (선택) 필드의 제약 조건
    * 제약조건이란? 데이터가 올바르게 저장되고 관리되도록 하기 위한 규칙<br>ex) 숫자만 저장되도록, 문자가 100자까지만 저장되도록 하는 등

## Migrations
* model 클래스의 변경사항(필드 생성, 수정 삭제등)을 DB에 최종 반영하는 방법

![migrations 과정](<../이미지/240314/migrations 과정.PNG>)
* 설계도를 최종적으로 만드는 과정과 DB를 만드는 과정이 필요

* Migrations 핵심 명령어 2가지
  *  $python manage.py makemigrations : model class를 기반으로 최종 설계도(migration) 작성
     *  django가 명령어를 통해 설계도를 만들기 때문에 생성된 파일(0001_initail.py)을 수정하면 안되고 models.py를 통해 수정할 것
  *  $ python manage.py migrate : 최종 설계도를 DB에 전달하여 반영
  
  ![DB 결과](<../이미지/240314/migrate 후 db결과.PNG>)

### 추가 Migrations
* 이미 생성된 테이블에 필드를 추가해야 한다면?
  
![필드 추가](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240314/%ED%95%84%EB%93%9C%EC%B6%94%EA%B0%80.PNG)

* 추가 모델 필드 작성

![추가migration1](<../이미지/240314/추가 migration1.PNG>)

* 위 코드를 작성후 makemigrations로 반영하면 아래와 같은 선택창이 생김

![추가 migration 2](<../이미지/240314/추가 migration2.PNG>)

* 데이터베이스는 무결성의 원칙이 있어서 빈값을 가진 컬럼을 추가할 수 없음 == 필드의 기본값 설정이 필요
* 1번은 현재 대화를 유지하면서 직접 기본값을 입력하는 방법
* 2번은 현재 대화에서 나간 후 models.py에 기본값 관련 설정을 하는 방법
* 여기서 1번을 선택한다면

![추가 migration3](<../이미지/240314/추가 migration3.PNG>)

* 날짜 데이터이기 때문에 직접 입력하기 보다 Django가 제안하는 기본값을 사용하는 것을 권장
* 아무것도 입력하지 않고 enter를 누르면 Django가 제안하는 기본값으로 설정 됨

![추가 migration4](<../이미지/240314/추가 migration4.PNG>)

* migration 과정 종료 후 2번째 migration 파일이 생성됨을 확인
* Django는 설계도를 쌓아가면서 추후 문제가 생겼을 시 복구하거나 되돌릴 수 있도록 함(git commit과 유사)

![추가 migration5](<../이미지/240314/추가 migration5.PNG>)
* 이때 migration에 작성된 설계도를 보면 2번 설계도는 1번 내용을 빼고 추가 된 내용만 설계되어 있음
* 이 말은 설계도를 중간에 지운다면 다른 설계도가 정상 작동 안할 수 있다는 걸 의미

* 이후 migrate하면 테이블 변화 확인

![추가 migration 6](<../이미지/240314/추가 migration6.PNG>)

* model class에 변경사항이 생겼다면, 반드시 새로운 설계도를 생성하고 이를 DB에 반영해야한다.
  * model class 변경 -> makemigrations -> migrate

## Model Field
* DB 테이블의 필드(열)을 정의하며, 해당 필드에 저장되는 데이터 타입과 제약 조건을 정의
  
### CharField()
* 길이의 제한이 있는 문자열을 넣을 때 사용
* 필드의 최대 길이를 결정하는 max_length는 필수 인자
  
### TextField()
* 글자의 수가 많을 때 사용
  
### DateTimeField()
* 날짜와 시간을 넣을 때 사용
* DateTimeField의 선택인자
  * auto_now : 데이터가 저장될때마다 자동으로 현재 날짜시간을 저장
  * auto_now_add : 데이터가 처음 생성될 때만 자동으로 현재 날짜 시간을 저장

# Admin site
* Automatic admin interface
  * Django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공
  * 데이터 확인 및 테스트 등을 진행하는데 매우 유용
* admin 계정 생성
  * $ python manage.py createsuperuser
  * email은 선택사항이기 때문에 입력하지 않고 진행가능
  * 비밀번호 입력시 보안상 터미널에 출력되지 않으니 무시하고 입력 이어가기

* DB에 생성된 admin 계정 확인
![admin 생성1](<../이미지/240314/admin site1.PNG>)

* admin에 모델 클래스 등록
  * admin.py에 작성한 모델 클래스를 등록해야만 admin site에서 확인 가능
![admin 생성2](<../이미지/240314/admin site2.PNG>)
#admin 사이트에 등록한다. Article 클래스를

* admin site 로그인 후 등록된 모델 클래스 확인
![admin 생성3](<../이미지/240314/admin site3.PNG>)

* 데이터 생성, 수정, 삭제 테스트
![admin 생성4](<../이미지/240314/admin site4.PNG>)

* 테이블 확인
![admin 생성5](<../이미지/240314/admin site5.PNG>)

# 참고
* 데이터 베이스를 초기화하고 싶으면
1) migration 파일 삭제
2) db.sqlite3 파일 삭제
   - 이 때 __init__.py와 migration 폴더가 삭제 되지 않도록 주의
   - 삭제 후 다시 만들어도 작동 안함

* Migration 기타 명령어
  * $ python manage.py showmigrations
    * migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 명령어
    * [X]표시가 있으면 migrate가 완료되었음을 의미
  * $ python manage.py sqlmigrate articles 0001
    * 해당 migrations파일이 SQL 언어(DB에서 사용하는 언어)로 어떻게 번역되어 DB에 전달되는지 확인하는 명령어
* 첫 migrate시 출력 내용이 많은 이유는 Django프로젝트가 동작하기 위해 미리 작성되어 있는 기본 내장 app들에 대한 migration파일들이 함께 migrate 되기 때문
* SQLite : 데이터베이스 관리 시스템 중 하나이며 Django의 기본 데이터베이스로 사용됨(파일로 존재하며 가볍고 호환성이 좋음)
* CRUD : 소프트웨어가 가지는 기본적인 데이터 처리 기능
  * Create(저장)
  * Read(조회)
  * Update(갱신)
  * Delete(삭제)