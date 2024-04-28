# Many to one relationship N:1 or 1:N
* 한테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한개와 관련된 관계

* Comment(N) - Article(1) : 0개 이상의 댓글은 1개의 게시글에 작성될 수 있음

* N:1 관계에서 외래키는 N에서 갖고 있어야함

    ![N:1](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240403/N%EB%8C%801.PNG)

## 댓글 모델
* ForeignKey() = N:1 관계 설정 모델 필드
* ForeignKey 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형으로 작성하는 것을 권장
* 외래 키는 ForeignKey 클래스를 작성하는 위치와 관계없이 테이블 필드 마지막에 생성됨

    ![댓글모델](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240403/%EB%8C%93%EA%B8%80%EB%AA%A8%EB%8D%B8.PNG)

### Foreignkey(to, on_delete)
* to : 참조하는 모델 class 이름
* on_delete : 외래 키가 참조하는 객체(1)가 사라졌을때, 외래 키를 가진 객체(N)를 어떻게 처리할 지를 정의하는 설정(데이터 무결성)
    * on_delete의 'CASCADE'
        * 부모객체(참조된 객체)가 삭제됐을 때 이를 참조하는 객체도 삭제
        * 참고 : https://docs.djangoproject.com/en/4.2/ref/models/fields/#arguments
    
### Migration 이후 댓글 테이블 확인
* 댓글 테이블의 article_id 필드 확인 == 따라서 모델에서 외래키 설정시 변수명을 article_id가 아닌 article로 형성(article_id로 설정하면 외래키 형성된경우 article_id_id로 필드명이 형성)
* '참조 대상 클래스' + '_'+ '클래스 이름'
    * 참조하는 클래스 이름의 소문자(단수형)로 작성하는 것이 권장되었던 이유

    ![댓글 테이블 확인](<../이미지/240403/댓글 참조관계 테이블확인 .png>)

## 댓글 생성 연습
1. shell_plus 실행 및 게시글 작성
    
    ![댓글 생성 연습1](<../이미지/240403/댓글 생성 연습1.PNG>)

2. 댓글 생성
    
    ![댓글 생성 연습2](<../이미지/240403/댓글 생성 연습2.PNG>)

3. shell_plus 실행 및 게시글 작성
* 이 때, 참조하는 외래키 데이터를 작성할 때 직접 키값을 넣지 않고 참조할 인스턴스를 연결해 주기(자동으로 pk연결)

    ![댓글 생성 연습3](<../이미지/240403/댓글 생성 연습3.PNG>)

4. comment 인스턴스를 통한 article 값 참조하기
* comment에 연결된 article을 호출할 수 있음
    
    ![댓글 생성 연습4](<../이미지/240403/댓글 생성 연습4.PNG>)

5. comment 인스턴스를 통한 article 값 참조하기
    
    ![댓글 생성 연습5](<../이미지/240403/댓글 생성 연습5.PNG>)

6. 두번째 댓글 생성

    ![댓글 생성 연습6](<../이미지/240403/댓글 생성 연습6.PNG>)

7. 작성된 댓글 데이터 확인

    ![댓글 생성 연습7](<../이미지/240403/댓글 생성 연습7.PNG>)

# 관계 모델 참조
## 역참조
* N:1관계에서 1에서 N을 참조하거나 조회하는 것, 1->N
* N은 외래 키를 가지고 있어 물리적으로 참조가 가능하지만 1은 N에 대한 참조 방법이 존재하지 않아 별도의 역참조 기능이 필요
### 역참조 QuerySet API
* 모델.참조_set.API 형태로 작성
* article= 모델, comment= article을 참조하는 모델, all()= querysetAPI
* _set은 복수형의 형태를 나타냄
* 

    ![역참조](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240403/%EC%97%AD%EC%B0%B8%EC%A1%B0.PNG)
    ![역참조 예시](<../이미지/240403/역참조 예시.PNG>)

### related manager
* N:1혹은 M:N관계에서 역참조 시에 사용하는 매니저== 역참조 대상클래스 이름_set
* 'objects' 매니저를 통해 QuerySet API를 사용했던 것처럼 related manager를 통해 QuerySet API를 사용할 수 있게 됨
* related manager 이름 규칙
    * N:1관계에서 생성되는 Related manager의 이름은 참조하는 '모델명_set' 이름 규칙으로 만들어짐
    * 특정 댓글의 게시글 참조(Comment -> Article)
        - comment.article
    * 특정 게시글의 댓글 목록 참조(Article -> Comment)
        - article.comment_set.all()

# 댓글 구현
## CREATE
### 댓글 CREATE 구현
1. 사용자로 댓글 데이터를 입력받기 위한 CommentForm 정의
    ![댓글 create 구현1](<../이미지/240403/댓글 create 구현1.PNG>)
2. detail view 함수에서 CommentForm을 사용하여 detail 페이지에 렌더링

    ![댓글 create 구현2](<../이미지/240403/댓글 create 구현2.PNG>)
    ![댓글 create 구현2-2](<../이미지/240403/댓글 create 구현2-2.PNG>)
3. Comment 작성시 Form을 그대로 넘겨주기 때문에 Article 선택창이 생김
    * Comment 클래스의 외래키 필드 article 또한 데이터 입력이 필요한 필드이므로 출력
    * 하지만 외래키 필드 데이터는 사용자로부터 입력 받는 값이 아닌 view 함수 내에서 다른 방법으로 전달 받아 저장해야함

    ![댓글 create 구현3](<../이미지/240403/댓글 create 구현3.PNG>)
    
    * CommentForm의 출력 필드를 조정하여 외래 키 필ㄷ드가 출력되지 않도록 함

    ![댓글 create 구현4](<../이미지/240403/댓글 create 구현4.PNG>)

4. URL을 통해 외래키를 전달
    
    ![댓글 create 구현5](<../이미지/240403/댓글 create 구현5.PNG>)

5. comment_create view 함수를 정의
* url에서 넘겨받은 pk 인자를 게시글을 조회하는 데 사용
    
    ![댓글 create 구현6](<../이미지/240403/댓글 create 구현6.PNG>)
* save(commit=False)
    * DB에 저장하지 않고 인스턴스만 반환
    * aritcle 객체를 저장하기 위해서 사용
* save의 commit인자를 활용해 외래 키 데이터를 추가 입력
    
    ![댓글 create 구현7](<../이미지/240403/댓글 create 구현7.PNG>)
* 댓글 조회까지 추가된 view함수
    
    ![실제 댓글create view함수](<../이미지/240403/실제 comment create view함수.PNG>)

## READ
* detail view 함수에서 전체 댓글 데이터를 조회

    ![댓글 Read 구현1](<../이미지/240403/댓글 Read 구현1.PNG>)
    ![댓글 Read 구현2](<../이미지/240403/댓글 Read 구현2.PNG>)

## DELETE
1. 댓글 삭제 url 작성
    
    ![댓글 Delete 구현1](<../이미지/240403/댓글 Delete 구현.PNG>)
2. 댓글 삭제 view함수 정의
    
    ![댓글 Delete 구현2](<../이미지/240403/댓글 Delete 구현2.PNG>)
3. 댓글 삭제 버튼 작성
    
    ![댓글 Delete 구현3](<../이미지/240403/댓글 Delete 구현3.PNG>)
4. 댓글 삭제 버튼 출력 확인 및 삭제 테스트
    
    ![댓글 Delete 구현4](<../이미지/240403/댓글 Delete 구현4.PNG>)

# 참고
* admin site 등록
    * comment 모델을 admin site에 등록해 CRUD 동작 확인하기

    ![admin page등록](<../이미지/240403/comment를 admin page 등록.PNG>)

* 댓글이 없는 경우 대체 콘텐츠 출력
    * DTL의 'for empty'태그 활용
    
    ![for empty](<../이미지/240403/for empty태그.PNG>)

* 댓글 개수 출력하기
    * DTL filter - 'length' 사용
```html
{{comments|length}}    
{{article.comment_set.all|length}}
```
    * QuerySet API - 'count()' 사용
```html
{{article.comment_set.count}}
```
