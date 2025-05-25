from django.urls import path
from .views import projek_api_list, projek_api_create, projek_api_send

urlpatterns = [
    path('projek/', projek_api_list, name='projek_api_list'),
    path('projek/create/', projek_api_create, name='projek_api_create'),
    path('projek/send/<int:pk>/', projek_api_send, name='projek_send'),
]