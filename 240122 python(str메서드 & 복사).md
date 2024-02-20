# Data Structure
여러 데이터를 효과적으로 사용,관리하기 위한 구조(str,list,dict 등)
## 자료구조
* 컴퓨터 공학에서는 '자료 구조'라고 함
* 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것
![data_struc](%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-1-1.PNG)
데이터 구조활용 
* 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 메서드를 호출하여 다양한 기능을 활용하기

선형 구조(순차리스트, 스택, 큐)와 비선형 구조(트리,그래프)가 중요!

# 메서드
객체에 속한 함수
- 객체의 상태를 조작하거나 동작을 수행
## 메서드의 특징
* 메서드는 클래스 내부에 정의되는 함수
* 클래스는 파이썬에서 '타입을 표현하는 방법'이며 이미 은연중에 사용해 왔음
* 예를 들어 help 함수를 통해 str을 호출해보면 class였다는 것을 확인 가능

> 매직 메서드(help에서 '__ 이름 __'형식으로 작성되어있음) : 개발자가 직접적인 관여는 안하지만 파이썬에서 처리하면서 자동으로 호출되는 메서드

```py
print(help(str))
```
> 메서드나 함수나 결과를 반환하지만 메서드는 데이터타입의 객체가 등장함 -> 객체.메서드()<br>객체가 갖고 있는 함수를 호출하기 때문

>메서드는 클래스에 속해 있는 함수 이며, 각 데이터 타입별로 다양한 기능을 가진 매서드가 존재

```py
# 메서드 호출 예시
print('hello'.capitalize()) # Hello

# 리스트 메서드 예시
numbers =[1,2,3]
numbers.append(4)

print(numbers) #[1,2,3,4]
```

## 문자열 조회/탐색 및 검증 메서드
python에서 is로 시작하면 거의 100% 리턴값이 T/F임
|메서드|설명|
|------|-------|
|s.find(x)|x의 첫번째 위치를 반환. 없으면,-1을 반환|
|s.index(x)|x의 첫번째 위치를 반환. 없으면,오류발생|
|s.isalpha()| 알파벳 문자 여부<br> * 단순 알파벳이 아닌 유니코드 상 Letter(한국어도 포함)|
|s.isupper()|대문자 여부|
|s.islower()|소문자 여부|

### .find(x)
x의 첫번째 위치를 반환. 없으면,-1을 반환
```py
print('banana'.find('a')) # 1
print('banana'.find('z')) # -1
```

### .index(x)
x의 첫번째 위치를 반환. 없으면,오류발생
```py
print('banana'.index('a')) #1

print('banana'.index('z'))
# ValueError: substring not found
```
### .isupper() / .islower()
문자열이 모두 대문자/소문자로 이루어져 있는지 확인
```py
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper()) # True
print(string2.isupper()) # False
print(string1.isupper()) # False
print(string2.isupper()) # False

```

### .isalpha()
문자열이 알파벳으로만 이루어져 있는지 확인
```py
string1 = 'Hello'
string2 = '123'
print(string1.isalpha()) # True
print(string2.isalpha()) # False
```
## 문자열 조작 메서드(새문자열 반환)
문자열은 불변의 데이터 타입이기때문에 원본을 바꿀수 없음
> 아래 설명의 대괄호는 파이썬의 문법이 아니라 선택적으로 넣을 수 있다는 표기(배커스 나우르 표기법)

|메서드|설명|
|------|-------|
|s.relace(old,new[,count])|바꿀 대상 글자를 새로운 글자로 바꿔서 반환|
|s.strip([chars])|공백이나 문자를 제거|
|s.split(sep=None, maxsplit =-1)| 공백이나 특정 문자를 기준으로 분리|
|'separator'.join([iterable])|구분자로 iterable을 합침|
|s.title()|문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 변환|
|s.upper()|모두 대문자로 변경|
|s.lower()|모두 소문자로 변경|
|s.swapcase()|대/소문자 서로 변경|

### .replace(old,new[,count])
바꿀 대상 글자를 새로운 글자로 바꿔서 반환
```py
text = 'Hello, world!'
new_text= text.replace('world', 'Python')
print(new_text) # Hello, Python!
```

### s.strip([chars])
문자열의 시작과 끝에 있는 공백이나 지정한 문자를 제거
> chars = characters
```py
text = '   Hello, world!    '
new_text = text.strip()
print(new_text) # 'Hello, world!'
```

### s.split(sep=None, maxsplit =-1)
지정공백이나 특정 문자를 기준으로 분리하여 문자열 리스트로 반환
```py

text= 'Hello, world!'
words = text.split(',')
print(words) # ['Hello', 'world!']
```

### 'separator'.join(iterable)
구분자로 iterable을 하나의 문자열로 합침<br>
```py
words = ['Hello', 'world!']
text = '-'.join(words)
print(text) # 'Hello-world'
```
split()과 역할이 반대
### 문자열 조작(생성,수정,삭제) 메서드
문자열은 불변이므로 원본 변경을 하지 않는다
```py
text = 'heLLo, woRld!'
new_text1= text.capitalize()
new_text2 = text.title()
new_text3 = text.upper()
new_text4 = text.swapcase()

print(new_text1) # Hello, world!
print(new_text2) # Hello, World!
print(new_text3) # HELLO, WORLD!
print(new_text4) # HEllo, WOrLD!
```

## 매서드는 이어서 사용가능
but, 앞쪽의 데이터 타입이 None이면 불가능

```PY
text = 'heLLo, woRld!'
new_text = text.swapcase().replace('l','z')
print(new_text) # HEzzO, WOrLD!
```

# 리스트 메서드
## 리스트 값 추가 및 삭제 메서드

|메서드|설명|
|------|-------|
|L.append(x)|리스트 마지막에 항목 x를 추가|
|L.extend(m)|iterable한 m의 모든 항목들을 리스트 끝에 추가 (+=와 같은 기능)|
|L.insert(i,x)|리스트 인덱스 i에 항목x를 삽입|
|L.remove(x)|리스트의 가장 왼쪽에 있는 항목x를 제거 항목이 존재하지 않을 경우, ValueError|
|L.pop()|리스트 가장 오른쪽에 있는 항목을 반환 후 제거|
|L.pop(i)|리스트 인덱스 i에 있는 항목을 반환 후 제거|
|L.clear()|리스트의 모든 항목 삭제|

### .append(x) 리스트에만 정의되어있음
리스트 마지막에 항목 x를 추가(한개만 추가)
```py
my_list = [1,2,3]
my_list.append(4)
print(my_list) # [1,2,3,4]
```

```py
print(my_list.append([10,9,8])) # None 리스트는 변경가능한 데이터 타입이어서 원본 변경이 가능함. 원본을 바꾸는 메서드는 리턴값이 없음
```

### .extend(iterable)
리스트에 다른 반복 가능한 객체의 모든 항목을 추가
```py
my_list = [1,2,3]
my_list.extend([4,5,6])
print(my_list) # [1,2,3,4,5,6]
```
### .insert(i,x)
리스트의 지정한 인덱스 i 위치에 항목 x를 삽입
```py
my_list = [1,2,3]
my_list.insert(1,5)
print(my_list) # [1,5,2,3]
```

### .remove(x)
리스트에서 첫번째로 일치하는 항목을 삭제
```py
my_list = [1,2,3]
my_list.remove(2)
print(my_list) # [1,3]
```
### .pop(i)
리스트에서 지정한 인덱스의 항목을 제거하고 **반환**<br>
작성하지 않을 경우 마지막항목을 제거
```py
my_list = [1,2,3,4,5]
item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1) # 5
print(item2) # 1
print(my_list) # [2,3,4]
```
### .clear()
리스트의 모든 항목을 삭제
```py
my_list = [1,2,3]
my_list.clear()
print(my_list) #[]
```
## 리스트 탐색 및 정렬 메서드

|문법|설명|
|------|-------|
|L.index(x,start, end)|리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환|
|L.reverse()|리스트의 순서를 역순으로 변경(정렬X)|
|L.sort()|리스트를 정렬(매개변수 이용가능)|
|L.count(x)|리스트에서 항목 x의 개수를 반환|

### .index(x)
리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환
```py
my_list = [1,2,3]
index = my_list.index(2)
print(index) # 1
```
### .count(x)
리스트에서 항목 x의 개수를 반환
```py
my_list = [1,2,2,3,3,3]
count = my_list.count(3)
print(count) # 3
```
### L.sort()
원본 리스트를 오름차순으로 정렬
```py
my_list = [3,2,1]
my_list.sort()
print(my_list) # [1,2,3]

#내림차순
my_list.sort(reverse=True) #reverse의 기본값이 False
print(my_list) # [3,2,1]
```
#### sorted()
내장함수여서 리스트외의 문자열도 정렬이 가능하고 원본말고 새로운 값을 반환
### L.reverse()
리스트의 순서를 역순으로 변경(정렬X)
```py
my_list = [1,3,2,8,1,9]
my_list.reverse()
print(my_list) # [9,1,8,2,3,1]
```

# 복사
## 데이터 타입과 복사
* 파이썬에서는 데이터의 분류에 따라 복사가 달라짐
* '변경 가능한 데이터 타입'과 '변경 불가능한 데이터 타입'을 다르게 다룸
### 변경 가능한 데이터 타입의 복사
```py
a = [1,2,3,4]
b=a
b[0]=100

print(a) # [100,2,3,4]
print(b) # [100,2,3,4]
```
### 변경 불가능한 데이터 타입의 복사
```py
a = 20
b=a
b=10

print(a) # 20
print(b) # 10
```

## 복사 유형
1. 할당(Assignment)
2. 얕은 복사(Shallow copy)=
모습은 똑같지만 다른 리스트를 만들때
slicing 이용(slicing은 자른 새로운 리스트른 반환 = 주소가 다르다)
3. 깊은 복사(Deep copy)

### 할당
```py
orginal_list = [1,2,3]
copy_list = original_list
print(original_list,copy_list) #[1,2,3] [1,2,3]
copy_list[0] = 'hi'
print(original_list,copy_list) #'hi',2,3] ['hi',2,3]
```
> 할당연산자(=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사

### 얕은 복사
```py
a =[1,2,3]
b= a[:]
print(a,b) # [1,2,3] [1,2,3]

b[0]= 100
print(a,b) #[1,2,3] [100,2,3]
# 슬라이싱을 통해 생성된 객체는 원본 객체아 독립적으로 존재
```
#### 얕은 복사의 한계
```py
a= [1,2,[100,200]]
b= a[:]

b[2][0] = 999
print(a) # [1,2,[999,200]]
#2차원 리스트는 복제불가능...내부객체의 주소가 같기 때문에 함께 변경
```

### 깊은 복사
```py
import copy
original_list = [1,2,[1,2]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0]=100

print(original_list) #[1,2,[1,2]]
print(deep_copied_list) #[1,2,[100,2]]
```

# 참고
## 문자열에 포함된 문자들의 유형을 판별하는 메서드
* isdecimal()
    * 문자열이 모두 숫자 문자(0~9)로만 이루어져 있어야 True
* isdigit()
    * isdecimal()과 비슷하지만, 유니코드 숫자도 인식(①도 숫자로 인식)
* isnumeric()
    * isdigit()과 유사하지만, 몇가지 추가적인 유니코드 문자들을 인식
    (분수, 지수, 루트 기호도 숫자로 인식)