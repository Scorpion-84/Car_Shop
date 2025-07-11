from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.CarViewSetApiView)

urlpatterns = [

    path('', views.all_carchoice),
    path('<int:car_id>', views.car_detail_view),
    path('cbv/', views.CarShopListApiView.as_view()),
    path('cbv/<int:car_id>', views.CarShopDetailApiView.as_view()),
    path('mixins/', views.CarListMixinsApiViews.as_view()),
    path('mixins/<pk>', views.CarDateilMixinsApiViews.as_view()),
    path('generics/', views.CarGenericsApiView.as_view()),
    path('generics/<pk>', views.CarGenericsDetailApiView.as_view()),
    path('viewsets/', include(router.urls)),
    path('users/', views.UserGenericsApiView.as_view()),
]