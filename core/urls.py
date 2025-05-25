# urls.py
from django.urls import path
from .views import projek_list, projek_create, projek_update, projek_delete

urlpatterns = [
    path('', projek_list, name='projek_list'),
    path('create/', projek_create, name='projek_create'),
    path('update/<int:pk>/', projek_update, name='projek_update'),
    path('delete/<int:pk>/', projek_delete, name='projek_delete'),
]