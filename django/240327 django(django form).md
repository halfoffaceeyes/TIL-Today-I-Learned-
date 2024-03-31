# HTML form
* 지금까지 사용자로부터 데이터를 받기 위해 활용한 방법 그러나 비정상적 혹은 악의적인 요청을 필터링 할 수 없음
* 유효한 데이터인지 확인을 안함

## 유효성 검사
* 수집한 데이터가 정확한지 유효한지 확인하는 과정
### 유효성 검사 구현
* 유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등 많은 것들을 고려해야 함
* 이런 과정과 기능을 직접 개발하는 것이 아닌 Django가 제공하는 Form을 사용

# Form Class
## Django Form
* 사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구

> 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공

![form class](<../이미지/240327/Form class 정의.PNG>)

![form class 적용1](<../이미지/240327/form class 적용1.PNG>)

![form class 적용2](<../이미지/240327/form class 적용2.PNG>)

![form class 적용결과](<../이미지/240327/form class 적용결과.PNG>)

## Form rendering options
* label, input 쌍을 특정 HTML 태그로 감싸는 옵션

https://docs.djangoproject.com/en/4.2/topics/forms/#form-rendering-options

![Form rendering options](<../이미지/240327/Form rendering options.PNG>)

![Form rendering options 결과](<../이미지/240327/Form rendering options 결과.PNG>)

# Widgets
* HTML 'input' element의 '표현'을 담당(CSS를 입히는 것과 비슷한 역할)
* Widget은 단순히 input요소의 속성 및 출력되는 부분을 변경하는 것
* 위의 예시들에서 django form으로 형성할 경우 content에 입력하는 부분이 textfield로 설정되어 크기가 작은데 forms.py에서 widget으로 속성을 textarea로 지정해줄경우 크기 조절이 가능하게 속성값을 입힐 수 있음

https://docs.djangoproject.com/ko/4.2/ref/forms/widgets/#built-in-widgets

# Django ModelForm
## Form vs ModelForm
* Form : 사용자 입력 데이터를 DB에 저장하지 않을 때(ex.로그인)
* ModelForm : 사용자 입력 데이터를 DB에 저장해야 할 때(ex. 게시글 작성, 회원가입)

## ModelForm
* Model과 연결된 Form을 자동으로 생성해주는 기능을 제공(Form + model)
==> django가 Model을 알아서 해석해서 ModelForm을 형성해줌
* ModelForm을 쓰는 이유는 유효성검사를 하기 위해 사용(DB에 저장하기 위해서는 유효성검사가 필요함)

![ModelForm class 정의](<../이미지/240327/ModelForm class 정의.PNG>)

![ModelForm class 결과](<../이미지/240327/ModelForm class 결과.PNG>)
fields = 튜플, 리스트 형태의 컬럼명
ex) field = (title, content)도 사용 가능
### Meta class
* ModelForm의 정보를 작성하는 곳
* Meta class는 모델정보, 필드 정보가 필수로 입력되어야 함.(model = 모델종류, fields = 어떤필드를 사용할지)
* Meta Data = 데이터를 위한 데이터

* ex) 사진(데이터)<br>
    - 사진의 메타 데이터<br>
        * 조리개값<br>
        * 날짜<br>
        * 위치<br>

* 'fields' 및 'exclude'속성
    * exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수도 있음
    * exclude는 빼는게 더 빠를때 사용

![model field exclude](<../이미지/240327/Modelform field and exclude.PNG>)

* Modelform의 구조
    * class Modelform -> class meta -> 모델지정 및 필드 지정
    * view함수에서 반드시 import를 해줘야함

* Modelform을 사용하면 사용자에게서 받아오는 입력값에 대해 알아서 해석 해서 form을 제공 (예를들어, 수정시간이나 등록시간의 경우에는 사용자가 입력하는 것이 아니라 자동으로 형성되므로 form에 형성하지 않음)
* ModelForm의 save()는 리턴값이 있음

![Modelform 적용 Creat 함수 변화](<../이미지/240327/ModelForm 적용한 create.PNG>)

* ModelForm에서 유효성 검사를 통과하지 못할 경우, 에러메세지를 Form의 Data에 반환하기 때문에 if절 아래의 content에 form을 새로 담아서 다시 렌더링을 해서 결과를 확인

![ModelForm 적용한 create 결과](<../이미지/240327/ModelForm 적용한 create 결과.PNG>)

### is_valid()
* 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean으로 변환
* 공백 데이터가 유효하지 않은 이유: 별도로 명시하지 않았지만 모델 필드에는 기본적으로 빈값은 허용하지 않는 제약 조건이 설정 되어 있음
* 빈값은 is_valid()에 의해 False로 평가되고 form 객체에는 그에 맞는 에러 메시지가 포함되어 다음 코드로 진행됨

* 에러가 발생하면 에러가 값이 Form에 담김 -> 에러가 담긴 Form을 새로운 HTML에 담아서 표현하기 위해 redirect가 아니라 render를 사용

* ModelForm을 적용한 edit 로직
![ModelForm edit](<../이미지/240327/ModelForm edit.PNG>)

* ModelForm을 적용한 update 로직
![ModelForm update](<../이미지/240327/ModelForm update로직.PNG>)

## save
* save()메서드가 생성과 수정을 구분하는 법
    * 키워드 인자 instance여부를 통해 생성할 지, 수정할 지를 결정
    * instance가 있으면 update, 없으면 create
* update과정은 create의 코드와 유사한데, 이때 생성인지 수정인지 확인하는 코드는 instance=article의 유무 -> instance로 원래에 있던 article을 넣어주면서 수정이라는 것을 알려주게됨

# Handling HTTP requests
## view 함수 구조 변화
외우지 말고 흐름을 잡자!
### new + create
* new와 create는 데이터 생성을 구현하기 위한 함수라는 공통점이 있지만,
* new는 GET method 요청만을, create는 POST method 요청만을 처리
* 두 함수를 결합할 수 있음
* 노란 영역의 POST에서 유효성 검사를 통과하지 못한다면 아래 context로 넘어가 에러메시지가 담긴 페이지가 나올 수 있도록 context의 위치를 조심해야함. else밖에 있도록

![new+create](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240327/new+create.PNG)

* 공통점과 차이점을 이용
    * 두함수의 유일한 차이점이었던 request method에 따른 분기
    * POST일 때는 과거 create 함수 구조였던 객체 생성 및 저장 로직 처리
    * POST가 아닐 때는 과거 단순히 form 인스턴스 생성
* 함수를 합친 후 URL 제거 및 view함수 경로, templates 경로 수정

![사용안하는 경로 제거](<../이미지/240327/new에서 create로 변경.PNG>)

![URL 수정](<../이미지/240327/view함수 변경.PNG>)

![템플릿 수정](<../이미지/240327/create 수정.PNG>)

* request method에 따른 요청의 변화
    * GET : articles/create  == 게시글 생성 문서를 줘!
    * POST : articles/create == 게시글을 생성해줘!

### edit + update
![edit + update](<../이미지/240327/edit + update.PNG>)

![edit+update url 수정](<../이미지/240327/edit+update url 수정.PNG>)

![edit+update 템플릿 수정](<../이미지/240327/edit+update 템플릿 수정.PNG>)


# 참고
## ModelForm 키워드 인자 data와 instance 살펴보기
![basemodelform](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240327/basemodelform.PNG)

## widget 응용
* Form에 class를 입히고 싶을 경우 model에 field를 직접 설정해주어야함.(widget은 form에 상속되어 있기 때문에)
* widget의 class안의 attrs(attributes)에 원하는 속성(css class)을 입혀줄 수 있음.
* widget은 meta class 위쪽에 작성하는 것을 권장
![widget응용](<../이미지/240327/widget 응용2.PNG>)


## 필드 수동 랜더링
https://docs.djangoproject.com/en/4.2/topics/forms/#rendering-fields-manually

![필드 수동랜더링](<../이미지/240327/필드 수동랜더링.PNG>)

## CRUD 작성
CRUD를 작성할 때, 구조를 잡고 시작하는 것이 중요 예를들어
```py
def create(request):
    if requset.method=='POST':
        pass
    else:
        pass # 여기부터 완성하고 위에를 적어야함
```