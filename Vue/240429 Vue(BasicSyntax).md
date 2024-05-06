# Template Syntax
* DOM을 기본 구성 요소 인스턴스의 데이터에 선언적으로 바인딩(Vue Instance와 DOM을 연결)할 수 있는 HTML 기반 템플릿 구문(확장된 문법 제공)을 사용

## Template syntax 종류
1. Text Interpoltation
```html
<p>Message : {{msg}}</p>
```
* 데이터 바인딩의 가장 기본적인 형태
* 이중 중괄호 구문 (콧수염 구문)을 사용
* 콧수염 구문은 해당 구성요소 인스턴스의 msg 속성값으로 대체(msg는 일반 변수가 아닌 반응형 변수)
* msg 속성이 변경될 때마다 업데이트 됨

2. Raw HTML
* html 자체를 출력하는 방법
```html
<div v-html='rawHtml'></div>
const rawHtml = ref('<span style='color:red'>This should be red.</span>) 
```
![Raw HTML 예시](<../이미지/240429/raw html.PNG>)
* 콧수염 구문은 데이터를 일반 텍스트로 해석하기 때문에 실제 HTML을 출력하려면 v-html을 사용해야함

3. Attribute Bindings
* 속성을 연결하는 방법
* 반응형 변수가 바뀌면 id도 바뀜
```html
<div v-bind:id="dynamicId"></div>
const dynamicId= ref('my-id')
```
![attribute bindings 예시](<../이미지/240429/attribute bindings.PNG>)
* 콧수염 구문은 HTML 속성 내에서 사용할 수 없기 때문에 v-bind를 사용
* HTML의 id 속성 값을 vue의 dynamicId 속성과 동기화 되도록 함
* 바인딩 값이 null이나 undefind인 경우 렌더링 요소에서 제거됨


4. JavaScript Expressions
```html
{{ number +1 }}
{{ ok ? 'YES' : 'NO' }}

{{ message.split('').reverse().join('') }}
<div :id='`list-${id}`'></div>
```
* Vue는 모든 데이터 바인딩 내에서 JavaScript 표현식의 모든 기능을 지원
* Vue 템플릿에서 JavaScript 표현식을 사용할 수 있는 위치
  1. 콧수염 구문 내부
  2. 모든 directive의 속성 값 ('v-'로 시작하는 특수 속성)

### 표현식 작성시 Expressions 주의사항
* 각 바인딩에는 하나의 단일 표현식만 포함될 수 있음
  * 표현식은 값으로 평가할 수 있는 코드 조각(return 뒤에 사용할 수 있는 코드여야 함)
* 작동하지 않는 경우
  * 선언식, if 문

  ![expressions 주의사항](<../이미지/240429/expressions 주의사항.PNG>)

# Directive
* 'v-' 접두사가 있는 특수 속성
* v-bind, v-on, v-if ...

## Directive 특징
* Directive의 속성 값은 단일 JavaScript 표현식이어야함(v-for, v-on 제외)
* 표현식 값이 변경될 때 DOM에 반응적으로 업데이트를 적용
* 아래 코드에서 v-if 뒤에 seen부분이 단순한 문자열이 아니라 바로 javascript의 표현식
```html
<p v-if='seen'>Hi There</p>
```
* Directive 전체 구문
  * Directive이후에는 콜론으로 시작
  * value에는 Javascript 표현식 == 아래 예시에서는 onSubmit이라는 함수를 호출

  ![Directive 전체구문](<../이미지/240429/directive 전체 구문.PNG>)

### Directive-'Arguments'
* 일부 directive는 directive 뒤에 콜론(':')으로 표시되는 인자를 사용할 수 있음(ex. v-on)
* 아래 예시의 href는 HTML\<a>요소의 href 속성 값을 myUrl 값에 바인딩 하도록 하는 v-bind의 인자
```html
<a v-bind:href="myUrl">Link</a>
```
* 아래 예시의 click은 이벤트 수신할 이벤트 이름을 작성하는 v-on의 인자
```html
<button v-on:click="doSomething">Button</button>
```
### Directive-'Modifiers'
* '.(dot)'로 표시되는 특수 접미사로, directive가 특별한 방식으로 바인딩되어야 함을 나타냄
* 아래 예시의 .prevent는 발생한 이벤트에서 event.preventDefault()를 호출하도록 v-on에 지시하는 modifier(수식어)
```html
<form @submit.prevent="onSubmit">...</form>
```
### Built-in Directives
* v-text
* v-show
* v-if
* v-for
* https://vuejs.org/api/built-in-directives.html

# Dynamically data binding
## v-bind
* 하나 이상의 속성 또는 컴포넌트(Vue 인스턴스) 데이터를 표현식에 동적으로 바인딩(연결)
* 단방향 바인딩 <-> v-model은 양방향 바인딩

## v-bind 사용처
1. Attribute Binding = src, href와 같은 속성을 넣는 경우
2. Class and Style Bindings = class나 inline-style을 넣는 경우

### Attribute Bindings
  * HTML의 속성 값을 Vue의 상태 속성 값과 동기화 되도록 함
  * script에서 선언된 변수를 속성값으로 동적으로 연결지어줌 
```html
<!-- v-bind.html -->
<img v-bind:src='imageSrc'>
<a v-bind:href='myUrl'>Move to url</a>
```
  * v-bind shorthand(약어)
    - ':'(colon)만 쓰고 v-bind를 생략
    - v-bind와 v-on만 생략 구문이 있음
```html
<img :src='imageSrc'>
<a :href='myUrl'>Move to url</a>
```

  * Dynamic attribute name(동적 인자 이름)
    * 속성의 값이 아니라 이름을 동적인자로 연결
    - 대괄호([])로 감싸서 directive argument에 JavaScript 표현식을 사용할 수도 있음
    - JavaScript 표현식에 따라 동적으로 평가된 값이 최종 argument 값으로 사용됨
    * 대괄호 안에 작성하는 이름은 반드시 소문자로만 구성 가능(브라우저가 속성 이름을 소문자로 강제 변환하기 때문)

  ![attribute bindings 동적인자 예시](<../이미지/240429/attribute bindings 동적인자.png>)


* Attribute Binding 예시
```html
<body>
  <div id="app">
    <img v-bind:src="imageSrc" alt="#">
    <a v-bind:href="myUrl">이동!</a>
  <!-- v bind의 생략 구문(약어) -->
    <img :src="imageSrc" alt="#">
    <a :href="myUrl">이동!</a>
    <p :[dynamicattr]="dynamicValue">.......</p> 
    <!-- <p title='Hello Vue.js'>로 생김 -->
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const imageSrc = ref('https://picsum.photos/200')
        const myUrl = ref('https://www.google.co.kr/')
        const dynamicattr = ref('title')
        const dynamicValue = ref('Hello Vue.js')
        return {
          imageSrc,
          myUrl,
          dynamicattr,
          dynamicValue
        }
      }
    })

    app.mount('#app')
  </script>
</body>
```
![attribute bindings 예시](<../이미지/240429/attribute bindings 예시.PNG>)

### Class and Style Bindings
* class와 style은 모두 HTML 속성이므로 다른 속성과 마찬가지로 v-bind를 사용하여 동적으로 문자열 값을 할당할 수 있음

* Vue는 class 및 style속성 값을 v-bind로 사용할 때 객체 또는 배열을 활용(여러개의 style을 동시에 적용하기 위해 사용)하여 작성할 수 있도록 함
  - 단순히 문자열 연결을 사용하여 이러한 값을 생성하는 것은 번거롭고 오류가 발생하기가 쉽기 때문

#### Class and Style Bindings가 가능한 경우
각각의 방법에서 객체로 진행하거나 배열로 진행하는 경우로 나누어짐
1. Binding HTML Classes
  1.1 Binding to Objects
  1.2 Binding to Arrays
2. Binding Inline Styles
  2.1 Binding to Objects
  2.2 Binding to Arrays

#### 1.1 Binding HTML Classes - Binding to Objects
* 객체를 :class에 전달하여 클래스를 동적으로 전환할 수 있음
  * 예시1
    - isActive의 Boolean 값에 의해 active 클래스의 존재가 결정됨
    * style에 있는 active class를 넣는지 여부를 isactive로 결정 

  ![binding objects](<../이미지/240429/binding to objects.PNG>)


* 객체에 더 많은 필드를 포함하여 여러 클래스를 전환할 수 있음
  * 예시2
    - :class directive를 일반 클래스 속성과 함께 사용 가능
    * 클래스명에 -가 들어있으면 문자열로 키를 만들어주어야함, javascript에서는 키값의 ""을 생략할 수 있지만 -가 있는 경우는 생략할 수 없음

  ![binding objects2](<../이미지/240429/binding to objects2.PNG>)


* 반드시 inline 방식으로 작성하지 않아도 됨
* 반응형 변수를 활용해 객체를 한번에 작성하는 방법

  ![binding objects3](<../이미지/240429/binding to objects3.PNG>)


#### 1.2 Binding HTML Classes - Binding to Arrays
* :class를 배열에 바인딩하여 클래스 목록을 적용할 수 있음
  * 예시1
  
  ![binding to arrays1](<../이미지/240429/binding to Arrays.PNG>)


* 배열 구문 내에서 객체 구문을 사용하는 경우
  * 예시 2

  ```html
  <div :class="[{ active : isActive }, infoClass]">Text</div>
  ```
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .active {
      color: crimson;
    }

    .text-primary {
      color: blue;
    }
  </style>
</head>

<body>
  <div id="app">

    <!-- Binding to Objects -->
    <div :class="{ active: isActive }">Text</div>
    <div class="static" :class="{ active: isActive, 'text-primary': hasInfo }">Text</div>
    <div class="static" :class="classObj">Text</div>

    <!-- Binding to Arrays -->
    <div :class="[activeClass, infoClass]">Text</div>
    <div :class="[{ active: isActive }, infoClass]">Text</div>

  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const isActive = ref(false)
        const hasInfo = ref(true)
        const classObj = ref({
          active: isActive,
          'text-primary': hasInfo
        })
        const activeClass = ref('active')
        const infoClass = ref('text-primary')
        return {
          isActive,
          hasInfo,
          classObj,
          activeClass,
          infoClass
        }
      }
    })

    app.mount('#app')
  </script>
</body>

</html>

```
#### 2.1 Binding Inline Styles - Binding to Objects
* :style은 JavaScript 객체 값에 대한 바인딩을 지원(HTML style 속성에 해당)

* 예시1

![binding to objects](<../이미지/240429/binding inline styles.PNG>)

  * 실제 CSS에서 사용하는 것처럼 :style은 kebab-cased 키 문자열도 지원(단, camelCase 작성을 권장)

* 예시2

![binding to objects2](<../이미지/240429/binding inline styles2.PNG>)

* 반드시 inline 방식으로 작성하지 않아도 됨
* 반응형 변수를 활용해 객체를 한번에 작성하는 방법
* 예시3

  ![binding to objects3](<../이미지/240429/binding inline styles3.png>)

```html

```

#### 2.2 Binding Inline Styles - Binding to Arrays
* 여러 스타일 객체를 배열에 작성해서 :style을 바인딩할 수 있음
* 작성한 객체는 병합 되어 동일한 요소에 적용
  * 예시 1
  * 스타일이 겹치면 가장 마지막에 적용된 스타일이 적용됨

  ![binding inline styles-binding to array1](<../이미지/240429/binding inline styles-binding to array1.png>)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <div id="app">
    <!-- Binding to Objects -->
    <div style="color: crimson; font-size: 50px;">Text</div>
    <div :style="{ color: activeColor, fontSize: fontSize + 'px'}">Text</div>
    <div :style="{ color: activeColor, 'font-size': fontSize + 'px'}">Text</div>
    <div :style="styleObj">Text</div>

    <!-- Binding to Arrays -->
    <div :style="[styleObj, styleObj2]">Text</div>
    <!-- <div style="color: blue; font-size: 50px; border: 1px solid black;">Text</div> -->
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const activeColor = ref('crimson')
        const fontSize = ref(50)
        const styleObj = ref({
          color: activeColor,
          fontSize: fontSize.value + 'px'
        })
        const styleObj2 = ref({
          color: 'blue',
          border: '1px solid black'
        })

        return {
          activeColor,
          fontSize,
          styleObj,
          styleObj2
        }
      }
    })

    app.mount('#app')
  </script>
</body>

</html>

```

### v-bind 종합
* 동적인 속성을 부여(일반속성(href,src..), class, style)
* http://vuejs.org/api/built-in-directives.html#v-bind

# Event Handling
## v-on
* DOM 요소에 이벤트 리스너를 연결 및 수신
* javascript에서 addeventlistener를 사용하는대신 v-on을 사용
### v-on 구성
```html
v-on:event="handler"
event ==JS에서 존재하는 이벤트 이름
handler==한줄짜리 코드
```
* handler 종류
  1. Inline handlers : 이벤트가 트리거 될때 실행 될 JavaScript 코드
  2. Method handlers : 컴포넌트에 정의된 메서드 이름

* v-on shorthand(약어)
  - '@'
  - v-bind와 다르게 ':'도 작성을 안함
```html
@event="handler"
```
### 1. Inline handlers
* Inline handlers는 주로 간단한 상황에 사용

  ![Inline handlers](<../이미지/240429/inline handler.PNG>)

### 2. Method Handlers
* Inline handlers로는 불가능한 대부분의 상황에서 사용
* method를 작성해서 호출하는 경우

  ![Method handlers](<../이미지/240429/Method handler.PNG>)

  ![Method handlers 결과](<../이미지/240429/Method handler 결과.PNG>)

* Method Handlers는 이를 트리거하는 기본 DOM Event 객체를 자동으로 수신

  ![method handlers 2](<../이미지/240429/method handler 2.PNG>)

### Inline Handlers에서의 메서드 호출
* 메서드 이름에 직접 바인딩하는 대신 Inline Handlers에서 메서드를 호출할 수도 있음
* 이렇게 하면 기본 이벤트 대신 사용자 지정 인자를 전달할 수 있음

  ![Inline Handlers에서의 메서드 호출](<../이미지/240429/Inline Handlers에서의 메서드 호출.PNG>)

### Inline Handlers에서의 event 인자에 접근하기
* Inline Handlers에서 원래 DOM 이벤트에 접근하기
* 사용자 지정인자를 정의한 순간 event인자는 자동으로 사라지기 때문에 사용하고 싶으면 직접 선언이 필요
* $event 변수를 사용하여 메서드에 전달, 인자 전달 순서는 상관없음(위치인자로 사용되기 때문)

  ![Inline Handlers에서의 event 인자에 접근하기](<../이미지/240429/Inline handler에서의 event 인자에 접근하기.PNG>)

### Event Modifiers
* Vue는 v-on에 대한 Event Modifiers를 제공해 event.preventDefault()와 같은 구문을 메서드에서 작성하지 않도록 함
* stop, prevent, self 등 다양한 modifiers를 제공
  * stop은 이벤트의 전파를 막음 == bubbling을 막음
  * prevent는 이벤트의 기본동작을 막음(ex. 새로고침을 막음)
* 메서드는 DOM 이벤트에 대한 처리보다는 데이터에 관한 논리를 작성하는 것에 집중할 것
* 수식어는 연결이 가능하며, 여러개의 수식어를 작성한다면 수식어 작성 순서대로 진행됨
```html
    <form @submit.prevent="onSubmit">...</form>
    <a @click.stop.prevent="onLink">...</a>
    <!-- stop은 이벤트의 전파를 막음 == 버블링을 막음 prevent는 기본 동작을 막음 -->
```
* Modifiers는 chained 되게끔 작성할 수 있으며 이때는 작성된 순서로 실행되기 때문에 작성 순서에 유의

### Key Modifiers
* Vue는 키보드 이벤트를 수신할 때 특정 키에 관한 별도 modifiers를 사용할 수 있음

* 예시
  * key가 Enter일 때만 onSubmit 이벤트를 호출하기
  ```
  <input @keyup.enter ='onSubmit'>
  ```

### 전체코드
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <div id="app">
    <!-- Inline Handlers -->
    <button v-on:click="count++">Add 1</button>
    <button @click="count++">Add 1</button>
    <p>Count: {{ count }}</p>

    <!-- Method Handlers -->
    <button @click="myFunc">Hello</button>

    <!-- Calling Methods in Inline Handlers -->
    <button @click="greeting('hello')">Say hello</button>
    <button>Say bye</button>

    <!-- Accessing Event Argument in Inline Handlers -->
    <button @click="warning('경고입니다.', $event)">Submit</button>
    <button @click="warning($event, '경고입니다.')">Submit</button>

    <!-- event modifiers -->
    <form @submit.prevent="onSubmit">...</form>
    <a @click.stop.prevent="onLink">...</a>

    <!-- key modifiers -->
    <input @keyup.enter="onSubmit">
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const count = ref(0)
        const name = ref('Alice')
        const myFunc = function (event) {
          console.log(event)
          console.log(event.currentTarget)
          console.log(`Hello, ${name.value}`)
        }
        const greeting = function (message) {
          console.log(message)
        }
        const warning = function (message, event) {
          console.log(message)
          console.log(event)
        }

        return {
          count,
          name,
          myFunc,
          greeting,
          warning
        }
      }
    })

    app.mount('#app')
  </script>
</body>

</html>

```

### v-on 종합
* https://vuejs.org/api/built-in-directives.html#v-on


# Form Input Bindings
* form을 처리할 때 사용자가 input에 입력하는 값을 실시간으로 JavaScipt 상태에 동기화해아 하는 경우(양방향 바인딩)
* 사용자 입력값을 바로 반응형 변수로 동기화
* 양방향 바인딩 방법
  1. v-bind와 v-on을 함께 사용
  2. v-model 사용

## v-bind와 v-on을 함께 사용
  1. v-bind를 사용하여 input 요소의 value 속성 값을 입력 값으로 사용
  2. v-on을 사용하여 input 이벤트가 발생할 때마다 input요소의 value값을 별도 반응형 변수에 저장하는 핸들러를 호출
    * v-on은 이벤트를 인자로 받아올 수 있음==eventlistener

  ![v-bind & v-on](<../이미지/240429/v-bind v-on.PNG>)
  ![v-bind & v-on 코드](<../이미지/240429/v-bind v-on 함께 사용.PNG>)
### 전체 코드
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <div id="app">
    <p>{{ inputText1 }}</p>
    <input :value="inputText1" @input="onInput">

    <p>{{ inputText2 }}</p>
    <input v-model="inputText2">
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const inputText1 = ref('')
        const inputText2 = ref('')
        // input의 value 값을 계속해서 반응형 변수 inputText1에 할당을 하는 함수
        const onInput= function(event){
          inputText1.value = event.currentTarget.value
        }
        return {
          inputText1,
          inputText2,
          onInput,
        }
      }
    })

    app.mount('#app')
  </script>
</body>

</html>

```


## v-model 사용
* v-model : form input 요소 또는 컴포넌트에서 양방향 바인딩을 만듦
* v-model을 사용하여 사용자 입력 데이텅와 반응형 변수를 실시간 동기화

  ![v-model 사용](<../이미지/240429/v-model 사용.png>)

* IME가 필요한 언어(한국어,중국어,일본어 등)의 경우 v-model이 제대로 업데이트되지 않음
* 해당 언어에 대해 올바르게 응답하려면 v-bind와 v-on 방법을 사용해야 함

  ![v-model 예시](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240429/v-model.PNG)

## v-model 활용
* v-model과 다양한 입력 양식
  * v-model은 단순 Text input 뿐만 아니라 Checkbox, Radio, Select 등 다양한 타입의 사용자 입력 방식과 함께 사용 가능

### Checkbox 활용
1. 단일 체크박스와 boolean 값 활용
  
  ![checkbox 활용1](<../이미지/240429/checkbox 활용1.PNG>)
```html
  <!-- single checkbox -->
    <input type="checkbox" id="checkbox" v-model="checked">
    <label for="checkbox">{{ checked }}</label>

```

2. 여러 체크박스와 배열 활용
  * 해당 배열에는 현재 선택된 체크박스의 값이 포함됨

  ![checkbox 활용2](<../이미지/240429/checkbox 활용2.PNG>)
```html
<!-- multiple checkbox -->
    <div>Checked names: {{ checkedNames }}</div>

    <input type="checkbox" id="alice" value="Alice" v-model="checkedNames">
    <label for="alice">Alice</label>

    <input type="checkbox" id="bella" value="Bella" v-model="checkedNames">
    <label for="bella">Bella</label>
```

#### Select 활용
* select에서 v-model 표현식의 초기 값이 어떤 option과도 일치하지 않는 경우 select요소는 '선택되지 않은(unselected)' 상태로 렌더링 됨

![select 활용](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240429/select%ED%99%9C%EC%9A%A9.PNG)

```html
 <!-- single select -->
    <div>Selected: {{ selected }}</div>

    <select v-model="selected">
      <option disabled value="">Please select one</option>
      <option>Alice</option>
      <option>Bella</option>
      <option>Cathy</option>
    </select>
  </div>

```
### 전체 코드
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <div id="app">
    <!-- single checkbox -->
    <input type="checkbox" id="checkbox" v-model="checked">
    <label for="checkbox">{{ checked }}</label>

    <!-- multiple checkbox -->
    <div>Checked names: {{ checkedNames }}</div>

    <input type="checkbox" id="alice" value="Alice" v-model="checkedNames">
    <label for="alice">Alice</label>

    <input type="checkbox" id="bella" value="Bella" v-model="checkedNames">
    <label for="bella">Bella</label>

    <!-- single select -->
    <div>Selected: {{ selected }}</div>

    <select v-model="selected">
      <option disabled value="">Please select one</option>
      <option>Alice</option>
      <option>Bella</option>
      <option>Cathy</option>
    </select>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref } = Vue

    const app = createApp({
      setup() {
        const checked = ref(false)
        const checkedNames = ref([])
        const selected = ref('')

        return {
          checked,
          checkedNames,
          selected
        }
      }
    })

    app.mount('#app')
  </script>
</body>

</html>

```


### v-model 종합
* https://vuejs.org/api/built-in-directives.html#v-model

# 참고

## `$` 접두어가 붙은 변수

- Vue 인스턴스 내에서 제공되는 내부 변수
- 사용자가 지정한 반응형 변수나 메서드와 구분하기 위함
- 주로 Vue 인스턴스 내부 상태를 다룰 때 사용
- 대표적으로 $event가 있음

## IME(Input Method Editor)

- 사용자가 입력 장치에서 기본적으로 사용할 수 없는 문자(비영어권 언어)를 입력할 수 있도록 하는 운영 체제 구성 프로그램
- 일반적으로 키보드 키보다 자모가 더 많은 언어에서 사용해야 함
  > IME가 동작하는 방식과 Vue의 양방향 바인딩(v-model) 동작 방식이 상충하기 때문에 한국어 입력시 예상대로 동작하지 않았던 것