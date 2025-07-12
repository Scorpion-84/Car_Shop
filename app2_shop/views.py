from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from app1_shop.models import CarChoice
from app1_shop.serializer import CarChoiceSerializer , UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

#region function base view
@api_view(['GET', 'POST'])
def all_carchoice(request = Request):

    if request.method == 'GET':
        shopcar = CarChoice.objects.all()
        car_serializer = CarChoiceSerializer(shopcar, many = True)
        return Response(car_serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CarChoiceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(None, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def car_detail_view(request = Request, car_id = int):

    try:
        car = CarChoice.objects.get(pk = car_id)

    except CarChoice.DoesNotExist:
        return Response(None, status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CarChoiceSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = CarChoiceSerializer(car, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        car.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)

#endregion function base view



#region class base view

class CarShopListApiView(APIView):
    
    def get(self, request=Request):
        shopcar = CarChoice.objects.all()
        car_serializer = CarChoiceSerializer(shopcar, many = True)
        return Response(car_serializer.data, status.HTTP_200_OK)
    def post(self, request=Request):
        
        serializer = CarChoiceSerializer(data = request.data)
        if serializer.is_valid():    
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        else:
            return Response(None, status.HTTP_400_BAD_REQUEST) 

class CarShopDetailApiView(APIView):

    def get_object(self, car_id = int ):
        try:
            car = CarChoice.objects.get(pk = car_id)
            return car

        except CarChoice.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)

    def get(self,request = Request, car_id=int):

        car = self.get_object(car_id)
        serializer = CarChoiceSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request=Request, car_id = int):

        car = self.get_object(car_id)
        serializer = CarChoiceSerializer(car, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request=Request, car_id = int):

        car = self.get_object(car_id)
        car.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)

#endregion class base view


#region mixins

class CarListMixinsApiViews(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = CarChoice.objects.all()
    serializer_class = CarChoiceSerializer

    def get(self, request = Request):
        return self.list(request)
    
    def post(self, request = Request):
        return self.create(request)
    

class CarDateilMixinsApiViews(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    
    queryset = CarChoice.objects.all()
    serializer_class = CarChoiceSerializer

    def get(self, request : Request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request : Request, pk):
        return self.update(request, pk)
    
    def delete(self, request : Request, pk):
        return self.destroy(request,pk)

#endregion


#region generics

class CarGenericsApiView(generics.ListCreateAPIView):
    
    queryset = CarChoice.objects.all()
    serializer_class = CarChoiceSerializer
#    authentication_classes = [BasicAuthentication]
#    permission_classes = [IsAuthenticated]

class CarGenericsDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = CarChoice.objects.all()
    serializer_class = CarChoiceSerializer


#endregion generics


#region viewsets

class CarViewSetApiView(viewsets.ModelViewSet):
    
    queryset = CarChoice.objects.all()
    serializer_class = CarChoiceSerializer


#endregion viewsets


#region users

class UserGenericsApiView(generics.ListAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer


#endregion users

