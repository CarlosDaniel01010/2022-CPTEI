from django.urls import path
from .views import ClienteView

urlpatterns = [
    path('clientes', ClienteView.as_view(), name='clientes'),

]