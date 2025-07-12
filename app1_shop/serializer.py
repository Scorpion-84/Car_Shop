from rest_framework import serializers
from .models import CarChoice
from django.contrib.auth import get_user_model

User = get_user_model()

class CarChoiceSerializer(serializers.ModelSerializer):
    
    def validate_many_car(self, many_car):
        
        if many_car < 1 or many_car > 5:
            raise serializers.ValidationError('many car is not valid !!!')
        return many_car
    class Meta:
        model = CarChoice
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):

    shopcar = CarChoiceSerializer(read_only = True, many = True)
    class Meta:
        model = User
        fields = '__all__'