from rest_framework.routers import DefaultRouter
from .views import ProjekViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'projects', ProjekViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
