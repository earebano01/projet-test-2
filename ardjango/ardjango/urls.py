from django.urls import path, include
from rest_framework.routers import SimpleRouter
from ardjango.views import TemperatureDataViewSet
from . import views

router = SimpleRouter()
router.register(r'temperature-data', TemperatureDataViewSet)
router.register('temperature', TemperatureDataViewSet, basename='temperature')

urlpatterns = [
    path('api/', include(router.urls)),
    path('temperature/', views.temperature, name='temperature'),
    
]

