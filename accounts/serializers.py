from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    def create(self,validated_data):
        user=get_user_model().objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name',""),
            last_name=validated_data.get('last_name',"")
        )
        return user
    class Meta:
        model=get_user_model()
        fields=('id','email','password','first_name','last_name')
        extra_kwargs={'password':{'write_only':True}}  #password field is not visible in the response 

        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    id = serializers.CharField(max_length=15, read_only=True)  
    token = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(write_only=True)  # This should not be read_only

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)  # Correct key is "password"
        
        if email is None:
            raise serializers.ValidationError("Email is required for Login")
        if password is None:
            raise serializers.ValidationError("Password is required for Login")
        
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid Email or Password")
        if not user.is_active:
            raise serializers.ValidationError("User is not active")
        
        return {
            "email": user.email,
            "id": user.id
        }
