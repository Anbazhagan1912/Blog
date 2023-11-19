from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.Serializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError('Username already taken !')
        return data
    
    def create(self, validated_data):
        user = User.objects.create(first_name = validated_data['firstname'], 
                                   last_name = validated_data['lastname'], 
                                   username = validated_data['username'].lower()
                                   )
        user.set_password(validated_data['password'])

        return validated_data
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        if not User.objects.filter(username = data['username']).exists():
            raise serializers.ValidationError("Accound Not Found")
        return data
    
    def get_jwt(self, data):
        user = User.objects.filter(username = data['username'], password = data['password']).first()
        if not user:
            return {"message":"invalid Creditials"}
        refresh = RefreshToken().for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }