from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import BaseLoginSerializer
import jwt
from django.conf import settings


class BaseLoginView(APIView):
    def post(self, request):
        serializer = BaseLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            payload = {
                'user_id': user.id,
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
            return Response({'token': token}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
