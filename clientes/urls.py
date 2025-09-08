from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, clientes

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')

urlpatterns = [
    path('api/', include(router.urls)),        # rota para API REST
    path('clientes/', clientes, name='clientes')  # rota para template HTML
]