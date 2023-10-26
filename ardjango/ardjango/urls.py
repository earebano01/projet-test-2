from django.urls import path, include
from rest_framework.routers import SimpleRouter
from ardjango.views import TemperatureDataViewSet

router = SimpleRouter()
router.register(r'temperature-data', TemperatureDataViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
