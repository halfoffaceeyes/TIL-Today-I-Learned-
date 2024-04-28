# ORM(Object-Relational-Mapping)
* 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술

## ORM의 역할
* 데이터 베이스를 조작하기 위해 사용
* 데이터베이스와 django(python)와 사용하는 언어가 다르기 때문에 소통 불가

![ORM역할](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240325/ORM.PNG)

# QuerySet API
* ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는 데 사용하는 도구
> API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리

    ![QuerySet API 구문](<../이미지/240325/QuerySet API 구문.png>)
QuerySet: 다중 데이터<br>
Instance : 단일 데이터

## QuerySet API 구문
![QuerySet API](<../이미지/240325/QuerySet API.PNG>)
호출시 모델명.objects. 는 고정(objects가 여러 메서드를 제공하는 역할)

![QuerySet API 구문 예시](<../이미지/240325/QuerySet API 구문 예시.png>)

### Query
* 데이터베이스에 특정한 데이터를 보여 달라는 요청
* "쿼리문을 작성한다."
    * 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다.
* 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 우리에게 전달
### QuerySet
* 데이터 베이스에게서 전달 받은 객체 목록(데이터 모음)
    * 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
* Django ORM을 통해 만들어진 자료형
* 단, 데이터베이스가 단일한 객체를 반환할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨

> QuerySet API는 python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장, 조회, 수정, 삭제하는 것(CRUD, Create, Read, Update, Delete)

# QuerySet API 실습
* 실습 사전 준비 - 외부라이브러리 설치 및 설정(Django-Shell 설치)

\$ pip install ipython django-extensions
* django-extensions : django의 확장 프로그램
* ipython : django-shell환경은 colorizing과 자동완성이 안되는데 가능하게 만들어주는 프로그램

![QuerySet API 실습](<../이미지/240325/QuerySet API 실습.PNG>)
꼭 settings.py의 INSTALLED_APPS에 django_extensions를 설치해 줄것

## Django Shell
* Django 환경안에서 실행되는 python shell
* 입력하는 QuerySet API 구문이 Django 프로젝트에 영향을 미침
\$ python manage.py shell_plus
shell_plus는 shell과 다르게 django의 Model을 불러옴

## Create
### 데이터 객체를 만드는 3가지 방법
1. 특정 테이블에 새로운 행을 추가하여 데이터를 추가하는 방법

* 클래스가 instance를 만들면서 시작

    ![객체형성1](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240325/create1.PNG)
* save()를 호출해주어야 DB에 전달 가능

    ![객체형성2](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240325/create2.PNG)
    ![객체형성3](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240325/create3.PNG)
    ![객체형성4](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240325/create4.PNG)

2. save 메서드를 호출해야 비로소 DB에 데이터가 저장됨
* 테이블에 한줄(행,레코드)이 쓰여진 것

![한줄로 객체 형성](<../이미지/240325/create 한줄입력.PNG>)


3. QuerySet API 중 create() 메서드 활용

![create()메서드](<../이미지/240325/create 메서드 활용.PNG>)

### save()
객체를 데이터베이스에 저장하는 메서드

## Read(조회)
* Return new QuerySets
    * all()
    * filter()

* Do not return QuerySets
    * get()

### all()
* 전체 데이터 조회

![all()](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240325/all().PNG)

### filter()
* 특정 조건 데이터 조회(키워드 인자가 있음, 데이터가 없어도 반환된 결과는 Queryset)

    ![filter()](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240325/filter().PNG)

### get()
* 단일 데이터 조회(반환값이 존재하여 변수에 저장가능하고 만약 데이터가 없으면 오류 발생, 여러개의 데이터를 조회해도 오류발생)

    ![get()](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240325/get().PNG)

* get() 특징
    * 객체를 찾을 수 없다면 DoesNotExist 예외를 발생시키고, 둘이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴
    * 위와 같은 특징을 가지고 있기 때문에 primary key와 같이 고유성(uniqueness)을 보장하는 조회에서 사용해야 함

## Update
* 인스턴스 변수를 변경 후 save 메서드 호출
* 수정과 삭제를 하려면 조회를 먼저 하고 진행해야함(get->update)
* 수정후 반드시 저장을 해줘야 db에 전달됨

    ![update](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240325/update.PNG)

## Delete
* 삭제하려는 데이터 조회 후 delete 메서드 호출(get-> delete)

    ![delete](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240325/delete.PNG)

* 중간의 행을 지우고 새로운 행을 만든다면??
    * ex) id가 1,2,3 중 2를 지우고 새로 만든다면, 4가 생성
    * ex) id가 1,2,3 중 3을 지우고 새로 만든다면, 4가 생성

# 참고
## Field lookups
* 특정 레코드에 대한 조건을 설정하는 방법(더 디테일한 조건을 설정하는 방법)
* QuerySet메서드filter(),exclude() 및 get()에 대한 키워드 인자로 지정
- https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups

```py
# Field lookups 예시
# 'content 컬럼에 'dja'가 포함된 모든 데이터 조회'
Article.objects.filter(content__contains='dja')
```

## ORM, QuerySet API를 사용하는 이유
* 데이터 베이스 쿼리를 추상화 하여 Django개발자가 데이터베이스와 직접 상호작용하지 않아도 되도록 함
* 데이터베이스와의 결합도를 낮추고 개발자가 더욱 직관적이고 생산적으로 개발할 수 있도록 도움
* https://docs.djangoproject.com/en/4.2/ref/models/querysets/
* https://docs.djangoproject.com/en/4.2/topics/db/queries

## 메인페이지를 만드는 법
* url -> view -> template순으로 작성(데이터의 흐름 순으로 작성)
* MTV 에서 View함수는 Controller역할이므로 데이터 베이스를 요청할수 있고 모델이랑 소통가능
* view함수에서 조회를 할 경우 반환값은 QuerySet 딕셔너리 형태의 데이터가 반환되는데 이를 render함수로 넘겨줄 때, dictionary 형태로 묶어서 전달해야하는 규칙이 있음
```py
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' = articles,
    }
    return render(request,'articles/index.html', context)
# Article 클래스의 객체를 조회해서 articles로 반환해주고
# context를 통해 index.html로 전달
# 그럼 index에서 {{articles}}로 queryset을 호출 가능
```