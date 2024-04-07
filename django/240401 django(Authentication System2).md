# 회원가입
* User 객체를 Create하는 과정

## UserCreationForm()
* 회원가입시 사용자 입력 데이터를 받는 Built-in ModelForm(Model Form이므로 데이터 베이스에 저장하기 위함)
* UserModel을 custom해서 바로 사용 못함.
* UserCreationForm은 modelForm이고 model정보로 django의 default user로 설정되어있음. 하지만 User custom을 한다면 django의 기본 유저를 사용하지 않기 때문에 model정보를 바꿔줄 필요가 있음
![회원가입 페이지 로직](<../이미지/240401/회원가입 페이지1.PNG>)
![회원가입 페이지](<../이미지/240401/회원가입 페이지.PNG>)
![회원가입 view함수](<../이미지/240401/회원가입 로직.PNG>)

* 회원가입 로직 에러

    * 회원가입에 사용하는 UserCreataionForm이 기존 유저 모델로 인해 작성된 클래스이기 때문
    * 대체한 유저모델로 변경 필요

* Manager isn't available; 'auth.User' has been swapped for 'accounts.User' ==django의 auth User를 사용할 수 없음, accounts.User로 변경되어서 == 기본 UserModel을 변경해줘야함

![회원가입 로직 에러](<../이미지/240401/회원가입 로직 에러.PNG>)

![유저모델 변경필요](<../이미지/240401/회원가입 로직 에러2.PNG>)

* 커스텀 유저 모델을 사용하려면 다시 작성해야 하는 Form
    * UserCreationForm
    * UserChangeForm
    * 두 Form 모두 class Meta: model = User가 작성된 Form

![UserCreationForm과 UserChangeForm 커스텀](<../이미지/240401/UsercreationForm UserChangeForm변경.PNG>)

* get_user_model()
    * auth 모듈에 등록된 Usermodel을 반환하는 함수
    * 현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환하는 함수
    * User 모델을 직접 참조 하지 않는 이유
        * get_user_model()을 사용해 User 모델을 참조하면 커스텀 User 모델을 자동으로 반환해주기 때문 == User모델의 이름을 변경하여도 수정하지 않고 자동으로 반환가능
        * Django는 필수적으로 User 클래스를 직접 참조하는 대신 get_user_model()을 사용해 참조해야한다고 강조하고 있음
        * from .models import User의 경우,코드 실행 순서로 인해 에러 발생가능성이 있기 때문에 사용하지 않음

* 회원가입 로직 작성(커스텀 Form 적용) == create로직과 동일

![회원가입 로직 작성](<../이미지/240401/회원가입 로직 작성.PNG>)

# 회원 탈퇴
* User 객체를 Delete하는과정
* 로그인한 user정보는 request.user에 담겨있음(삭제하려는 User를 조회할 필요가 없음)
* 로그인 하지 않으면 request.user에 AnonymousUser가 들어있음
* DB에서 삭제하기 때문에 POST

![회원탈퇴 로직](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240401/%ED%9A%8C%EC%9B%90%ED%83%88%ED%87%B4.PNG)

# 회원정보 수정
* User 객체를 Update하는 과정
* UserChangeFrom()
    * 회원정보 수정시 사용자 입력 데이터를 받는 built-in ModelForm

![회원정보 수정1](<../이미지/240401/회원 정보 수정페이지1.PNG>)
![회원정보 수정2](<../이미지/240401/회원 정보 수정페이지2.PNG>)
![회원정보 수정3](<../이미지/240401/회원 정보 수정페이지3.PNG>)

## UserChangeForm 사용 시 문제점
* User 모델의 모든 정보들(fields)까지 모두 출력되어 수정이 가능하기 때문에 일반 사용자들이 접근해서는 안되는 정보는 출력하지 않도록 해야함
* CustomUserChangeForm에서 접근 가능한 필드를 다시 조정
* fields 종류 정보 : https://docs.djangoproject.com/en/5.0/ref/contrib/auth/

![CustomUserChangeForm 출력 필드 재정의](<../이미지/240401/CustomUserChangeForm 출력 필드 재정의.PNG>)

![CustomUserChangeForm 출력 필드 재정의2](<../이미지/240401/CustomUserChangeForm 출력 필드 재정의2.PNG>)

# 비밀번호 변경
* 인증된 사용자의 Session 데이터를 Update하는 과정
## PasswordChangeForm()
* 비밀번호 변경 시 사용자 입력 데이터를 받는 built-in Form

## 비밀번호 변경 페이지 작성
* django는 비밀번호 변경 페이지를 회원정보 수정 form에서 별도 주소로 안내

# 세션 무효화 방지
* 암호 변경 시 세션 무효화
    * 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게되어 버려 로그인 상태가 유지되지 못하고 로그아웃 처리됨
    * 비밀번호가 변경 되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문

* update_session_auth_hash(request,user)
    * 암호 변경시 세션 무효화를 막아주는 함수
    * 암호가 변경되면 새로운 password의 Session Data로 기존 session을 자동으로 갱신

![update_session_auth](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240401/update_session_auth_hash.PNG)

# 인증된 사용자에 대한 접근 제한
* 로그인 사용자에 대한 접근을 제한하는 2가지 방법
1. is_authenticated 속성(attribute)
    * 사용자가 인증되었는지 여부를 알수 있는 User model의 속성
    * 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성이며, 비인증 사용자에 대해서는 항상 False
    * django에서는 request.user.is_authenticated 를 권장(user.is_authenticated도 가능하긴함)
   
* 로그인과 비로그인 상태에서 화면에 출력되는 링크를 다르게 설정가능

![is_authenticated 적용1](<../이미지/240401/is_authenticated 적용.PNG>)

* 인증된 사용자라면 로그인/회원가입 로직을 수행할 수 없도록 하기

![is_authenticated 적용2](<../이미지/240401/is_authenticated 적용2.PNG>)

2. login_required 데코레이터(decorator)
    * 인증된 사용자에 대해서만 view함수를 실행시키는 데코레이터
    * 비인증 사용자의 경우 /accounts/login/ 주소로 redirect 시킴(자동으로 accounts의 login으로 보내주기 때문에 accounts app의 이름이 중요)

* 인증된 사용자만 게시글을 작성/수정/삭제 할 수 있도록 수정

![login_required 적용1](<../이미지/240401/login_required 적용1.PNG>)

* 인증된 사용자만 로그아웃/탈퇴/수정/비밀번호 변경할 수 있도록 수정

![login_required 적용2](<../이미지/240401/login_required 적용2.PNG>)


# 참고
## is_authenticated 속성
* user 객체로 만들어졌으면 True 반환
https://github.com/django/django/blob/main/django/contrib/auth/base_user.py#L85

## 회원가입후 로그인 까지 이어서 진행하는 법
* signup후 로그인을 진행
![회원가입후 자동 로그인](<../이미지/240401/회원가입 후 로그인 자동.PNG>)

## 탈퇴와 함께 기존 사용자의 Session Data 삭제 방법
* 사용자 객체 삭제 이후 로그아웃 함수 호출
* 단, '탈퇴(1) 후 로그아웃(2)'의 순서가 바뀌면 안됨
* auth_logout은 request의 user정보를 AnonymousUser로 변경하기 때문에
* 먼저 로그아웃이 진행되면 해당 요청 객체 정보가 없어지기 때문에 탈퇴에 필요한 유저 정보 또한 없어져 진행 불가

![탈퇴와함께 세션 데이터 삭제](<../이미지/240401/탈퇴와함께 세션데이터삭제.PNG>)
