from django.shortcuts import render
from .models import Blog
from rest_framework.decorators import APIView
from .serializer import Blogserializer
from rest_framework.status import HTTP_201_CREATED,HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class BlogApi(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            data['user'] = request.user.id
            serializer = Blogserializer(data = data)
            print(serializer)

            if not serializer.is_valid():
                return Response({"data":serializer.errors, 'message':"somthing went worng"}, status = HTTP_400_BAD_REQUEST)
            
            serializer.save()
            
            return Response({"data":"", "message":"Blog Created susse"}, status=HTTP_201_CREATED)
        
        except Exception as e:
            print(e)
            return Response({"data":"", 'message':"somthiddddddng went worng"}, status = HTTP_400_BAD_REQUEST)
