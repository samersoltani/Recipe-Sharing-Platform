from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from.serializers import UserRegistrationSerializer,ProfileSerializer,LogoutSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken


class UserRegistrationApiView(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer
    
    def post(self,request):
        serializer = UserRegistrationSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response({"message": "User registered successfully"})   
    


class ProfileAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get(self,request,*args,**kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class LogoutApiView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer

    def post(self,request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh_token = serializer.validated_data['refresh']

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        
        except InvalidToken as e:
            return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
