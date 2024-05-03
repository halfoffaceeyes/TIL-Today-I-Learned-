from django.http import JsonResponse
from rest_framework.decorators import api_view
import pandas as pd

df = pd.read_csv('./data/test_data.CSV', encoding='CP949')

@api_view(['get'])
def test_a(request):
    df = pd.read_csv('./data/test_data.CSV', encoding='CP949')
    data = df.to_dict('records')
    return JsonResponse({'dat':data})


@api_view(['get'])
def test_b(request):
    df = pd.read_csv('./data/test_data_has_null.CSV', encoding='CP949')
    df = df.fillna('NULL')
    data = df.to_dict('records')
    return JsonResponse({'dat':data})


@api_view(['get'])
def test_c(request):
    newdf = df.copy()
    avg_age = df['나이'].mean()
    newdf['나이차이'] = abs(newdf['나이'] - avg_age)
    data = newdf.sort_values(by='나이차이').loc[:, newdf.columns != '나이차이'].head(10).to_dict('records')
    return JsonResponse({'dat':data})
    # 나이 데이터를 문자에서 숫자로 변환, 결측치는 NaN으로 변환
    # df['나이'] = pd.to_numeric(df['나이'], errors='coerce')
    # # 결측치를 제외한 나이 데이터의 평균 계산
    # avg_age = df['나이'].dropna().mean()
    # # df에 평균 나이와의 나이 차이 필드 추가
    # df['나이 차이'] = abs(df['나이'] - avg_age)
    # # 평균 나이와의 나이 차이가 가장 적은 10개의 행을 새로운 DataFrame으로 반환
    # similar_age_df = df.nsmallest(10, '나이 차이')
    # # 임의로 생성했던 나이 차이 필드를 다시 삭제
    # similar_age_df.drop(columns=['나이 차이'], inplace=True)
    # data = similar_age_df.to_dict(orient='records')
    # return JsonResponse({'data': data}, json_dumps_params={'ensure_ascii': False})

    # 민경-선재 코드 
    # df = pd.read_csv('data/test_data.CSV', encoding='cp949')
    # avg = df['나이'].mean(numeric_only=True)
    # df['평균차'] = abs(df['나이'] - avg)
    # closest_data = df.nsmallest(10, '평균차')
    # data = closest_data.to_dict('records')
    # return JsonResponse({'dat': data})