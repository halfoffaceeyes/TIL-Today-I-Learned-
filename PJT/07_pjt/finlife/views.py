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
    if request.method =='GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductListSerializer(products,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    product = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(product, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def top_rate(request):
    # option = DepositOptions.objects.filter(intr_rate2=DepositOptions.objects.aggregate(Max('intr_rate2'))["intr_rate2__max"])[0]
    option = DepositOptions.objects.all().order_by('-intr_rate2')[0]
    serializer = DepositProductsSerializer(option.product)
    return Response(serializer.data, status=status.HTTP_200_OK)