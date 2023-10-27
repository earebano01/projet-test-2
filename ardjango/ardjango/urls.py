from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ardjango.views import TemperatureDataViewSet
from . import views

router = routers.SimpleRouter()
router.register(r'temperature-data', TemperatureDataViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('humidity/', views.humidityView, name='humidity'),
    path('temperature/', views.temperatureView, name='temperature'),
    path('heat_index/', views.heat_indexView, name='heat_index'),
    path('statistics/', views.statisticsView, name='statistics'),
    
]

