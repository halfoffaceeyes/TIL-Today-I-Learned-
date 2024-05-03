# PJT 08

### 이번 pjt 를 통해 배운 내용

* 서버의 병목현상을 파악할 수 있는 서버 부하,스트레스 테스트에 대해 배웠다.
* Pandas를 이용하여 데이터 조회 및 변환하는 방법에 대해 배웠다.

## A. CSV 데이터를 DataFrame으로 변환 후 반환
```py
def test_a(request):
    df = pd.read_csv('./data/test_data.CSV', encoding='CP949')
    data = df.to_dict('records')
    return JsonResponse({'dat':data})
```

* 요구 사항 :
  * 제공한 데이터(data/test_data.CSV)를 Django 에서 읽어오도록 구현
  * 프로젝트 경로와 동일한 폴더에 data 폴더를 저장
  * Numpy 혹은 Pandas 의 CSV 를 읽어오는 함수를 활용하여 완성
  * DataFrame 생성 시 columns 옵션을 적절히 활용
  

* 내가 생각하는 이 문제의 포인트
  * Pandas에서 CSV 파일을 읽어오는 함수를 익혀야 함. 
  * Pandas method를 이용하여 Data조회 및 데이터 변환하는 방법을 터득해야 함.

## B. 결측치 처리 후 데이터 반환
```py
@api_view(['get'])
def test_b(request):
    df = pd.read_csv('./data/test_data_has_null.CSV', encoding='CP949')
    df = df.fillna('NULL')
    data = df.to_dict('records')
    return JsonResponse({'dat':data})
```

* 요구 사항 : 비어 있는 값을 'NULL' 문자열로 치환 후 DataFrame을 반환


* 내가 생각하는 이 문제의 포인트
  * fillna를 이용하여 blank를 NULL 문자열로 치환
  * 치환한 데이터를 다시 dict형태로 변환하여 return


## C. 알고리즘 구현하기(평균 나이와 가장 비슷한 10명)
```py
@api_view(['get'])
def test_c(request):
    newdf = df.copy()
    avg_age = df['나이'].mean()
    newdf['나이차이'] = abs(newdf['나이'] - avg_age)
    data = newdf.sort_values(by='나이차이').loc[:, newdf.columns != '나이차이'].head(10).to_dict('records')
    return JsonResponse({'dat':data})
```

* 요구 사항 : 
  * DataFrame 의 “나이” 필드를 활용
  * 평균 나이와 가장 비슷한 나이인 10개 행을 새로운 DataFrame 으로 만들어 반환
  * “나이” 필드에 대해 평균값을 구할 수 있도록 DataFrame 을 전역 변수로 선언하여 문제 해결에 활용
  * “나이” 필드의 데이터 중, 결측치를 제외한 데이터들에 대하여 평균을 계산

* 내가 생각하는 이 문제의 포인트
  * "나이"필드를 이용하여 평균나이 계산
  * 평균값에 가까운 데이터를 구하기 위해 "나이차이" 필드 추가
  * sort_value를 활용하여 나이차이가 가장 적은 데이터부터 오름차순으로 정렬 후 상위 10개 데이터 출력 

## D. Locust를 활용한 알고리즘 성능 측정
|총접속자|동시접속자|평균 RPS|응답시간(평균)|응답시간(50%)|응답시간(95%)|Fail(/s)|
|---|---|---|---|---|---|---|
|100|10|47.9|5|4|11|0|
|500|50|232.4|34|17|53|0|
|500|100|241.3|44|12|50|0.2|
|1000|50|430.7|223|61|820|0.1|
|1000|100|436.9|252|66|950|0.8|
|1000|200|442.6|233|35|940|3.7|
|2000|200|407.7|2781|2800|4200|7.8|
|다|른|조|데|이|터|임|
|1000|50|258.5|1656|1700|2800|0.2|
|1000|50|364.4|633|560|1600|0.5|


* 내가 생각하는 이 문제의 포인트
  * locust 사용법을 익혀야 함.
  * venv에 따라 실행이 안될 수 있음.


# 후기

* 데이터를 직접 수정하는 것보다 조회하는 것이 속도를 개선하는 데 도움이 됨
* Locust 라이브러리 사용법을 배울 수 있었던 좋은 기회였음
* Pandas는 아직 익숙하지 않아서 더 공부해야겠음!