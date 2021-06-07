import hashlib
import os
import time
import uuid
import urllib.parse
import base64

from rest_framework import status, generics
from quickstart.models import AddressWhiteList, EmailCode, CurrencyStatus, Subuser, User, SubuserObserver
from quickstart.serializers import EmailCodeSerializer, AddressBookSerializer, UserSerializer, \
    AddressBookListSerializer, PoolStatusSerializer, SubuserExistSerializer, UserConfigSerializer, \
    MiningAccountSerializer, ObserverAccountSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from random import randint
from Crypto.Cipher import AES
from Crypto import Random


@api_view(['POST'])
def email_code_gen(request):
    """
    Manage request for user account email
    """
    email_decode = urllib.parse.unquote(request.data.get('email'))
    serializer_data = {'code': randint(100000, 999999),
                       'email': email_decode,
                       'status': 1,
                       'create': int(time.time())}
    serializer = EmailCodeSerializer(data=serializer_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def modify_withdraw_percent(request):
    """
    modify withdraw percent with given account id and currency
    """
    account_id = request.data.get('accountId')
    currency = request.data.get('currency')
    queryset = AddressWhiteList.objects.filter(currency=currency)
    serializer_class = AddressBookSerializer(queryset, many=True)
    return Response(serializer_class.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def user_register(request):
    """
    register for login user
    Note:
    As talked on 06/07/2021, register need check email code. email code has expiration time.
    This expiration time not defined yet. In here, API do not check the code expiration time.
    """
    new_user_email = request.data.get('email')
    new_user_code = request.data.get('emailCode')
    new_user_pwd = request.data.get('pwd')

    # uuid - 16 bit gen
    new_uuid = uuid.uuid1().bytes

    # encode given pwd
    iv = Random.new().read(AES.block_size)
    private_key = pad("The private key")
    aes = AES.new(private_key.encode("utf8"), AES.MODE_CBC, iv)
    cipher_passwd = aes.encrypt(pad(new_user_pwd).encode("utf8"))

    # check email code:
    stored_email_code = EmailCode.objects.filter(email=new_user_email).first().code

    # ===============check expiration time =====================
    #                          TBD
    # ==========================================================

    # check code
    if stored_email_code == new_user_code:
        serializer_data = {'uuid': new_uuid,
                           'email': new_user_email,
                           'password': str(cipher_passwd)
                           }
        serializer = UserSerializer(data=serializer_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_address_book_list(request):
    input_currency = request.GET['currency']
    queryset = AddressWhiteList.objects.filter(currency=input_currency)
    serializer_class = AddressBookListSerializer(queryset, many=True)
    return Response(serializer_class.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_pool_status(request):
    queryset = CurrencyStatus.objects.all()
    serializer_class = PoolStatusSerializer(queryset, many=True)
    return Response(serializer_class.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def subuser_exist(request):
    input_subuser_name = request.GET['name']
    queryset = Subuser.objects.filter(name=input_subuser_name)
    serializer_class = SubuserExistSerializer(queryset, many=True)
    if serializer_class.data:
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def check_permission(request):
    input_subuser_name = request.GET['name']
    hardcode_return_data = {
        "viewPermission": True,
        "billPermission": True
    }
    return Response(hardcode_return_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_config(request):
    """
    This function do not have any input due to frontend security.
    Hard code a test user uuid below for dev/test
    """
    user_uuid = '1234567890123456'
    queryset = User.objects.filter(uuid=user_uuid)
    serializer_class = UserConfigSerializer(queryset, many=True)
    if serializer_class.data:
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_mining_account(request):
    """
    This function do not have any input due to frontend security.
    Hard code a test user uuid below for dev/test
    """
    user_uuid = '1234567890123456'
    queryset = Subuser.objects.filter(user_uuid=user_uuid)
    serializer_class = MiningAccountSerializer(queryset, many=True)
    if serializer_class.data:
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_observer_account(request):
    """
    This function do not have any input due to frontend security.
    Hard code a test user uuid below for dev/test
    """
    user_uuid = '1234567890123456'
    queryset = SubuserObserver.objects.filter(observer_user_uuid=user_uuid)
    serializer_class = ObserverAccountSerializer(queryset, many=True)
    if serializer_class.data:
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# ============== suppoet function =================
def pad(s):
    block_size = 16
    remainder = len(s) % block_size
    padding_needed = block_size - remainder
    return s + padding_needed * ' '
