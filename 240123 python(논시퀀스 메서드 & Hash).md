# 비시퀀스 데이터 구조
## set
고유한 항목들의 정렬되지 않은 컬렉션<br>
중복 X, 정렬X
|메서드|설명|
|------|---|
|s.add(x)|세트s에 항목x를 추가. 이미 x가 있다면 변화 없음|
|s.clear()|세트s에 모든 항목을 제거|
|s.remove(x)|세트s에서 항목x를 제거. 항목 x가 없을 경우 Key error|
|s.pop()|세트 s에서 랜덤하게 항목을 반환하고, 해당 항목을 제거|
|s.discard|세트 s에서 항목 x를 제거|
|s.update(iterable)|세트 s에 다른 iterable 요소를 추가|
### .add(x)
세트에 x를 추가
```py
my_set = {'a','b','c',1,2,3}
print(my_set) #{1,'b',3,2,'c','a'}
my_set.add(d)
print(my_set) #{1,'b',3,2,'c','d','a'}
my_set.add(d)
print(my_set) #{1,'b',3,2,'c','d','a'} # 중복이 안되므로 똑같은 값을 한번 더 넣으면 추가가 안됨
```

### .clear()
세트의 모든 항목을 제거
```py
my_set = {'a''b''c',1,2,3}
my_set.clear()
print(my_set) # set()
```

### .remove(x)
세트에서 항목 x를 제거
```py
my_set = {'a''b''c',1,2,3}
my_set.remove(2)
print(my_set) # {'b',1,3,'c','a'}
my_set.remove(10)
print(my_set) # KeyError
```
### .remove(x)
세트에서 항목 x를 제거. remove와 달리 에러 없음
```py
my_set = {'a''b''c',1,2,3}
my_set.discard(2)
print(my_set) # {'b',1,3,'c','a'}
my_set.discard(10)
print(my_set) # KeyError
```

### .discard(x)
세트에서 항목 x를 제거. remove와 달리 에러 없음
 - 반환값도 없음
```py
my_set = {'a''b''c',1,2,3}
my_set.discard(2)
print(my_set) # {'b',1,3,'c','a'}
result = my_set.discard(10)
print(result) # None
print(my_set) 
```

### .pop()
세트에서 임의의 요소를 제거하고 반환<br>
우리가 생각하는 random의 확률이 아님<br>
아래 코드 실행시 element에서 1이 많이 나옴 그이유는 자료구조와 관계가 있음->
```py
my_set = {'a''b''c',1,2,3}
element = my_set.pop()
print(element) #1
print(my_set) #{2,3,'b','a','c'}
```

### .update(iterable)
세트에 다른 iterable요소를 추가
(리스트의 extend와 비슷)
```py
my_set={'a','b','c',1,2,3,}
my_set.update([1,4,5])
print(my_set) #{1,2,3,'c',4,5,'b','a'}
```
### 세트의 집합 메서드
|메서드|설명|연산자|
|------|---|------|
|set1.difference(set2)|set1에는 있지만 set2에는 없는 항목으로 세트를 생성 후 반환|set1-set2|
|set1.intersection(set2)|set1과set2 모두 들어있는 항목으로 세트를 생성 후 반환|set1 & set2|
|set1.issubset(set2)|set1의 항목이 모두 set2에 들어있으면 True를 반환|set1 <=set2|
|set1.issuperset(set2)|set1이 set2의 항목을 모두 포함하면 True을 반환|set1>=set2|
|set1.union(set2)|set1또는 set2에 들어있는 항목으로 세트를 생성 후 반환|set1\|set2|

```py
set1 = {0,1,2,3,4}
set2 = {1,3,5,7,9}
print(set1.difference(set2)) #{0,2,4}
print(set1.intersection(set2)) #{1,3}
print(set1.issubset(set2)) #False 하나라도 포함 안하면 False
print(set1.issuperset(set2)) # False 하나라도 포함 안하면 False
print(set1.union(set2)) #{0,1,2,3,4,5,7,9}

```

# dictionary
고유한 항목들의 정렬되지 않은 컬렉션

|메서드|설명|
|---------|----|
|D.clear()|딕셔너리 D의 모든 키/값 쌍을 제거|
|D.get(k)|키 k에 연결된 값을 반환(키가 없으면 None을 반환)|
|D.get(k,v)|키 k에 연결된 값을 반환하거나 키가 없으면 기본값으로 v를 반환|
|D.keys()|딕셔너리 D의 키를 모은 객체를 반환|
|D.values()|딕셔너리 D의 값을 모은 객체를 반환|
|D.items()|딕셔너리 D의 키/값을 모은 객체를 반환|
|D.pop(k)|딕셔너리 D의 키 k를 제거하고 연결됐던 값을 반환(없으면 오류)|
|D.pop(k,v)|딕셔너리 D의 키 k를 제거하고 연결됐던 값을 반환(없으면 v를 반환)|
|D.setdefault(k)|딕셔너리 D에서 키k와 연결된 값을 반환|
|D.setdefault(k,v)|딕셔너리 D에서 키k와 연결된 값을 반환<br> 
k가 D의 키가 아니면 값v와 연결한 키 k 를 D에 추가하고 v를 반환|
|D.update(other)|other내 각 키에 대해 D에 있는 키면 D에 있는 그 키의 값을 other에 있는 값으로 대체<br> other에 있는 각 키에 대해 D에 없는 키면 키/값 쌍을 D에 추가|

### .clear()
딕셔너리 D의 모든 키/값 쌍을 제거
```py
person = {'name': 'Alice', 'age':25}
person.clear()
print(person) #{}

```


### get(key[,default])
키 k에 연결된 값을 반환(키가 없으면 None을 반환)

```py
person = {'name': 'Alice', 'age':25}

print(person.get('name')) # Alice
print(person.get('country')) # None
print(person.get('country','Unknown')) # Unknown

```
### .keys()
딕셔너리의 키를 모은 객체를 반환

```py
person = {'name': 'Alice', 'age':25}

print(person.keys()) # dict_keys(['name', 'age'])

for k in person.keys():
    print(k)
"""
name
age
"""
```
### .values()
딕셔너리의 값을 모은 객체를 반환
```py
person = {'name': 'Alice', 'age':25}

print(person.values()) # dict_values(['Alice', 25])

for k in person.values():
    print(k)
"""
Alice
25
"""
```
### items()
딕셔너리의 키/값을 모은 객체를 반환
```py
person = {'name': 'Alice', 'age':25}

print(person.items()) # dict_items([('name','Alice'),('age',25)])

for k,v in person.items():
    print(k,v)
"""
name Alice
age 25
"""
```

### .pop(k[,default])
딕셔너리의 키 k를 제거하고 연결됐던 값을 반환<br>(없으면 에러나 default를 반환)
```py
person = {'name': 'Alice', 'age':25}

print(person.pop('age')) #25
print(person) # {'name','age'}
print(person.pop('country',None)) # None
print(person.pop('country')) # KeyError
```
### .setdefault(key[,default])
딕셔너리에서 키k와 연결된 값을 반환<br>
키가 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환
-> 이걸 잘 사용할때 키가 없는 경우의 if else문을 안써도 가능할 수 있음
```py
person = {'name': 'Alice', 'age':25}

print(person.setdefault('country','Korea')) # Korea
print(person) # {'name' : 'Alice', 'age' : 25,'country': 'Korea'}

```

### .update([other])
other가 제공하는 키/값 쌍으로 딕셔너리를 갱신 기존 키는 덮어씀 (딕셔너리에 값추가할때 간단하게 사용가능)
```py
person = {'name': 'Alice', 'age':25}
other_person = {'name': 'Jane', 'gender':'Female'}
person.update(other_person)
print(person) # {'name' : 'Jane', 'age' : 25,'gender': 'Female'}
person.update(age=50)
print(person)  # {'name' : 'Jane', 'age' : 50,'gender': 'Female'}
person.update(age=50,country='Korea')
print(person) #  # {'name' : 'Jane', 'age' : 50,'gender': 'Female','country': 'Korea'}
```

# 해시 테이블
해시 함수를 사용하여 변환한 값을 색인(index)으로 삼아 키(key)와 데이터(value)를 저장하는 자료 구조
> 데이터를 효율적으로 저장하고 **검색**하기 위해 사용
> set의 pop메서드 사용시 요소중 문자열과 숫자열이 섞였을 경우 1이 많이 나왔던 이유이기도 함

## 해시 테이블 원리
dict = {
    'John': '521-1234',
    'Lisa': '521-8976',
    'Sandra': '521-9655',
}
list =[
    {John': '521-1234'},
    {'Lisa': '521-8976'},
    {'Sandra': '521-9655'},
]
의 형태의 자료가 어떻게 저장되어 있을까?
> 딕셔너리는 Lisa의 위치가 상관없이 값을 찾을 수 있지만 list는 lisa를 모든 요소에서 하나씩 찾아봐야함 -> 이 차이는 해시테이블때문
> 선형 검색이 아니라 키를 해시 함수를 통해 해시 값으로 변환하고, 이 해시 값을 인덱스로 사용하여 데이터를 저장하거나 검색

![hash](이미지/240123/해시테이블.PNG)
* 데이터 검색이 매우 빠르게 이루어짐

### 해시(Hash)
데이터를 해시함수에 넣으면 인덱스로 반환하여 인덱스를 이용하여 값을 호출함
* 임의의 크기를 가진 데이터를 고정된 크기의 고유한 값으로 **변환**하는 것
* 이렇게 생성된 고유한 값(index값)은 주로 해당 데이터를 **식별**하는 데 사용될 수 있음
    * 일종의 '지문'과 같은 역할
    * 데이터를 고유하게 식별
* 파이썬에서는 해시 함수를 사용하여 데이터를 해시 값으로 변환하며, 이 해시값은 **정수**로 표현됨

### 해시함수(Hash function)
* 임의의 길이의 데이터를 입력받아 고정된 길이의 데이터(해시 값)를 출력하는 함수
* 주로 해시 테이블 자료구조에 사용되며, 매우 빠른 데이터 검색을 위한 컴퓨터 소프트웨어에서 유용하게 사용

### set의 요소 & dictionary의 키와 해시테이블 관계
리스트는 앞에서부터 하나씩 비교하면서 검색해야하지만 set의 경우에는 해쉬함수로 인덱스가 나오기 때문에 in 연산자를 활용했을 때 보다 빠르게 검색가능
* 파이썬에서 세트의 요소와 딕셔너리의 키는 해시 테이블을 이용하여 중복되지 않는 고유값을 저장함
* 세트 내의 각 요소는 해시 함수를 통해 해시 값으로 변환되고, 이 해시 값을 기반으로 해시 테이블에 저장됨
* 마찬가지로 딕셔너리의 키는 고유해야 하므로, 키를 해시 함수를 통해 해시 값으로 변환하여 해시 테이블에 저장
    * 따라서 딕셔너리의 키는 매우 빠른 탐색 속도를 제공하며, 중복된 값을 허용하지 않음

#### 예시
* 정수 값 자체가 곧 해시 값

```py
my_set={3,2,1,9,100,4,87,39,10,52}
print(my_set.pop()) # 1
print(my_set.pop()) # 2
print(my_set.pop()) # 3
print(my_set.pop()) # 100
print(my_set.pop()) # 4
print(my_set.pop()) # 39
print(my_set.pop()) # 9
print(my_set.pop()) # 10
print(my_set.pop()) # 52
print(my_set.pop()) #87
print(my_set) # set()
#위의 결과 값은 고정됨-> 정수값 자체가 해시값이기 때문에 1이 해시함수를 거치면 인덱스 1이 반환됨
# but 문자열은 길이가 바뀌기 때문에 해시함수로 바꾸면 인덱스가 정수가 바뀜
# 결국 pop으로 값을 반환시 해시테이블에서 나열된 순서로 값을 빼내는 것
# 문자열을 섞으면 해시함수가 실행될때마다 인덱스 값이 바뀌기 때문에 위치가 계속 바뀜
```
#### set의 pop 메서드 예시 -문자열
반환 값이 매번 다름
```py
my_set={'a','b','c','d','e','f','g','h','i','j'}
print(my_set.pop()) # a
print(my_set.pop()) # f
print(my_set.pop()) # h
print(my_set.pop()) # h
print(my_set.pop()) # e
print(my_set.pop()) # d
```
#### 파이썬에서의 해시 함수
* 파이썬에서 해시 함수의 동작 방식은 객체 타입에 따라 달라짐
* 정수와 문자열은 서로 다른 타입이며, 이들의 해시 값을 계산하는 방식도 다름
```py
print(hash(1)) # 1
print(hash(1)) # 1
print(hash('a')) # 실행시마다 다름
print(hash('a')) # 실행시마다 다름
```

#### 파이썬에서의 해시 함수 - 정수
* 같은 정수는 항상 같은 해시값을 가짐
* 해시 테이블에 정수를 저장할 때 효율적인 방법
* 예를 들어, hash(1)과 hash(2)는 항상 서로 다른 해시 값을 갖지만, hash(1)은 항상 동일한 해시 값을 갖게 됨.

정수는 항상 같은 해시값을 갖지만 순서대로 되어있는 것은 아님

#### 파이썬에서의 해시 함수 - 문자열
* 문자열은 가변적인 길이를 갖고 있고, 문자열에 포함된 각 문자들의 유니코드 코드 포인트 등을 기반으로 해시 값을 계산
* 이로 인해 문자열의 해시 값은 실행 시마다 다르게 됨
```py
print(hash('a')) # 실행시마다 다름
print(hash('a')) # 실행시마다 다름
```
#### set의 pop메서드의 결과와 해시 테이블의 관계
* pop 메서드는 set에서 임의의 요소를 제거하고 반환
* 실행할 때마다 다른 요소를 얻는다는 의미에서의 "무작위"가 아니라 "임의"라는 의미에서 "무작위"
    * By "arbitrary" the docs don't mean "random"
> 해시 테이블에 나타나는 순서대로 반환하는 것

### hashable
* hash() 함수의 인자로 전달해서 결과를 반환 받을 수 있는 객체를 hashable이라 함
* 대부분의 불변형 데이터 타입은 hashable
* 단, tuple의 경우 불변형이지만 해시 불가능한 객체를 참조할 때는 tuple 자체도 해시 불가능해지는 경우가 있음
#### hashable과 불변성 간의 관계
* 해시 테이블의 키는 불변해야 함
    * 객체가 생성된 후에 그 값을 변경할 수 없어야 함
* 불변 객체는 해시 값이 변하지 않으므로 동일한 값에 대해 일관된 해시 값을 유지할 수 있음
* 단, "hash 가능하다 != 불변하다"
#### 가변형 객체가 hashable하지 않은 이유
* 값이 변경될 수 있기 때문에 동일한 객체에 대한 해시 값이 변경될 가능성이 있음(해시 테이블의 무결성 유지 불가)
* 가변형 객체가 변경되면 해신 값이 변경되기 때문에, 같은 객체에 대한 서로 다른 해시 값이 반환될 수 있음(해 시 값의 일관성 유지 불가)

```py
# TypeError : unhashable type : 'list'
print(hash[1,2,3])
# TypeError : unhashable type : 'list'
my_set = {[1,2,3],1,2,3,4,5}
# TypeError : unhashable type : 'set'
print({3,2}:'a')
```

#### hashable 객체가 필요한 이유
1. 해시 테이블 기반 자료구조 사용
    * set와 dic의 키
    * 중복 값 방지
    * 빠른 검색과 조회
2. 불별성을 통한 일관된 해시 값
3. 안정성과 예측 가능성 유지