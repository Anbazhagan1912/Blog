from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializer import RegisterSerializer, LoginSerializer
from rest_framework.status import HTTP_201_CREATED,HTTP_404_NOT_FOUND,HTTP_400_BAD_REQUEST, HTTP_200_OK


class RegistrationView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            serializer = RegisterSerializer(data=request.data)

            if not serializer.is_valid():
                return Response({
                    "data": serializer.errors,
                    "message": "Something went worng"
                }, status=HTTP_400_BAD_REQUEST)
            
            serializer.save()

            return Response({
                "data":{},
                "message": "User Created Successfully",
            }, status=HTTP_201_CREATED)
        
        
        except Exception as e:
            print(e)
            return Response({
                "data": {},
                "message": "Something went worng"
            }, status=HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    
    def post(self, request, *args, **kwargs):
        try:
            serializer = LoginSerializer(data = request.data)

            if not serializer.is_valid():
                return Response({'data': serializer.errors, "message": "Something went worng"}, status=HTTP_400_BAD_REQUEST)
            return Response(data=serializer.get_jwt(serializer.data), status=HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({
                "data": {},
                "message": "Something went worng"
            }, status=HTTP_400_BAD_REQUEST)

