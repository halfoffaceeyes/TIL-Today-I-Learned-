# 팔로우 기능 구현

1. url 작성
* 주의 사항 : \<usename>/주소를 urlpatterns의 첫번째로 작성한다면 문자열로 입력받는 모든 주소가 profile로 들어감(login,logout,signup등등) ==> 해결하기 위해 맨아래로 내리거나 /profile/\<username>처럼 앞에 profile을 붙여서 다른 주소로 만들어줌

    ![팔로우 url](<../이미지/240409/팔로우 url.PNG>)

2. view함수 작성
* User는 직접 참조를 하지 않기 때문에 get_user_model()함수나, Auth_USER_MODEL을 사용 => AUTH_USER_MODEL는 models.py에서만 사용하므로 get_user_model함수사용

    ![프로필 view함수](<../이미지/240409/팔로우 프로필 view.PNG>)


3. profile 템플릿 작성

    ![profile 템플릿 작성](<../이미지/240409/팔로우 프로필 템플릿.PNG>)

4. 프로필 구현

    ![프로필 이동 태그 작성](<../이미지/240409/팔로우 프로필 이동.PNG>)

5. 프로필 페이지 결과

    ![프로필 페이지 결과](<../이미지/240409/프로필페이지 결과.PNG>)

# 팔로우 기능 구현
## User(M) - User(N)
* 0 명 이상의 회원은 0명 이상의 회원과 관련
* 회원은 0명 이상의 팔로워를 가질수 있고, 0명 이상의 다른 회원들을 팔로잉 할 수 있음

1. ManyToManyField 작성
* ManyToManyField는 복수형으로 작성
* self로 참조하는 ManyToMany Field를 작성(이때, 자신을 참조할 경우 symmetrical 옵션을 사용할 수 있음, 이때 대칭을 꺼줌)

* 참조 : 내가 팔로우하는 사람들(팔로잉, followings)
* 역참조 : 상대방 입장에서 나는 팔로워 중 한명(팔로워,followers)
* 참조 역참조 관계는 바뀌어도 상관없으나 관계조회시 생각하기 편한 방향으로 정한것

* 이 때, related name설정을 안한다면,<br>
참조는 user1.followings.all() <br>
역참조는 user1.user_set.all()이 되므로 통일시켜주기 위해 followers로 이름을 설정

![팔로우 필드 설정](<../이미지/240409/팔로우 기능 1.PNG>)

2. Migration 진행 후 중개 테이블 확인

    ![중개테이블이름](<../이미지/240409/팔로우 기능 2.PNG>)
* from -> to followings
* to -> from followers

    ![중개 테이블](<../이미지/240409/팔로우 기능 2-2.PNG>)

3. url 작성
* 이 때 user_pk는 상대방을 조회하기 위해 필요

    ![팔로우 url](<../이미지/240409/팔로우 기능 3.PNG>)


4. 팔로우 view함수 작성
```py
    me = request.user # 현재 유저(나)
    you = get_user_model().objects.get(pk=user_pk) # 내가 팔로우를 할 유저
``` 
* 만약 팔로우가 이미 되어있으면 버튼을 누를 경우 팔로우 취소함 : me.followings.remove(you)==you.followers.remove(me) 이 둘은 참조 역참조 관계이므로 같은 결과를 갖음

* if me != you: 현재 유저는 스스로 팔로잉하면 안되므로

    ![팔로우 view함수](<../이미지/240409/팔로우 기능 4.PNG>)

5. 프로필 유정의 팔로잉, 팔로우 수 & 팔로우, 언팔로우 버튼 작성

    ![팔로우 템플릿 작성](<../이미지/240409/팔로우 기능 5.PNG>)

## 참고
### .exists()
* QuerySet API 중하나
* QuerySet에 결과가 포함되어 있으면 True를 반환하고 결과가 포함되어 있지 않으면 False를 반환
* 큰 QuerySet에 있는 특정 객체 검색에 유용

    ![exist 적용1](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240409/exist%EC%A0%81%EC%9A%A9.PNG)
    ![exist 적용2](<../이미지/240409/exist 적용 2.PNG>)

# Fixtures
* Django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음
* 데이터는 데이터베이스 구조에 맞추어 작성되어 있음
* Fixtures는 초기 데이터를 제공하기 위해 사용

## 초기 데이터의 필요성
* 협업하는 유저 A,B가 있다고 생각해보기
1. A가 먼저 프로젝트를 작업 후 원격 저장소에 push 진행
    * gitignore로 인해 DB는 업로드하지 않기 때문에 A가 생성한 데이터도 업로드 X
2. B가 원격 저장소에서 A가 push한 프로젝트를 pull(혹은 clone)
    * 결과적으로는 B는 DB가 없는 프로젝트를 받게 됨
* 이처럼 프로젝트의 앱을 처음 설정할 때 동일하게 준비된 데이터로 데이터베이스를 미리 채우는 것이 필요한 순간이 있음
* Django에서는 fixtures를 사용해 앱에 초기 데이터(initial data)를 제공

## Fixtures 활용
### Fixtures 관련 명령어
* dumpdata : 생성(데이터 추출)
* loaddata : 로드(데이터 입력)

#### dumpdata
* 데이터 베이스의 모든 데이터를 추출
* 작성 예시
    * --indent 4는 데이터 형식을 들여쓰기 4칸을 넣어서 작성할 것이라는 뜻(인덴트를 안주면 데이터가 한줄로 나옴, 데이터를 잘 구별하고자 하기 위함, 필수 아님)

    ![작성 예시](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240409/dumpdata.PNG)
* 활용

    ![dumpdata 활용](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240409/dumpdata2.PNG)
    ![dumpdata 활용2](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240409/dumpdata3.PNG)

#### loaddata
* Fixtures 데이터를 데이터베이스로 불러오기
##### Fixtures 파일의 기본 경로
* app_name/fixtures/
* Django는 설치된 모든 app의 디렉토리에서 fixtures 폴더 이후의 경로로 fixtures 파일을 찾아 load

##### loaddata 활용
* 경로 설정

    ![loaddata경로설정](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240409/loaddata%ED%99%9C%EC%9A%A9.PNG)
    ![loaddata 활용](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240409/loaddata%ED%99%9C%EC%9A%A92.PNG)

##### loaddata 순서 주의사항
* 만약 loaddata를 한번에 실행하지 않고 별도로 실행한다면 모델 관계에 따라 load 순서가 중요할 수 있음
    - comment는 article에 대한 key 및 user에 대한 key가 필요
    - article은 user에 대한 key가 필요
* 즉, 현재 모델 관계에서는 user -> article -> comment 순으로 data를 load해야 오류를 발생하지 않음
* 한번에 로드하면 django가 알아서 데이터를 입혀줌

#### 참고
* 모든 모델을 한번에 dump하기

    ![한번에 dump하기](<../이미지/240409/한번에 dump.PNG>)

* loaddata 시 encoding codec 관련 에러가 발생하는 경우
    * 2가지 방법 중 택 1
    1. dumpdata 시 추가 옵션 작성
    ```
    $ python -Xutf8 manage.py dumpdata [생략]
    ```

    2. 메모장 활용
        1. 메모장으로 json파일 열기
        2. '다른 이름으로 저장' 클릭
        3. 인코딩을 UTF8로 선택 후 저장

* Fixtures 파일을 직접 만들지 말고 반드시 dumpdata명령어를 사용하여 생성할것!!

# Improve query
* query 개선하기
* 같은 결과를 얻기 위해 DB측에 보내는 Query 개수를 점차 줄여 조회하기

## 사전준비
* fixture 데이터
    - 게시글 10개 / 댓글 100개 / 유저 5개
* 모델관계
    - N:1 - Article:User / Comment:Article / Comment:Article
    - N:M - Article:User

## annotate
* SQL의 GROUP BY를 사용
* 반복되는 sql을 한번에 데이터를 가져올 수 있도록 작성

### 문제 상황
* 문제 원인
    - 각 게시글마다 댓글 개수를 반복 평가

    ![annotate 문제 현황1](<../이미지/240409/annotate 문제 현황1.PNG>)
    
    ![annotate 문제 현황2](<../이미지/240409/annotate 문제 현황2.PNG>)

### annotate 적용
* 문제 해결
    - 게시글을 조회하면서 댓글 개수까지 한번에 조회해서 가져오기

    ![annotate 적용 1](<../이미지/240409/annotate 적용1.PNG>)

* 반복되는 쿼리를 제거

    ![annotate 적용 2](<../이미지/240409/annotate 적용2.PNG>)

## select_related
* SQL의 INNER JOIN을 사용
* 1:1 또는 N:1 참조 관계에서 사용
### 문제 상황
* 문제 원인
    - 각 게시글마다 작성한 유저명까지 반복 평가

![selected related 문제상황](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240409/selected_related.PNG)

### 문제 해결
* 게시글을 조회하면서 유저정보까지 한번에 조회해서 가져오기

    ![selected_related 적용](<../이미지/240409/selected_related 적용.PNG>)

    ![selected_related 적용 결과](<../이미지/240409/selected_related 적용 결과.PNG>)

## prefetch_related
* M:N 또는 N:1 역참조 관계에서 사용
* SQL이 아닌 Python을 사용한 JOIN을 진행
### 문제상황
* 각 게시글 출력 후 각 게시글의 댓글 목록까지 개별적으로 모두 평가

![prefetche_related 문제 상황](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240409/prefetched_related.PNG)
![prefetche_related 문제 상황2](<../이미지/240409/prefetched_related 문제상황.PNG>)

### 문제 해결
* 게시글을 조회하면서 참조된 댓글까지 한번에 조회해서 가져오기

![prefetched_related 문제해결](<../이미지/240409/prefetched_related 문제해결.PNG>)
![prefetched_related 문제해결](<../이미지/240409/prefetched_related 문제해결2.PNG>)

## select_related & prefetch_related

## 문제 상황
* '게시글' + '각 게시글의 댓글 목록' + '댓글의 작성자'를 단계적으로 평가

![selected_related& prefetch 문제상황](<../이미지/240409/selected_related& prefetch 문제상황.PNG>)
![selected_related& prefetch 문제상황2](<../이미지/240409/selected_related& prefetch 문제상황2.PNG>)

### 문제 해결
* 1단계 : prefetch_related 적용 : 게시글을 조회하면서 참조된 댓글까지 한번에 조회

    ![selected_related& prefetch 문제해결1](<../이미지/240409/selected_related& prefetch 문제해결1.PNG>)

* 아직 100개의 비슷한 쿼리가 중복으로 조회 중

    ![selected_related& prefetch 결과1](<../이미지/240409/selected_related& prefetch 결과1.PNG>)

* 2단계 : '게시글' + '각 게시글의 댓글 목록' + '댓글의 작성자'를 한번에 조회

    ![selected_related& prefetch 문제해결2](<../이미지/240409/selected_related& prefetch 문제해결2.PNG>)

* 2개의 쿼리만 남음 ==시간단축

    ![selected_related& prefetch 결과2](<../이미지/240409/selected_related& prefetch 결과2.PNG>)