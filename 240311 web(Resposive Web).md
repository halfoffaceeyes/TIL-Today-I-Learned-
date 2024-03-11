# Emmet
* CSS와 HTML 자동완성으로 코드 작성이 가능하게 만들어준 플러그 인
* docs.emmet.io에서 검색
* emmet cheat sheet로 검색해서 연습해볼것
```html
p*3>lorem5
<p>Lorem ipsum dolor sit amet.</p>
<p>Nobis earum labore animi vero?</p>
<p>Voluptatibus sit quaerat qui at.</p>

div>.container>h1{Hello}+navi>ul>li*5>a{Link $}
<div>
    <div class="container">
        <h1>Hello</h1>
        <nav>
            <li><a href="">Link</a></li>
            <li><a href="">Link</a></li>
            <li><a href="">Link</a></li>
            <li><a href="">Link</a></li>
            <li><a href="">Link</a></li>
        </nav>
    </div>
</div>
```
# VS코드 유용한 단축키
1. ctrl+l : Line 선택 
2. ctrl+d : 동일한 키워드 연속 선택
3. ctrl+alt+화살표 : 멀티 커서
4. alt + 클릭 : 멀티 커서
5. alt+ 화살표 : 선택한 라인 끌고가기
6. alt + shift + 화살표 : 선택한 라인 복사

# Bootstrap Grid sytem
* flex를 기반으로 만들어진 grid
* 웹페이지의 레이아웃을 조정하는 데 사용되는 *12개의 컬럼*으로 구성된 시스템(12의 약수가 많아서 12개로 나눔)
* Grid system 목적
  * 반응형 디자인을 지원해 웹페이지를 모바일, 태블릿, 데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도움
## 반응형 웹디자인(Responsive Web Design)
* 디바이스 종류나 화면 크기에 상관없이, 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기능
  
![12개의 컬럼 사용 예시](<이미지/240311/12컬럼 예시.PNG>)

## Grid system 구조
1. Container(=row, class = 'container'랑 혼동하지 말것)
   * Column들을 담고 있는 공간
![container](<이미지/240311/grid system container.PNG>)
2. Column
   * 실제 컨텐츠를 포함하는 부분
![column](<이미지/240311/grid system column.PNG>)
3. Gutter
    * 컴럼과 컬럼 사이의 여백
![Gutter](<이미지/240311/grid system gutter.PNG>)

* 1개의 row 안에 12개의 column 영역이 구성
* 각 요소는 12개 중 몇개를 차지할 것인지 지정됨
![기본요소](<이미지/240311/grid system 기본요소.PNG>)
### Grid System 실습
* 기본

![기본예시](<이미지/240311/grid system 기본.PNG>)
* 중첩(Nesting)

![중첩예시](<이미지/240311/grid system Nesting.PNG>)


* 상쇄(Offset) - 특정 영역을 비우는 기능

![상쇄예시](<이미지/240311/grid system Offset.PNG>)

* Gutter : Grid system에서 column 사이에 여백 영역, x축은 padding, y축은 margin으로 여백 생성

![gutter 설명](<이미지/240311/grid system gutter예시.PNG>)

![gutter예시](<이미지/240311/grid system gutter 실습.PNG>)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <style>
    .box {
      border: 1px solid black;
      background-color: lightblue;
      text-align: center;
    }
  </style>
</head>

<body>
  <h2 class="text-center">Basic</h2>
  <div class="container">
    <div class="row">
      <div class="box col">col</div>
      <div class="box col">col</div>
      <div class="box col">col</div>
    </div>
    <div class="row">
      <div class="box col-4">col-4</div>
      <div class="box col-4">col-4</div>
      <div class="box col-4">col-4</div>
    </div>
    <div class="row">
      <div class="box col-2">col-2</div>
      <div class="box col-8">col-8</div>
      <div class="box col-2">col-2</div>
    </div>
  </div>

  <hr>

  <h2 class="text-center">Nesting</h2>
  <div class="container">
    <div class="row">
      <div class="box col-4">col-4</div>
      <div class="box col-8">
        <div class="">
          <div class="box col-6">col-6</div>
          <div class="box col-6">col-6</div>
          <div class="box col-6">col-6</div>
          <div class="box col-6">col-6</div>
        </div>
      </div>
    </div>
  </div>

  <hr>

  <h2 class="text-center">Offset</h2>
  <div class="container">
    <div class="row">
      <div class="box col-4">col-4</div>
      <div class="box col-4 offset-4">col-4 offset-4</div>
    </div>
    <div class="row">
      <div class="box col-3 offset-3">col-3 offset-3</div>
      <div class="box col-3 offset-3">col-3 offset-3</div>
    </div>
    <div class="row">
      <div class="box col-6 offset-3">col-6 offset-3</div>
    </div>
  </div>

  <hr>

  <h2 class="text-center">Gutters(gx-0)</h2>
  <div class="container">
    <div class="row gx-0">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>

  <br>

  <h2 class="text-center">Gutters(gy-5)</h2>
  <div class="container">
    <div class="row gy-5">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>


  <br>

  <h2 class="text-center">Gutters(g-5)</h2>
  <div class="container">
    <div class="row g-5">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
    crossorigin="anonymous"></script>
</body>

</html>

```
### The Grid System
* CSS가 아닌 편집 디자인에서 나온 개념으로 구성요소를 잘 배치해서 시각적으로 좋은 결과물을 만들기 위함
* 기본적으로 안쪽에 있는 요소들의 오와 열을 맞추는 것에서 기인
* 정보 구조와 배열을 체계적으로 작성하여 정보의 질서를 부여하는 시스템

![grid system](<이미지/240311/grid system.PNG>)


# Grid system for responsive web
## Responsive Web Design
* 디바이스 종류나 화면 크기에 상관없이, 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술
* Bootstrap grid system에서는 12개 column과 6개 breakpoints를 사용하여 반응형 웹 디자인을 구현

## Grid system breakpoints
* 웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점
* 화면 너비에 따라 6개의 분기점 제공(xs(기본),sm,md,lg,xl,xxl)
* 각 breakpoints 마다 설정된 최대 너비값 **이상으로** 화면이 커지면 grid system 동작이 변경됨
* 
* ![grid system breakpoint](<이미지/240311/grid system breakpoint.PNG>)

### breakpoints 실습
![breakpoints1](%EC%9D%B4%EB%AF%B8%EC%A7%80/240311/breakpoints1.PNG)
![breakpoints2](%EC%9D%B4%EB%AF%B8%EC%A7%80/240311/breakpoints2.PNG)
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <style>
    .box {
      border: 1px solid black;
      background-color: lightblue;
      text-align: center;
    }
  </style>
</head>

<body>
  <h2 class="text-center">Breakpoints</h2>
  <div class="container">
    <div class="row">
      <div class="box col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
        col
      </div>
      <div class="box col-12 col-sm-6 col-md-8 col-lg-3 col-xl-4">
        col
      </div>
      <div class="box col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
        col
      </div>
      <div class="box col-12 col-sm-6 col-md-8 col-lg-3 col-xl-12">
        col
      </div>
    </div>

    <hr>

    <h2 class="text-center">Breakpoints + offset</h2>
    <div class="row">
      <div class="box col-12 col-sm-4 col-md-6">
        col
      </div>
      <div class="box col-12 col-sm-4 col-md-6">
        col
      </div>
      <div class="box col-12 col-sm-4 col-md-6">
        col
      </div>
      <div class="box col-12 col-sm-4 col-md-6 offset-sm-4 offset-md-0">
        <!-- breakpoint는 어떠한 크기 이상에 대한 설정이므로 md에서 다시 0으로 바꿔주는 설정이 필요 -->
        col
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
    crossorigin="anonymous"></script>
</body>

</html>
```

* Media Query로 작성된 grid system의 breakpoints

![Media Query](<이미지/240311/media query로 작성된 breakpoints.PNG>)

### bootstrap에서 gridcard 문법을 지원해줌
* row-cols 클래스를 사용하여 행당 표시할 열(카드) 수를 손쉽게 제어할 수 있음
* row-cols-1 row-cols-md-2 g-4 (xs size에서는 row안에 1개의 카드를 보여줌, md size에서는 2개의 카드를 동시에 보여줌)
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>
  <h2 class="text-center">Grid Cards</h2>
  <div class="container">
    <div class="row row-cols-1 row-cols-sm-3 row-cols-md 2">
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content.</p>
          </div>
        </div>
      </div>
      <div class="col offset-sm-4 offset-md-0">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
    crossorigin="anonymous"></script>
</body>

</html>

```

# CSS Layout 종합정리
![CSS lay out 종합정리1](<이미지/240311/css layout 정리1.PNG>)

![CSS lay out 종합정리2](<이미지/240311/css layout 정리2.PNG>)

![CSS lay out 종합정리3](<이미지/240311/css layout 정리3.PNG>)

![CSS lay out 종합정리4](<이미지/240311/css layout 정리4.PNG>)


web개발 연습은 이미 만들어진 웹페이지를 잡아서 clone 코딩연습을 해보기!

ex) google 뉴스 페이지를 보고 따라 만들어보기, instagram 페이지 만들어보기

google에 web.dev를 입력해서 웹개발 관련 문서를 볼 수 있음