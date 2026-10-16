from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers
from .serializers import SignupSerializer

class SignupView(APIView):
    @extend_schema(
        tags=['Auth'],
        request=SignupSerializer,
        responses={201: inline_serializer('SignupResponse', {'msg': serializers.CharField()})},
    )
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "user created"}, status=201)
        return Response(serializer.errors, status=400)