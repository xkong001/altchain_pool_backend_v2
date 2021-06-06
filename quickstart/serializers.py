from rest_framework import serializers
from quickstart.models import Coin
from quickstart.models import EmailCode


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ['id', 'currency', 'algorithm']


class EmailCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailCode
        fields = ['email', 'code', 'status', 'create']






