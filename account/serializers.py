from rest_framework import serializers
# from .models import UserProfile
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['email'] = user.email
        return token


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ('id', 'password', 'email', 'phone_number', 'first_name', 'city', 'student', 'advertiser', 'date_created', )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'password', 'email', 'phone_number', 'first_name', 'city', 'student', 'advertiser', 'date_created', )

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('password', 'email','phone_number','first_name', 'city', 'student', 'advertiser', 'date_created')
        extra_kwargs = {
            'last_name': {'required': False},
        }

    # def validate(self, attrs):
    #     if len(attrs['password']) != 5 and type(attrs['password']) != 'int':
    #         raise serializers.ValidationError({"password": "Password fields error."})
    #     if len(attrs['phone_number']) != 9:
    #         raise serializers.ValidationError(
    #             {"phone_number": "Check Number"})
    #     return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],   
            first_name=validated_data['first_name'],   
            city=validated_data['city'],   
            student=validated_data['student'], 
            advertiser=validated_data['advertiser'], 
            phone_number = validate_data['phone_number']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
