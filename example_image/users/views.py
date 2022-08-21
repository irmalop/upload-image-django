from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, ParseError

from .models import User
from .serializers import UserSerializer, UserListSerializer

class  CrearListarUser(APIView):
    permission_classes = (AllowAny, )
    parser_classes = (MultiPartParser, FormParser)
    
    def get(self, request):
        users = User.objects.all().filter(status_delete=False)
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data, status = HTTP_200_OK)
    
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)