from django.urls import path
from .views import insertar

urlpatterns = [
    path('insertar/', insertar, name='insertar'),
]
