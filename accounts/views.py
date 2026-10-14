from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SignupSerializer

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "user created"}, status=201)
        return Response(serializer.errors, status=400)