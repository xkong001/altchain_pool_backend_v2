import time
import urllib.parse

from rest_framework import status
from quickstart.serializers import EmailCodeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from random import randint

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

