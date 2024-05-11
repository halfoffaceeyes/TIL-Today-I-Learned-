# Computed Properties
## Computed
* "계산된 속성"을 정의하는 함수
* 리턴된 값을 메모리에 저장하여 재사용성을 높이는 방법
* 미리 계산된 속성을 사용하여 템플릿에서 표현식을 단순하게 하고 불필요한 반복 연산을 줄임

### computed 기본 예시
* 할 일이 남아 있는지 여부에 따라 다른 메시지를 출력하기
* 변화가 생겼을 때만 계산을 하도록 하는 함수
  * computed 미적용

    ![computed 미적용](<../이미지/240430/computed 기본예시 미적용.PNG>)

    * 템플릿이 복잡해지며 todos에 따라 계산을 수행하게 됨
    * 만약 이 계산을 템플릿에 여러번 사용하는 경우에는 반복이 발생

  * computed 적용
    * 반응형 데이터를 포함하는 복잡한 로직의 경우 computed를 활용하여 미리 값을 계산하여 계산된 값을 사용
  
    ![computed 적용](<../이미지/240430/computed 기본예시 적용.PNG>)

### computed 특징
* 반환되는 값은 computed ref객체이며 일반 refs와 유사하게 계산된 결과를 .value로 참조할 수 있음(템플릿에서는 .value 생략 가능)
* computed속성은 의존된 반응형 데이터를 자동으로 추적
* 의존하는 데이터가 변경될 때만 재평가
  * restOfTodos의 계산은 todos에 의존하고 있음
  * 따라서 todos가 변경될 때만 restOfTodos가 업데이트됨

  ![computed 특징](<../이미지/240430/computed 특징.PNG>)

## Computed vs Methods
* computed와 동일한 로직을 처리할 수 있는 method

  ![computed와 동일한 로직의 method](<../이미지/240430/computed와 동일한 method.PNG>)

### computed와 method 차이
* computed 속성은 의존된 반응형 데이터를 기반으로 캐시(cached)된다
* 의존하는 데이터가 변경된 경우에만 재평가됨
* 즉, 의존된 반응형 데이터가 변경되지 않는 한 이미 계산된 결과에 대한 여러 참조는 다시 평가할 필요없이 이전에 계산된 결과를 즉시 반환
* 반면, method 호출은 다시 렌더링이 발생할 때마다 항상 함수를 실행

### Cache(캐시)
* 데이터나 결과를 일시적으로 저장해두는 임시 저장소
* 이후에 같은 데이터나 결과를 다시 계산하지 않고 빠르게 접근할 수 있도록 함
* 개발자도구의 network 탭에서 볼수 있음
#### Cache 예시
* '웹페이지의 캐시 데이터'
  - 과거 방문한 적이 있는 페이지에 다시 접속할 경우
  - 페이지 일부 데이터를 브라우저 캐시에 저장 후 같은 페이지에 다시 요청시 모든 데이터를 다시 응답 받는 것이 아닌 일부 캐시된 데이터를 사용하여 더 빠르게 웹페이지를 렌더링
![cache 예시](<../이미지/240430/cache 예시.PNG>)

### Computed와 method의 적절한 사용처
* computed
  - 의존하는 데이터에 따라 결과가 바뀌는 계산된 속성을 만들 때 유용
  - 동일한 의존성을 가진 여러 곳에서 사용할 때 계산 결과를 캐싱하여 중복 계산 방지
  - 의존된 데이터가 변경되면 자동으로 업데이트
  - 계산된 결과가 cache에 저장되기 때문에 위와 같은 속성들이 있음

* method
  - 단순히 특정 동작을 수행하는 함수를 정의할 때 사용
  - 데이터에 의존하는 지 여부와 관계없이 항상 동일한 결과를 반환하는 함수
  - 호출해야만 실행됨

* 무조건 computed만 사용하는 것이 아니라 사용목적과 상황에 맞게 computed와 method를 적절히 조합하여 사용

# Conditional Rendering
## v-if
* 표현식 값의 true/false를 기반으로 요소를 조건부로 렌더링
### v-if 예시
* 'v-else' directive를 사용하여 v-if에 대한 else 블록을 나타낼 수 있음

![v-if 예시](<../이미지/240430/v-if 예시.PNG>)

* isSeen 값을 클릭하면 !isSeen으로 변경

![v-if 예시 코드](<../이미지/240430/v-if 예시 코드.PNG>)


* 'v-else-if' directive를 사용하여 v-if에 대한 else if 블록을 나타낼 수 있음

![v-else-if](<../이미지/240430/v-else-if 코드.PNG>)

### 여러 요소에 대한 v-if 적용
* HTML template요소에 v-if를 사용하여 하나 이상의 요소에 대해 적용할 수 있음(v-else, v-else-if 모두 적용 가능)
* 페이지가 로드될 때 렌더링 되지 않지만 JavaScript를 사용하여 나중에 문서에서 사용할 수 있도록 하는 HTML을 보유하기 위한 메커니즘
* 보이지 않는 wrapper 역할

![template](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240430/template.PNG)

## v-show
* 표현식 값의 true/false를 기반으로 요소의 가시성(visibility)을 전환

### v-show 예시
* v-show 요소는 항상 DOM에 렌더링 되어 있음
* CSS display 속성만 전환하기 때문

![v-show](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240430/v-show.PNG)

### v-if와 v-show의 적절한 사용처
* v-if(Cheap intial load, expensive toggle)
  * 초기 조건이 false인 경우 아무작업도 수행하지 않음
  * 토글 비용이 높음

* v-show(Expensive initial load, cheap toggle)
  * 초기 조건에 관계없이 항상 렌더링
  * 초기 렌더링 비용이 더 높음

* v-if는 HTML에 작성이 되지 않고 v-show는 HTML작성을 하지만 css 속성으로 보여지지 않게 만들어주는것
* 콘텐츠를 매우 자주 전환하는 경우에는 v-show를, 실행중에 조건이 변경되지 않는 경우에는 v-if를 권장

# List Rendering
## v-for
* 소스데이터를 기반으로 요소 또는 템플릿 블록을 여러번 렌더링
  * 소스데이터 == Array, Object, Number, String, Iterable

### v-for 구조
* v-for는 alias in experession 형식의 특수 구문을 사용
```html
<div v-for="item in items">
  {{item.text}}
</div>
```
* 인덱스(객체에서는 key)에 대한 별칭을 지정할 수 있음
```html
<div v-for="(item,index) in arr"></div>
<div v-for="value in object"></div>
<div v-for="(value,key) in object"></div>
<div v-for="(value,key,index) in object"></div>
```

### v-for 예시
* 배열 반복

![v-for 예시](<../이미지/240430/v-for 예시.PNG>)

* 객체 반복

![v-for 예시2](<../이미지/240430/v-for 예시2.PNG>)

### 여러 요소에 대한 v-for 적용
  * HTML template요소에 v-for를 사용하여 하나 이상의 요소에 대해 반복 렌더링 할 수 있음

  ![template v-for](<../이미지/240430/template v-for.PNG>)
### 중첩된 v-for
* 각 v-for 범위는 상위 범위에 접근 할 수 있음

![중첩된 for](<../이미지/240430/중첩된 for.PNG>)


## v-for with key
* 반드시 v-for와 key를 함께 사용한다
  * 내부 컴포넌트의 상태를 일관되게 하여 데이터의 예측 가능한 행동을 유지하기 위함
### v-for와 key
* key는 반드시 각 요소에 대한 고유한 값을 나타낼 수 있는 식별자여야 함

  ![v-for와 key](<../이미지/240430/v-for와 key.PNG>)

### 내장 특수 속성 key
* number 혹은 string으로만 사용해야 함
* Vue의 내부 가상 DOM 알고리즘이 이전 목록과 새 노드 목록을 비교할 때 각 node를 식별하는 용도로 사용
* Vue 내부 동작 관련된 부분이기에 최대한 작성하려고 노력할 것
* https://vuejs.org/api/built-in-special-attributes.html#key

## v-for with v-if
* 동일 요소에 v-for와 v-if를 함께 사용하지 않는다.
  * 동일한 요소에서 v-if가 v-for 보다 우선순위가 더 높기 때문
  * v-if에서의 조건은 v-for 범위의 변수에 접근할 수 없음

### v-for와 v-if 문제 상황
* todo 데이터 중 이미 처리한(isComplete === true) todo만 출력하기

  ![문제상황 예시](<../이미지/240430/v-for v-if 동시사용 문제상황.PNG>)

* v-if가 더 높은 우선순위를 가지므로 v-for 범위의 todo 데이터를 v-if에서 사용할 수 없음

  ![동시사용시 오류 발생](<../이미지/240430/v-for v-if 동시사용 오류.PNG>)

### 해결법 1. computed 활용
* computed를 활용해 필터링 된 목록을 반환하여 반복하도록 설정

  ![v-for v-if 해결 computed](<../이미지/240430/v-for v-if 해결 computed.PNG>)

### 해결법 2. v-for와 \<template> 요소 활용
* v-for와 template 요소를 사용하여 v-if 위치를 이동

  ![v-for와 <template> 요소 활용](<../이미지/240430/v-for v-if 해결 template.PNG>)
## v-for 주의사항
* v-for와 key를 같이 사용
* v-for와 v-if는 동시에 사용하면 안됨

# Watchers
## watch
* 하나 이상의 반응형 데이터를 감시하고, 감시하느 데이터가 변경되면 콜백 함수를 호출
* computed와 유사하지만 다름
### wahch 구조

![watch 구조](<../이미지/240430/watch 구조.PNG>)
* 첫번째 인자(source)
  - watch가 감시하는 대상(반응형 변수, 값을 반환하는 함수 등)
* 두번째 인자(callback function)
  - source가 변경될 때 호출되는 콜백 함수
  * 콜백 함수에 인자가 두개가 들어감
  1. newValue
    * 감시하는 대상이 변화된 값
  2. oldValue(optional)
    * 감시하는 대상의 기존 값
* watch는 변경되기 전, 후의 값들을 모두 관리할 수 있음
* watch는 변화되면 바로 호출이 되기 때문에 const를 통해 선언할 필요가 없음

![watch 기본동작](<../이미지/240430/watch 기본동작.PNG>)
* watch는 선언만 해놓으면 실행해서 변화가 생겼을 때 동작을 함 == 변화가 없으면 실행이 없음

### watch 예시
* 감시하는 변수에 변화가 생겼을 때 연관 데이터 업데이트 하기

![watch 예시](<../이미지/240430/watch 예시.PNG>)
![watch 예시결과](<../이미지/240430/watch 예시 결과.PNG>)

### 여러 source를 감시하는 watch
* 배열을 활용

![watch 여러 source](<../이미지/240430/watch 여러 source 감시.PNG>)

## Computed vs watch
![computed vs watch](<../이미지/240430/computed vs watch.PNG>)
> computed와 watch 모두 의존(감시)하는 원본 데이터를 직접 변경하지 않음 == computed는 읽기전용 속성이라고도 함

* computed는 의존하는 데이터가 중요==값을 반환하기 위해 사용
* watch는 axios랑 같이 사용함

# Lifecycle Hooks
* Vue 인스턴스의 생애주기 동안 특정 시점에 실행되는 함수

## Lifecycle Hooks Diagram
* 인스턴스의 생애주기 중간 중간에 함수를 제공하여 개발자가 특정 단계에서 원하는 로직을 작성할 수 있도록 함


  ![life cycle hook](../%EC%9D%B4%EB%AF%B8%EC%A7%80/240430/lifecycle.png)
* https://vuejs.org/guide/essentials/lifecycle.html#lifecycle-diagram

## Lifecycle Hooks 예시
1. Vue 컴포넌트 인스턴스가 초기 렌더링 및 DOM 요소 생성이 완료된 후 특정 로직을 수행하기(onMounted)
  * onMounted는 app이 실행되면서 자동으로 같이 실행되는 함수

  ![lifecycle hook 예시](<../이미지/240430/lifecycle hook 예시.PNG>)

* 다른 예시
  - onMounted가 없으면 처음 페이지 렌더링시 아무 사진도 없지만 onMounted로 버튼을 누르지 않아도 사진이 나오도록 수정가능
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
    <button @click="getCatImage">냥냥펀치</button>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    const { createApp, ref,onMounted } = Vue
    const URL = 'https://api.thecatapi.com/v1/images/search'

    const app = createApp({
      setup() {
        const getCatImage = function () {
          axios({
            method: 'get',
            url: URL,
          })
            .then((response) => {
              imgUrl = response.data[0].url
              return imgUrl
            })
            .then((imgData) => {
              imgElem = document.createElement('img')
              imgElem.setAttribute('src', imgData)
              document.body.appendChild(imgElem)
            })
            .catch((error) => {
              console.log('실패했다옹')
            })
        }
        onMounted(() =>{
          getCatImage()
        })

        return { getCatImage }
      }
    })

    app.mount('#app')
  </script>
</body>

</html>
```


2. 반응형 데이터의 변경으로 인해 컴포넌트의 DOM이 업데이트 된 후 특정 로직을 수행하기(onUpdated)
  * onUpdated는 값이 변경되면 함수가 실행됨

  ![lifecycle hook 예시2](<../이미지/240430/lifecycle hook 예시2.PNG>)
  ![lifecycle hook 예시2 결과](<../이미지/240430/lifecycle hook 예시 결과.PNG>)

## Lifecycle Hooks 특징
* Vue는 Lifecycle Hooks에 등록된 콜백 함수들을 인스턴스와 자동으로 연결함
* 이렇게 동작하려면 hooks 함수들은 반드시 동기적으로 작성되어야 함== 콜백함수에 넣으면 안됨, 그 자체로 작성해서 사용해야함
* 인스턴스 생애주기의 여러 단계에서 호출되는 다른 hooks도 있으며, 가장 일반적으로 사용되는 것은 onMounted, onUpdated, onUnmounted
* https://vuejs.org/api/composition-api-lifecycle.html

# Vue Style Guide
* Vue의 스타일 가이드 규칙은 우선순위에 따라 4가지 범주로 나눔
* 규칙 범주
  - 우선순위 A : 필수(Essential)
  - 우선순위 B : 적극 권장(Strongly Recommended)
  - 우선순위 C : 권장(Recommended)
  - 우선순위 D : 주의 필요(Use with Cation)
* https://vuejs.org/style-guide/

## 우선순위 별 특징
- A: 필수(Essential)
  - 오류를 방지하는 데 도움이 되므로 어떤 경우에도 규칙을 학습하고 준수
    * v-for에 key 작성하기
    * 동일 요소에 v-if와 v-for 함께 사용하지 않기
- B: 적극 권장(Strongly Recommended)
  - 가독성 및 개발자 경험을 향상시킴
  - 규칙을 어겨도 코드는 여전히 실행되겠지만, 정당한 사유가 있어야 규칙을 위반할 수 있음
- C: 권장(Recommended)
  - 일관성을 보장하도록 임의의 선택을 할 수 있음
- D: 주의 필요(Use with Caution)
  - 잠재적 위험 특성을 고려함

# 참고
## computed 주의사항
* Computed의 반환 값은 변경하지 말것
  * computed의 반환 값은 의존하는 데이터의 파생된 값
    * 이미 의존하는 데이터에 의해 계산이 완료된 값
* 일종의 snapshot이며 의존하는 데이터가 변경될 때만 새 snapshot이 생성됨
* 계산된 값은 읽기 전용으로 취급되어야 하며 변경 되어서는 안됨
* 대신 새값을 얻기 위해서는 의존하는 데이터를 업데이트 해야함
* computed에서 reverse() 및 sort() 사용시 원본 배열을 변경하기 때문에 원본 배열의 복사본을 만들어서 진행해야함
  
  ![computed 주의사항](<../이미지/240430/computed 주의사항.PNG>)

## 배열과 v-for 관련
### 배열 변경 관련 메서드
* v-for와 배열을 함께 사용 시 배열의 메서드를 주의해서 사용해야함
1. 변화 메서드
  - 호출하는 원본 배열을 변경
  - push(), pop(), shift(), unshift(), splice(), sort(), reverse()
2. qoduf rycp
  - 원본 배열을 수정하지 않고 항상 새 배열을 반환
  - filter(), concat(), slice()

### v-for와 배열을 활용해 '필터링/정렬' 활용하기
  * 원본 데이터를 수정하거나 교체하지 않고 필터링하거나 정렬된 새로운 데이터를 표시하는 방법
  1. computed 활용
    - 원본 기반으로 필터링 된 새로운 결과를 생성
    
    ![v-for 필터링 정렬 computed](<../이미지/240430/v-for 필터링 computed.PNG>)

  2. method 활용(computed가 불가능한 중첩된 v-for에 경우 사용)
  
    ![v-for 필터링 정렬 method](<../이미지/240430/v-for 필터링 method.PNG>)

### 배열의 인덱스를 v-for의 key로 사용하지 말것
![v-for key 주의사항](<../이미지/240430/v-for key 주의사항.PNG>)
* 인덱스는 식별자가 아닌 배열의 항목 위치만 나타내기 때문
* 만약 새 요소가 배열의 끝이 아닌 위치 삽입되면 이미 반복된 구성 요소 데이터가 함께 업데이트되지 않기 때문
* 직접 고유한 값을 만들어내는 메서드를 만들거나 외부 라이브러리 등을 활용하는 등 식별자 역할을 할 수 있는 값을 만들어 사용