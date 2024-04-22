# Event
## 웹에서의 이벤트
* 화면을 스크롤하는 것
* 버튼을 클릭했을 때 팝업 창이 출력되는 것
* 마우스 커서의 위치에 따라 드래그 앤 드롭하는 것
* 사용자의 키보드 입력 값에 따라 새로운 요소를 생성하는 것
> 웹에서의 모든 동작은 이벤트 발생과 함께 한다.

## event 객체
* 무언가 일어났다는 신호, 사건
> 모든 DOM 요소는 이러한 event를 만들어 냄

### 'event' object
* DOM에서 이벤트가 발생했을 때 생성되는 객체
* 이벤트 종류
  - mouse, input, keyboard, touch ...
  - https://developer.mozilla.org/en-US/docs/Web/API/Event

* DOM 요소는 event를 받고 받은 event를 '처리'할 수 있음(event handler를 이용해 처리)

### event handler
* 이벤트가 발생했을 때 실행되는 함수
* 사용자의 행동에 어떻게 반응할 지를 JavaScript 코드로 표현한 것

#### .addEventListener()
* 대표적인 이벤트 핸들러 중 하나
* 특정 이벤트를 DOM 요소가 수신할 때마다 콜백 함수를 호출
![.addEventListener](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240422/addEventListener.PNG)

* 대상에 특정 Event가 발생하면, 지정한 이벤트를 받아 할 일을 등록한다.

* addEventListener의 인자
  * type
    * 수신할 이벤트 이름
    * 문자열로 작성(ex. 'click')
  * handler
    * 발생한 이벤트 객체를 수신하는 콜백 함수
    * 콜백 함수는 발생한 event object를 유일한 매개변수로 받음
  
##### addEventListener 활용
* 버튼을 클릭하면 버튼 요소 출력하기
* 버튼에 이벤트 처리기를 부착하여 클릭 이벤트가 발생하면 이벤트가 발생한 버튼 정보를 출력
![addEventListener 활용](<../이미지/240422/addEventListener 활용.PNG>)
* 요소에 addEventListener를 부착하게 되면 내부의 this값은 대상 요소를 가리키게 됨(event 객체의 currentTarget 속성 값과 동일)
```html
<body>
  <button id="btn">버튼</button>

  <script>
    // 1. 버튼 선택
    const btn = document.querySelector('#btn')


    // 2. 콜백 함수
    const detectClick = function (event){
      console.log(event)
      console.log(this)
      console.log(event.currentTarget)
    }

    // 3. 버튼에 이벤트 핸들러를 부착
    // btn.addEventListener('click',function(event) {
    //   console.log(event)
    //   console.log(this)
    //   console.log(event.currentTarget)
    // })
    btn.addEventListener('click',detectClick)

  </script>
</body>
```
* addEventListener의 콜백 함수 특징
  * 발생한 이벤트를 나타내는 event 객체를 유일한 매개변수로 받음
  * 반환 값 없음
![addEventListener 콜백함수 특징](<../이미지/240422/addEventListener 콜백함수 특징.PNG>)

## 버블링
* form > div > p 형태의 중첩된 구조에 각각 이벤트 핸들러가 있을 때 p 요소를 클릭하면??
![버블링 개요](<../이미지/240422/버블링 개요.PNG>)
* <p> 요소만 클릭했는데도 불구하고 모든 핸들러가 동작
![버블링 개요2](<../이미지/240422/버블링 개요2.PNG>)

### 버블링이란?
* 한 요소에 이벤트가 발생하면, 이 요소에 할당된 핸들러가 동작하고, 이어서 부모 요소의 핸들러가 동작하는 현상
* 가장 최상단의 조상 요소(document)를 만날 때까지 이 과정이 반복되면서 요소 각각에 할당된 핸들러가 동작
* 이벤트가 제일 깊은 곳에 있는 요소에서 시작해 부모 요소를 거슬러 올라가며 발생하는 것이 마치 물속 거품과 닮았기 때문
* 가장 안쪽의 <p> 요소를 클릭하면 p->div->form 순서로 3개의 이벤트 핸들러가 모두 동작했던 것

* 이벤트가 정확히 어디서 발생했는지 접근할 수 있는 방법
  * event.currentTarget
  * event.target

#### 'currentTarget' & 'target' 속성
* currentTarget 속성
  * '현재' 요소
  * 항상 이벤트 핸들러가 연결된 요소만을 참조하는 속성
  * 'this'와 같음
* 'target' 속성
  * 이벤트가 발생한 가장 안쪽의 요소(target)를 참조하는 속성
  * 실제 이벤트가 시작된 요소
  * 버블링이 진행되어도 변하지 않음

##### 'currentTarget' & 'target' 예시
* 세요소 중 가장 최상위 요소인 outerouter요소에만 핸들러가 부착
* 각 요소를 클릭했을 때 event의 target과 currentTarget의 차이 비교
!['currentTarget' & 'target' 예시](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240422/target&currentTarget.PNG)

* 'currentTarget' : 핸들러가 연결된 outerouter 요소만을 가리킴
* 'target' : 실제 이벤트가 발생하는 요소를 가리킴
* 핸들러는 outerrouter에만 할당되어 있지만 하위 요소 outer와 inner를 클릭해도 해당 핸들러가 동작함
* 클릭 이벤트가 어디서 발생했든 상관없이 outerouter까지 이벤트가 버블링 되어 핸들러를 실행시키기 때문

![target&currentTarget 예시2](<../이미지/240422/target&currentTarget 예시2.PNG>)
```html

<body>
  <div id="outerouter">
    outerouter
    <div id="outer">
      outer
      <div id="inner">inner</div>
    </div>
  </div>

  <script>
    const outerOuterElement = document.querySelector('#outerouter')
    const outerElement = document.querySelector('#outer')
    const innerElement = document.querySelector('#inner')

    const clickHandler = function (event) {
      console.log('currentTarget:', event.currentTarget.id)
      console.log('target:', event.target.id)
    }

    outerOuterElement.addEventListener('click', clickHandler)
  </script>
</body>

```

### 캡처링과 버블링
* 캡처링(capturing)
  * 이벤트가 하위 요소로 전파되는 단계(버블링과 반대)
* table안에 td를 클릭하면 이벤트는 최상위 요소부터 아래로 전파
* 실제 이벤트가 발생한 지점(event.target)에서 실행된 후 다시 위로 전파
  - 이 과정에서 상위 요소에 할당된 이벤트 핸들러가 호출되는 것
* 캡처링은 실제 다루는 경우가 거의 없으므로 버블링에 집중하기
![캡처링과 버블링](<../이미지/240422/캡처링과 버블링.PNG>)



### 버블링이 필요한 이유
* 각자 다른 동작을 수행하는 버튼이 여러개 있다고 가정할 경우 각 버튼마다 서로 이벤트 핸들러를 할당할 필요가 없음
* 각 버튼의 공통 조상인 div 요소에 이벤트 핸들러 단하나만 할당

![버블링이 필요한 이유](<../이미지/240422/버블링이 필요한 이유.PNG>)

* 요소의 공통 조상에 이벤트 핸들러를 단 하나만 할당하면 여러 요소를 한꺼번에 다룰 수 있음
* 공통 조상에 할당한 핸들러에서 event.target을 이용하면 실제 어떤 버튼에서 이벤트가 발생했는지 알 수 있기 때문

# event handler 활용 실습

1. 버튼을 클릭하면 숫자를 1씩 증가해서 출력하기
2. 사용자의 입력 값을 실시간으로 출력하기
3. 사용자의 입력값을 실시간으로 출력 - '+' 버튼을 클릭하면 출력한 값의 CSS 스타일을 변경하기
4. todo 프로그램 구현
5. 로또 번호 생성기 구현


## click 이벤트 실습
* 버튼을 클릭하면 숫자를 1씩 증가
![클릭 이벤트 실습](<../이미지/240422/클릭 이벤트 실습.PNG>)

```html
<body>
  <button id="btn">버튼</button>
  <p>클릭횟수 : <span id="counter">0</span></p>

  <script>
    // 1. 버튼 선택
    const btn = document.querySelector('#btn')
    
    // 3. 초기값 선언
    let count =0
    
    // 2. 이벤트 핸들러 부착
    btn.addEventListener('click',function(event){
      // 3.1 초기값 1증가
        count +=1
      // 2.1 count할 요소 선택
      const spanTag = document.querySelector('#counter')
      // 2.2 count할 요소 안의 숫자를 선택
      spanTag.textContent = count

    })
</script>
</body>
```

## input 이벤트 실습
* 사용자의 입력값을 실시간으로 출력하기
![input 실습](<../이미지/240422/input 실습.PNG>)
```html

<body>
  <input type="text" id="text-input">
  <p></p>

  <script>

    // 1. input 태그 선택
    const inputTag = document.querySelector('#text-input')
    // 3-3 p 태그 선택
    const pTag = document.querySelector('p')
    // 2. 콜백 함수(input 태그에 input 이벤트가 발생할 때마다 실행되는 코드)
    const inputHandler= function(event){
      // 3-1 사용자가 입력한 데이터가 어디에 있는지 찾기
      // console.log(event)
      // console.log(event.currentTarget.value)
      // console.log(this.value)
      // 3-2 사용자 입력데이터를 p 태그의 컨텐츠로 저장
      pTag.textContent = event.currentTarget.value
    }
    // 3. 선택한 input 태그에 이벤트 핸들러 부착
    inputTag.addEventListener('input',inputHandler)
  </script>
</body>
```

### currentTarget 주의사항
* console.log()로 event 객체를 출력할 경우 currentTarget 키의 값은 null을 가짐
* currentTarget은 이벤트가 처리되는 동안에만 사용할 수 있기 때문
* 대신 console.log(event.currentTarget)을 사용하여 콘솔에서 확인 가능
* currentTarget 이후의 속성 값들은 'target'을 참고해서 사용하기
![currentTarget 주의사항](<../이미지/240422/currentTarget 주의사항.PNG>)

## click & input 이벤트 실습
* 사용자의 입력값을 실시간으로 출력<br>
'+' 버튼을 클릭하면 출력한 값의 CSS 스타일을 변경
![click & input 이벤트 실습](<../이미지/240422/click & input 이벤트.PNG>)

```html
<body>
  <h1></h1>
  <button id="btn">클릭</button>
  <input type="text" id="text-input">

  <script>
    // 1. input, h1 및 버튼 태그 선택
    const inputTag = document.querySelector('#text-input')
    const h1Tag = document.querySelector('h1')
    const btn = document.querySelector('#btn')

    // 2. input 이벤트에 반응하는 콜백 함수
    const inputHandler = function (event){
      h1Tag.textContent = event.currentTarget.value
    }

    // 4. 버튼에 클릭 이벤트에 반응하는 콜백함수
    const clickHandler = function(event){
      // 4.1 선택해둔 h1 태그의 클래스 목록에 blue클래스를 추가
      // h1Tag.classList.add('blue')

      // toggle 방법
      h1Tag.classList.toggle('blue')
    }

    // 3. input 태그에 이벤트 핸들러 부착
    inputTag.addEventListener('input',inputHandler)

    // 5. 버튼 태그에 이벤트 핸들러 부착
    btn.addEventListener('click', clickHandler)
</script>
</body>
```

## todo 실습
* 사용자의 입력데이터를 리스트 형태로 저장
![todo 실습](<../이미지/240422/todo 실습.PNG>)


* todo 추가 기능 구현
  1. 빈문자열 입력 방지
  2. 입력이 없을 경우 경고 대화상자를 띄움

```html
<body>
  <input type="text" class="input-text">
  <button id="btn">+</button>
  <ul></ul>

  <script>
    //  1. 필요한 태그를 모두 선택
    const inputTag = document.querySelector('.input-text')
    const btn = document.querySelector('#btn')
    const ulTag = document.querySelector('ul')

    //  2. 콜백함수 addTodo 작성
    const addTodo = function(event){
      //  2.1 사용자 입력 데이터를 저장
      const inputData = inputTag.value
      // 3. 빈문자열은 추가되지 않고 경고창으로 처리
      if (inputData.trim()) {
        // 2.2 li 태그 생성
        const listTag = document.createElement('li')
        // 2.3 생성한 li 태그에 텍스트 컨텐츠에 사용자 입력 값을 할당
        listTag.textContent = inputData
  
        // 2.4 완성한 li 태그를 ul 태그의 자식 요소로 추가
        ulTag.appendChild(listTag)
        inputTag.value=''
        
      } else{
        window.alert('할 일을 입력하세요')
      }
    }

    //  3. btn에 클릭 이벤트 핸들러 부착
    btn.addEventListener('click',addTodo)
  </script>
</body>
```

## 로또 번호 생성기 실습
* JS는 script를 목적으로 생성된 언어여서 모듈이 다양하지 않아 random을 만드는데 어려움이 있음
* Lodash 라이브러리를 이용하여 만듦
![로또 번호 생성기](<../이미지/240422/로또 번호 추천기 실습.PNG>)

```html
<body>
  <h1>로또 추천 번호</h1>
  <button id="btn">행운 번호 받기</button>
  <div></div>

  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <script>
    // 1. 필요한 태그 모두 선택
    const btn = document.querySelector('#btn')
    const divTag = document.querySelector('div')

    // 2. getLottery 콜백 함수 작성
    const getLottery =function(event){
      // 2.1 1부터 45까지의 번호가 필요
      const numbers = _.range(1,46)

      // 2.2 1~45에서 6개를 추출
      const sixNumbers = _.sampleSize(numbers,6)
      // console.log(sixNumbers)

      // 4. li 태그들을 담을 ul 태그 형성
      const ulTag = document.createElement('ul')

      // 2.3 번호 1개씩 li 태그로 형성
      sixNumbers.forEach(number => {
        // 3.1 번호를 담을 li 태그 형성
        const liTag = document.createElement('li')
        // 3.2 li 태그의 컨텐츠에 로또 숫자를 할당
        liTag.textContent = number
        ulTag.appendChild(liTag)
      });
      // 3.4 완성한 ul 태그를 div 태그의 자식 요소로 추가
      divTag.appendChild(ulTag)
    }
    // 3. btn 태그에 클릭 이벤트 핸들러 부착
    btn.addEventListener('click',getLottery)

  </script>
</body>
```

### lodash
* 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리
* array,object 등 자료구조를 다룰 때 사용하는 유용하고 간편한 함수들을 제공
* https://lodash.com/

# 이벤트 기본 동작 취소
* HTML의 각 요소가 기본적으로 가지고 있는 이벤트가 때로는 방해가 되는 경우가 있어 이벤트의 기본 동작을 취소할 필요가 있음
* 예시
  - form 요소의 제출 이벤트를 취소하여 페이지 새로고침을 막을 수 있음
  - a 요소를 클릭 할 때 페이지 이동을 막고 추가 로직을 수행할 수 있음

## .preventDefault()
* 해당 이벤트에 대한 기본 동작을 실행하지 않도록 지정

### 이벤트 동작 취소 실습
* copy 이벤트 동작 취소
  * 콘텐츠를 복사하는 것을 방지
  ![이벤트 동작 취소 실습1](<../이미지/240422/이벤트 동작 취소 실습1.PNG>)
  ![이벤트 동작 취소 실습2](<../이미지/240422/이벤트 동작 취소 실습2.PNG>)
  ![이벤트 동작 취소 실습3](<../이미지/240422/이벤트 동작 취소 실습3.PNG>)

# 참고
* addEventListener에서의 화살표 함수 주의사항
  * 화살표 함수는 자신만의 this를 가지지 않기 때문에 자신을 포함하고 있는 함수의 this를 상속받음
  * this를 사용해야하는 경우 addEventListener에서는 일반 함수로 사용하기
  ![addEventListener에서 화살표 함수 주의 사항](<../이미지/240422/addEventListener에서 화살표 함수 주의 사항.PNG>)