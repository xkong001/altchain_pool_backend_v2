from rest_framework import serializers
from quickstart.models import *
from quickstart.models import EmailCode


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ['id', 'currency', 'algorithm']


class EmailCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailCode
        fields = ['email', 'code', 'status', 'create']


class AddressBookSerializer(serializers.ModelSerializer):
    #subuser_payment_address = serializers.PrimaryKeyRelatedField(
    #    queryset=SubuserPaymentAddress.objects.all())
    subuser_payment_address = serializers.StringRelatedField(many=True)

    class Meta:
        model = AddressWhiteList
        fields = ['user_uuid', 'currency', 'subuser_payment_address']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid', 'email', 'password']


class AddressBookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressWhiteList
        fields = ['user_uuid', 'address', 'currency', 'ext_data', 'gmt_update']





