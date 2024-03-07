# 웹
* World Wide Web
    * 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간
## Web
* Web site, Web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술
* 인터넷에서 여러개의 Web page가 모인것으로, 사용자들에게 정보나 서비스를 제공하는 공간

## Web page
* HTML, CSS등의 웹 기술을 이용하여 만들어진, 'Web site'를 구성하는 하나의 요소
![비유](%EC%9D%B4%EB%AF%B8%EC%A7%80/240306/web%EA%B5%AC%EC%84%B1.PNG)![구성요소](<이미지/240306/webpage 구성요소.PNG>)

# HTML
* HyperText Markup Language 웹페이지의 의미와 구조를 정의하는 언어

## Hypertext
* 웹페이지를 다른 페이지로 연결하는 링크
* 참조를 통해 사용자가 한문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
![hypertext](%EC%9D%B4%EB%AF%B8%EC%A7%80/240306/hypertext.PNG)
## Markup Language
* 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
* ex) HTML, Markdown

마크업을 적용 안했을때

![markup example](%EC%9D%B4%EB%AF%B8%EC%A7%80/240306/Markup%EC%A0%81%EC%9A%A9x.PNG)

마크업을 적용했을때

![markup](<이미지/240306/Markup 적용.PNG>)

![markup language](%EC%9D%B4%EB%AF%B8%EC%A7%80/240306/Markup.PNG)

# 웹 구조화
<\!DOCTYPE html>
- 해당 문서가 html로 문서라는 것을 나타냄

\<html>\</html>
- 전체 페이지의 콘텐츠를 포함

\<title>\</title>
- 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용

\<head>\</head>
- HTML 문서에 관련된 설명, 설정 등
- 사용자에게 보이지 않음

\<body>\</body>
- 페이지에 표시되는 모든 콘텐츠
![HTML 구조](<이미지/240306/HTML 구조.PNG>)

## HTML Element(요소)
![HTML 요소](<이미지/240306/HTML 요소.PNG>)
* 하나의 요소는 여는 태그와 닫는 태그 그리고 그안의 내용으로 구성됨
* 닫는태그는 태그 이름 앞에 슬래시가 포함되며 닫는 태그가 없는 태그도 존재
* \<p>는 paragraph

## HTML Attributes(속성)
![속성](<이미지/240306/HTML 속성.PNG>)
속성="값" 형태(html은 쌍따옴표를 사용)
* 규칙
    * 속성은 요소 이름과 속성 사이에 공백이 있어야 함
    * 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함(콤마를 사용하지 않음)
    * 속성 값은 열고 닫는 따옴표로 감싸야 함
* 목적
    * 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
    * CSS에서 해당 요소를 선택하기 위한 값으로 활용됨
![구조예시](<이미지/240306/HTML 구조 예시.PNG>)


```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>My page</title>
</head>

<body>
    <p>My page</p>
    <!--a는 Anchor (하이퍼 텍스트)-->
    <a href="http://www.google.co.kr/">Google</a>
    <!--이미지는 닫는태그가 없다 -> 열고닫는게 있다는 것은 컨텐츠가 있다는 의미이므로 컨텐츠가 없다는 뜻-->
    <img src="images/sample.png" alt="">
    <!--이미지 태그는 속성값만 필요함, src==source==파일 경로, alt == 이미지가 호출이 안될경우 대체될 텍스트 -->
</body>
</html>
```
VScode의 확장프로그램 중 open in browser를 사용하면 alt+b를 눌러서 vscode에서 바로 html 실행가능

크롬의 F12를 눌러보면 개발자 도구를 볼수 있는데 HTML의 디버깅 도구라고 보면 됨. 개발자 도구의 Element탭 위주로 확인해서 어떤 요소가 되어 있는지 확인을 필수로 해야함!

# Text Structure
## HTML Text structure
* HTML의 주요 목적 중 하나는 텍스트 구조와 의미를 제공하는 것

## HTML
* 웹페이지의 의미와 구조를 정의하는 언어 = 구조를 잡는 언어

* \<h1>Heading\</hi>
  * 예를 들어 h1요소는 단순히 텍스트를 크게만 만드는 것이 아닌 현재 문서의 최상위 제목이라는 의미를 부여하는 것
  * 하나의 html문서에는 h1태그를 하나만 쓰는 것을 권장
* 대표적인 HTML Text structure
  * Heading & Paragraphs
    * h1~6,p
  * Lists
    * ol(숫자가 있는 리스트),ul(숫자가 없는 리스트),li(리스트 내 개별 요소)
  * Emphasis & Importance
    * em, strong
  
* 구조를 잡고 코드로 옮기는 연습을 우선적으로 진행 해야함!
* 아래 코드의 구조
![구조잡기](%EC%9D%B4%EB%AF%B8%EC%A7%80/240306/%EA%B5%AC%EC%A1%B0%EC%9E%A1%EA%B8%B0.png)
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>My page</title>
</head>

<body>
    <h1>Heading</h1>
    <h2>Sub Heading</h2>
    <p>texttext</p>
    <!--emphasis는 기울임-->
    <p>this is<em>emphasis</em></p>
    <!--strong은 bold-->
    <p>Hi<strong>myname</strong> is Air</p>
    <!--ol ordered list 순서번호로 나옴, ul unordered list 순서없는 목록으로 나옴-->
    <ol>
        <li>파이썬</li>
        <li>알고리즘</li>
        <li>웹</li>
    </ol>
    <ul>
        <li>파이썬</li>
        <li>알고리즘</li>
        <li>웹</li>
    </ul>
</body>
</html>
```
* MDN에서 웹기술에 대한 전반 기술에 대한 표준문서를 만들어 놓았기 때문에 모든 검색을 여기서 확인할것 (ex: h1 tag mdn)

# 웹스타일링
## CSS
* Cascading Style Sheet
* 웹 페이지의 디자인과 레이아웃을 구성하는 언어

![Css 적용x](<이미지/240306/css 적용x.PNG>)

![css구문](<이미지/240306/css 구문.PNG>)
* 값을 입력할 경우 단위를 만드시 사용해야함.
* font-size의 기본값(rem) ==16px, font-size :1.5 rem;이라고 적으면 24 px를 의미함
* 하나의 선언이 끝나면 세미콜론을 무조건 찍어주어야함

## CSS 적용방법
1. 인라인(Inline)스타일
    * HTML 요소 안에 style 속성 값으로 작성
  
  ![인라인](%EC%9D%B4%EB%AF%B8%EC%A7%80/240306/%EC%9D%B8%EB%9D%BC%EC%9D%B8.PNG)
2. Internal style
    * head 태그 안에 style 태그에 작성

![내부 스타일](%EC%9D%B4%EB%AF%B8%EC%A7%80/240306/%EB%82%B4%EB%B6%80%EC%8A%A4%ED%83%80%EC%9D%BC.PNG)

3. External style
    * 별도의 CSS 파일 생성후 HTML link 태그를 사용해 불러오기

![외부css](<이미지/240306/외부 css.PNG>)

* 재사용성이 제일 좋은 3번형식을 파일의 규모가 커질 경우 사용하고, 2번 방법도 많이 사용함
* 인라인 방법은 주로 테스트 용도로 사용

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <!--head안에 style태그를 만들면 css 공간이 만들어짐==internal style-->
  <style>
    h2{
      color: red;
    }
  </style>
  <!--외부스타일은 link:css로 호출 가능-->
  <link rel="stylesheet" href="style.css">
</head>

<body>
  <!--아래를 인라인 스타일변경이라고 함-->
  <h1 style="color: blue;background-color: yellow;">Inline Style</h1>
  <h2>Internal Style</h2>
  <h3>External Style</h3>
</body>

</html>

```

# CSS 선택자(중요!)
## CSS Selectors
* HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자

### 선택자 종류
* 기본 선택자
    *  전체 선택자 (*)
       *  HTML 모든 요소를 선택
    *  요소(tag) 선택자
       *  지정한 모든 태그를 선택
    *  클래스(class) 선택자(.)
       *  주어진 클래스 속성을 가진 모든 요소를 선택
    *  아이디(id) 선택자(#)
       *  주어진 아이디 속성을 가진 요소 선택
       *  문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함(두번쓴다고 에러가 발생하지는 않지만 권장하지 않은 표기, 왜냐면 우선순위가 아이디 선택자가 더 높기 때문에)
    *  속성(attr) 선택자 등
       *  속성 값을 선택 ([속성=값])
* 결합자
    * 자손 결합자(' '(space)) = 자식 + 손주
    * 자식 결합자(>)

![css 선택자](<이미지/240306/css 선택자.PNG>)


* google에 css bento라고 검색하면 css dinner라는 페이지에서 선택자와 결합자를 찾아가는 연습가능(움직이는 그림의 선택자를 입력)
* 
![css bento 예시](<이미지/240306/css bento.PNG>)


```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    *{
      color:red;
    }
    h2{
      color: orange;
    }
   
    h3,
    h4{
      color: blue;
    }
    .green{
      color: green;
    }
    #purple{
      color: purple;
    }
    .green > span{
      font-size: 50px;
    }
    .green li{
      color:brown;
    }
  </style>
   <!--위의 h3,h4처럼 콤마로 연결하는 경우, 스타일 가이드 상 엔터로 분리시켜주기를 바람-->
</head>

<body>
  <h1 class="green">Heading</h1>
  <h2>선택자</h2>
  <h3>연습</h3>
  <h4>반가워요</h4>
  <p id="purple">과목 목록</p>
  <!--ul태그 안에 웹리스트의 ol의 html에 접근하려면 2단계 아래이므로 자손태그로 접근해야함-->
  <ul class="green">
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>웹
      <ol>
        <li>HTML</li>
        <li>CSS</li>
        <li>PYTHON</li>
      </ol>
    </li>
  </ul>
  <p class="green">Lorem, <span>ipsum</span> dolor.</p>
</body>

</html>

```
![셀렉터 예시](<이미지/240306/selector 예시.PNG>)

* HTML 문서는 프로그래밍 언어랑 다르게 잘못될 경우 에러를 발생시키지 않고 적용하지 않음, 그래서 잘못 작성한 코드를 직접 찾아야함

# 명시도(중요!)
## 명시도(Specificity)
* 결과적으로 요소에 적용할 CSS선언을 결정하기 위한 알고리즘
* 동일한 요소를 가리키는 2개이상의 CSS 규칙이 있는 경우 가장 높은 명시도를 가진 Selector가 승리하여 스타일이 적용됨
* 전체선택자는 낮은 편, 왜냐면 전체선택자과 같이 다른 선택자를 사용할 경우 다른 선택자가 우선적용되므로


## Cascade 계단식
* 한 요소에 동일한 가중치를 가진 선택자가 적용될때 CSS에서 마지막에 나오는 선언이 사용됨
```html
  h1{
    color : red;
  }
  h1{
    color :purple;
  }
```
h1태그 내용은 purple 색이 적용됨

## 명시도 높은순
1. Importance
    - !important
2. Inline 스타일
3. 선택자
   - id 선택자>class 선택자 > 요소 선택자
4. 소스 코드 선언 순서

### 명시도 적용 예시
* *동일한* h1 태그에 아래와 같이 스타일이 작성된다면 h1 태그 내용의 색은 red가 적용됨
```html
코드예시
.make-red{
    color : red;
}
h1{
    color : purple;
}

<h1 class ='make-red'> # 같은 태그이므로 명시도를 따져서 class인 빨간색
<div class='make-red'>
    <h1> hello </h1> # 다른 태그이므로 h1 기준인 보라색
</div>

명시도를 따질 때에는 동일한 태그인지 여부가 중요, 동일한 위치의 태그이라면 명시도를 고려하지만 그게 아니라면 태그 기준으로 들어감
```
*

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    h2 {
      color: darkviolet !important;
    }

    p {
      color: blue;
    }

    .orange {
      color: orange;
    }

    .green {
      color: green;
    }

    #red {
      color: red;
    }
  </style>
</head>

<body>
  <p>1</p><!--파랑-->
  <p class="orange">2</p> <!--오렌지-->
  <p class="green orange">3</p> <!--그린 클래스내부에 작성하는 건 그냥 2개를 작성하는 것이고 css(style)에서 선언된 순서가 orange green 순서이므로 그린이 적용됨-->
  <p class="orange green">4</p> <!--그린-->
  <p id="red" class="orange">5</p><!--레드 id가 우선순위가 더 높음-->
  <h2 id="red" class="orange">6</h2><!--다크바이올렛 !important-->
  <p id="red" class="orange" style="color: brown;">7</p><!--브라운 인라인 선택자-->
  <h2 id="red" class="orange" style="color: brown;">8</h2><!--다크바이올렛 !important-->


</body>

</html>

```
## !important
* 다른 우선 순위 규칙보다 우선하여 적용하는 키워드
* Cascade의 구조를 무시하고 강제로 스타일을 적용하는 방식이므로 사용을 권장하지 않음


# CSS 상속
* 기본적으로 CSS는 상속을 통해 부모요소의 속성을 자식에게 상속해 재사용성을 높임
* 상속되는 속성
    - Text 관련 요소!(front,color, text-align), opacity,visibility 등
* 상속되지 않는 속성
    - Box model 관련요소(width, height, border, box-sizing)
    - position 관련 요소(position, top/right/bottom.left,z-index) 등

* 상속 여부는 MDN 문서에서 확인하기

![MDN](<이미지/240306/상속 MDN.PNG>)

![상속 예시](%EC%9D%B4%EB%AF%B8%EC%A7%80/240306/%EC%83%81%EC%86%8D.PNG)

![결과](<이미지/240306/상속 결과.PNG>)

# 참고
## HTML 관련사항
* 요소(태그) 이름은 대소문자를 구분하지 않지만 '소문자' 사용을 권장
* 속성의 따옴표는 작은 따옴표와 큰 따옴표를 구분하지 않지만 '큰 따옴표' 권장
* HTML은 프로그래밍 언어와 달리 에러를 반환하지 않기 때문에 작성시 주의
## CSS 인라인스타일은 사용하지 말것
* CSS와 HTML 구조 정보가 혼합되어 작성되기 때문에 코드를 이해하기 어렵게 만듦
## CSS의 모든 속성을 외우는 것이 아님
* 자주 사용되는 속성은 그리 많지 않으며 주로 활용하는 속성 위주로 사용하다 보면 자연습럽게 익히게 됨
* 그 외 속성들은 

## 속성은 되도록 'class'만 사용할 것 (중요!)
* id, 요소 선택자 등 여러 선택자들과 함께 사용할 경우 우선순위 규칙에 따라 예기치 못한 스타일 규칙이 적용되어 전반적인 유지보수가 어려워지기 때문
* 문서에서 단 한번 유일하게 적용될 스타일에 경우에만 'id 선택자' 사용을 고려
