# Many to many relationships N:M or M:N
* 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
* 양쪽 모두에서 N:1관계를 가짐
# N:1의 한계
## 의사와 환자 간 모델 관계 설정
* 한명의 의사에게 여러 환자가 예약할 수 있도록 설계
![의사와 환자간 모델 관계](<../이미지/240408/의사와 환자간 모델 관계.PNG>)
![의사와 환자간 모델 관계2](<../이미지/240408/의사와 환자간 모델 관계2.PNG>)
* 결과
![의사와 환자간 모델 관계 결과](<../이미지/240408/의사와 환자간 모델 관계 테이블 생성.PNG>)

* 이 때 1번환자(carol)가 두 의사 모두에게 진료를 받고자 한다면 환자 테이블에 1번 환자 데이터가 중복으로 입력될 수 밖에 없음
* 동일한 환자지만 다른 의사에게도 진료받기 위해 예약하기 위해서는 객체를 하나 더 만들어 진행해야함 => 외래 키 컬럼에 1,2 형태로 저장하는 것은 DB타입 문제로 불가능하기 때문에 테이블을 따로 만들어야함

# 중개 모델
## 예약모델 생성
* 환자 모델의 외래 키를 삭제하고 별도의 예약 모델을 새로 생성
* 예약 모델은 의사와 환자에 각각 N:1 관계를 가짐
![중개 모델 1](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240408/%EC%A4%91%EA%B0%9C%EB%AA%A8%EB%8D%B81.PNG)
![중개 모델 2](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240408/%EC%A4%91%EA%B0%9C%EB%AA%A8%EB%8D%B82.PNG)

* 의사와 환자가 예약 모델을 통해 각각 본인의 진료 내역 확인
![중개 모델 3](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240408/%EC%A4%91%EA%B0%9C%EB%AA%A8%EB%8D%B83.PNG)
* 동일한 의사에게 새로운 환자 예약 가능
![중개 모델 4](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240408/%EC%A4%91%EA%B0%9C%EB%AA%A8%EB%8D%B84.PNG)

* Django에서는 'ManyToMany Field'로 중개 모델을 자동으로 생성

# ManyToManyField
* M:N 관계 설정 모델 필드
* 환자 모델에 ManyToManyField 작성
    - 의사 모델에 작성해도 상관 없으며 참조/역참조 관계만 잘 기억할 것
    
![ManyToManyField 설정](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240408/ManyToManyField.PNG)

* hospitals_patient_doctors라는 중개 테이블 형성

* 의사 1명 환자 2명 생성후, 예약 생성 및 제거
    * 생성 : add
        * 환자가 의사를 참조하고 있기 때문에 환자에서 생성시 patient1.doctors.add(doctor1)
        * 의사는 환자를 역참조하여 생성가능
        doctor1.patient_set.add(patient2)
        ![Many to many 테이블 생성](<../이미지/240408/MNtable 형성.PNG>)
    * 제거 : remove
![예약 생성 제거](<../이미지/240408/ManyToManyField 생성 제거.PNG>)

# 'through' argument
* 중개 테이블에 '추가 데이터'(증상, 예약일과 같은 데이터)를 사용해 M:N 관계를 형성하려는 경우에 사용
* Resevation Class 재작성 및 through 설정
![through argument](<../이미지/240408/through argument.PNG>)

* 예약 생성 1 : Reservation class를 사용한 예약 생성
![through argument 예약생성](<../이미지/240408/through argument 생성1.PNG>)

* 예약 생성 2 : Patient 또는 Doctor의 인스턴스를 통한 예약 생성(through_defaults)
![through default 사용](<../이미지/240408/through default.PNG>)

* 결과
![테이블 생성 결과](<../이미지/240408/through 결과.PNG>)
    * 생성과 마찬가지로 의사와 환자 모두 각각 예약 삭제 가능

![field 삭제 가능](<../이미지/240408/ManyToManyField 특징.PNG>)

# M:N 관계 주요 사항
* M:N 관계로 맺어진 두테이블에는 물리적인 변화가 없음
* ManyToManyField는 중개 테이블을 자동으로 생성
* ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음
    - 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것
* N:1은 완전한 종속의 관계였지만 M:N은 종속적인 관계가 아니며 '의사에게 진찰받는 환자 & 환자를 진찰하는 의사' 이렇게 2가지 형태 모두 표현 가능

# ManyToManyField
* ManyToManyField(to,**options) : M:N관계 설정 시 사용하는 모델 필드
* 대표인자 세가지
    * related_name
    * symmetrical
    * through

1. 'related_name' arguments
* 역참조의 이름을 변경
![related_name](<../이미지/240408/related name.PNG>)

2. 'symmetrical' arguments
* 관계 설정 시 대칭 유무 설정
* ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용
* 기본값: True
![symmetrical](<../이미지/240408/symmetrical argument.PNG>)

* True일 경우
- source모델(관계를 시작하는 모델)의 인스턴스가 target모델(관계의 대상이 되는 모델)의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source모델 인스턴스를 자동으로 참조하도록함(대칭)
- 즉, 내가 당신의 친구라면 자동으로 당신도 내친구가 됨

* False일 경우
- True와 반대(대칭되지 않음)

3. 'through' arguments
* 사용하고자 하는 중개모델을 지정
* 일반적으로 추가 데이터를 M:N관계와 연결하려는 경우에 활용
![through argument](<../이미지/240408/through argu.PNG>)

## M:N에서의 대표 methods
* add()
    - '지정된 객체를 관련 객체 집합에 추가'
    - 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
* remove()
    * '관련 객체 집합에서 지정된 모델 객체를 제거'

# 좋아요 기능 구현
## 모델 관계 설정
* Article(M) - User(N)
    * 0개 이상의 게시글은 0명 이상의 회원과 관련
    * 게시글은 회원으로부터 0개 이상의 좋아요를 받을 수 있고, 회원은 0개 이상의 게시글에 좋아요를 누를 수 있음

![모델 관계 설정](<../이미지/240408/모델 관계 설정.PNG>)

* 역참조 에러 발생 : 기존의 Foreign key(user)와 like_users간 충돌 발생
![모델 관계 설정 2](<../이미지/240408/모델 관계 설정2.PNG>)
    * 역참조 매니저 충돌
        * N:1
            * 유저가 작성한 게시글
            * user.article_set.all()
        * M:N
            * 유저가 좋아요한 게시글
            * user.article_set.all()
        * like_users필드 생성 시 자동으로 역참조 매니저 .article_set가 생성됨
        * 그러나 이전 N:1(Article-User)관계에서 이미 같은 이름의 매니저를 사용 중
        - user.article_set.all()->해당 유저가 작성한 모든 게시글 조회
        - user가 작성한 글(user.article_set)과 user가 좋아요를 누른 글(user.article_set)을 구분할 수 없게 되므로 둘 중 하나에 related_name 작성 필요

* 변경된 모델
![모델 관계 설정3](<../이미지/240408/모델 관계 설정3.PNG>)
    
### User-Article 간 사용 가능한 전체 related manager
* article.user : 게시글을 작성한 유저 - N:1
* user.article_set : 유저가 작성한 게시글(역참조) - N:1
* article.like_users : 게시글을 좋아요 한 유저 - M:N
* user.like_articles : 유저가 좋아요 한 게시글(역참조) - M:N

## 기능 구현
* url 작성
![좋아요url](<../이미지/240408/좋아요 url.PNG>)
* view함수 작성
![좋아요view](<../이미지/240408/좋아요 view.PNG>)
* index 템플릿에서 각 게시 글에 좋아요 버튼 출력
![좋아요 버튼](<../이미지/240408/좋아요 버튼.PNG>)
* 출력 확인
![좋아요 기능 구현](<../이미지/240408/좋아요 기능 구현 확인.PNG>)