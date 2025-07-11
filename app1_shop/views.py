from django.shortcuts import render
from app1_shop.models import CarChoice
from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

def front_page(request):

    context={
        'shopcar' : CarChoice.objects.all()
    }
    return render(request,'app1_shop/index.html',context)

@api_view(['GET'])
def car_json(request:Request):

    shopcar = list(CarChoice.objects.all().values('id', 'car_choice', 'color_choice', 'many_car'))
    return Response({'shopcar' : shopcar}, status.HTTP_200_OK)