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
    subuser_payment_address = serializers.PrimaryKeyRelatedField(
        queryset=SubuserPaymentAddress.objects.all())

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


class PoolStatusSerializer(serializers.ModelSerializer):
    blocks = serializers.SerializerMethodField()
    hashrate = serializers.SerializerMethodField()
    miners = serializers.SerializerMethodField()
    workers = serializers.SerializerMethodField()

    class Meta:
        model = CurrencyStatus
        fields = ['currency', 'income', 'mean_income_24h', 'income_hashrate', 'usd',
                  'cny', 'network_hashrate', 'blocks', 'hashrate', 'miners', 'workers']

    @staticmethod
    def get_blocks(obj):
        currency_pool_status = CurrencyPoolStatus.objects.get(currency=obj.currency)
        return currency_pool_status.blocks

    @staticmethod
    def get_hashrate(obj):
        currency_pool_status = CurrencyPoolStatus.objects.get(currency=obj.currency)
        return currency_pool_status.hashrate

    @staticmethod
    def get_miners(obj):
        currency_pool_status = CurrencyPoolStatus.objects.get(currency=obj.currency)
        return currency_pool_status.miners

    @staticmethod
    def get_workers(obj):
        currency_pool_status = CurrencyPoolStatus.objects.get(currency=obj.currency)
        return currency_pool_status.workers


class SubuserExistSerializer(serializers.ModelSerializer):
    """
    Create this serializer only for subuser check
    In case code conflict, add this serializer with key word "Exist"
    """

    class Meta:
        model = Subuser
        fields = ['name']


class PermissionSerializer(serializers.ModelSerializer):
    """
    Not ready for this API yet. DB missing data.
    Based on the meeting on 06/06/2021, at this point only return True to all permissions
    """

    class Meta:
        fields = ['viewPermission', 'billPermission']


class FollowWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowWallet
        fields = ['uuid', 'wallet']


class UserConfigSerializer(serializers.ModelSerializer):
    """
    Get all user config
    """
    follow_wallet = FollowWalletSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['uuid', 'follow_wallet']


class MiningAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subuser
        fields = '__all__'


class ObserverAccountSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    memo = serializers.SerializerMethodField()
    account_stat = serializers.SerializerMethodField()
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = SubuserObserver
        fields = ['subuser_uuid', 'name', 'memo', 'account_stat', 'img_url']

    @staticmethod
    def get_name(obj):
        sub_user = Subuser.objects.get(uuid=obj.subuser_uuid)
        return sub_user.name

    @staticmethod
    def get_memo(obj):
        sub_user = Subuser.objects.get(uuid=obj.subuser_uuid)
        return sub_user.memo

    @staticmethod
    def get_account_stat(obj):
        sub_user = Subuser.objects.get(uuid=obj.subuser_uuid)
        return sub_user.account_stat

    @staticmethod
    def get_img_url(obj):
        sub_user = Subuser.objects.get(uuid=obj.subuser_uuid)
        return sub_user.img_url