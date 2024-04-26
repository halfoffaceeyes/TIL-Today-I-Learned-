# PJT 07

## 이번 pjt를 통해 배운 내용

환경 변수 관리

- API KEY와 같이 외부에 노출하면 안되는 정보를 따로 관리
- `pip install django-environ`
- .env 파일 작성
  - `API_KEY='발급받은 API KEY'`
  - 따옴표로 묶어서 문자열 형태로 입력
  - 수정 후 서버를 다시 시작해야 반영됨

```python
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# 위는 원래 있는 애들임, 얘네 바로 밑에 써주자

# settings.py에 아래 코드 추가
import os
import environ

# 환경변수를 불러올 수 있는 상태로 설정
env = environ.Env(DEBUG=(bool, True))

# 환경변수를 읽어올 파일을 설정
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

# 환경변수를 읽어옴
API_KEY = env('API_KEY')

# settings에 등록한 환경변수 사용 방법
# views.py
from django.conf import settings

API_KEY = settings.API_KEY
```

- 이후 .gitignore 파일에 .env를 추가하여 API KEY가 외부에 노출되지 않도록 설정

## 필수 요구사항 - 모델 클래스

### DepositProducts 모델 클래스

- 금융 상품 코드, 금융 회사명, 금융 상품명, 금융 상품 설명, 가입 제한(1: 제한 없음, 2: 서민 전용, 3: 일부 제한), 가입 대상, 가입 방법, 우대 조건

```py
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
```

### DepositOptions 모델 클래스

- 외래 키(DepositProducts 클래스 참조), 금융 상품 코드, 저축금리 유형명, 저축 금리, 최고 우대 금리, 저축 기간(단위: 개월)

```py
class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()
```

### 포인트
- unique 옵션을 사용하면 중복값이 저장되지 않도록 설정할 수 있다

## 필수 요구사항 - view 함수

### finlife 앱의 view함수

```python
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DepositOptions,DepositProducts
from .serializers import DepositOptionsSerializer,DepositProductsSerializer,DepositProductListSerializer
from django.conf import settings
import requests
from django.db.models import Max


# Create your views here.
API_KEY = settings.API_KEY
BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'


# 요청이 오면 정기예금 상품 목록을 받아와 DB에 저장할 수 있도록 코드 구현
@api_view(['GET'])
def save_deposit_products(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': API_KEY, 
        'topFinGrpNo': '020000', 
        'pageNo': 1
    }
    response = requests.get(URL, params=params).json()

    products = response['result']['baseList']    
    productserializer = DepositProductsSerializer(data=products, many=True)
    if productserializer.is_valid(raise_exception=True):
        productserializer.save()
    
    options = response['result']['optionList']
    for option in options:
        fin_prdt_cd = option['fin_prdt_cd']
        optionserializer = DepositOptionsSerializer(data=option)
        product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        if optionserializer.is_valid(raise_exception=True):
            optionserializer.save(product=product)
    return Response(productserializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','POST'])
def deposit_products(request):
    # 요청이 오면 DB에 저장된 정기예금 상품 목록을 반환하도록 코드 구현
    if request.method =='GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductListSerializer(products,many=True)
        return Response(serializer.data)
    # 요청이 오면 요청과 함께 전송한 데이터를 DB에 저장하도록 코드 구현
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 요청이 오면 상품 코드에 따라 해당 상품의 옵션 리스트를 출력하도록 코드 구현
@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    product = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(product, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 요청이 오면 금리가 가장 높은 상품의 상세정보와 옵션을 반환하도록 코드 구현
@api_view(['GET'])
def top_rate(request):
    # option = DepositOptions.objects.filter(intr_rate2=DepositOptions.objects.aggregate(Max('intr_rate2'))["intr_rate2__max"])[0]
    option = DepositOptions.objects.all().order_by('-intr_rate2')[0]
    serializer = DepositProductsSerializer(option.product)
    return Response(serializer.data, status=status.HTTP_200_OK)
```

### finlife 앱의 Serializer

```python
from rest_framework import serializers
from .models import DepositOptions, DepositProducts

    
class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product', )

class DepositProductsSerializer(serializers.ModelSerializer):
    join_deny = serializers.IntegerField(max_value=3, min_value=1)
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields= '__all__'
```

### 포인트
- form의 integerfield에서 max_value, min_value를 설정했듯 serializer의 integerfield에서도 값을 지정해줄 수 있다
- 아래 두가지 코드는 동일한 역할을 한다
```python
# option = DepositOptions.objects.filter(intr_rate2=DepositOptions.objects.aggregate(Max('intr_rate2'))["intr_rate2__max"])[0]
  option = DepositOptions.objects.all().order_by('-intr_rate2')[0]
```

## 후기

- DRF 실습 시간이 부족했다고 느꼈는데 이번 프로젝트를 하면서 헷갈렸던 부분을 학습하고 복습을 진행할 수 있었다
- 외부 API를 사용하기도 하고 직접 API서버를 만들어 보며 기존 서비스의 API 구동 원리를 조금이나마 더 이해하게 되었다
- 외부 API를 사용한다면 데이터를 직접 생성하는 부분에 대해 고려할 일이 없는데 직접 서버를 만들어보며 새로운 부분들에 대해 고려해볼 수 있었다
- 지난 시간에 배웠던 git flow에 대한 필요성을 다시 한번 느낄 수 있었다
- form과 serializer가 확실히 비슷하게 만들어졌음을 확인할 수 있었다
