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