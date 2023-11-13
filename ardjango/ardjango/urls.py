from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from ardjango.views import TemperatureDataViewSet, HumidityDataViewSet, CelsiusDataViewSet, FahrenheitDataViewSet, HicDataViewSet, HifDataViewSet
from ardjango.views import HumidityDataViewSet, CelsiusDataViewSet, FahrenheitDataViewSet, HicDataViewSet, HifDataViewSet
from . import views

router = routers.SimpleRouter()
# router.register(r'temperature-data', TemperatureDataViewSet)
router.register(r'humidity-data', HumidityDataViewSet)
router.register(r'celsius-data', CelsiusDataViewSet)
router.register(r'fahrenheit-data', FahrenheitDataViewSet)
router.register(r'hic-data', HicDataViewSet)
router.register(r'hif-data', HifDataViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('humidity/', views.humidityView, name='humidity'),
    path('celsius/', views.celsiusView, name='celsius'),
    path('fahrenheit/', views.fahrenheitView, name='fahrenheit'),
    path('hic/', views.HICView, name='hic'),
    path('hif/', views.HIFView, name='hif'),
    # path('temperature/', views.temperatureView, name='temperature'),
    # path('heat_index/', views.heat_indexView, name='heat_index'),
    # path('statistics/', views.statisticsView, name='statistics'),
    # path('json/', views.jsonView, name='json'),
    
]

