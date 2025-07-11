from rest_framework import serializers
from .models import CarChoice
from django.contrib.auth import get_user_model

User = get_user_model()

class CarChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarChoice
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):

    shopcar = CarChoiceSerializer(read_only = True, many = True)
    class Meta:
        model = User
        fields = '__all__'