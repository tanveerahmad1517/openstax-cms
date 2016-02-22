from django.conf.urls import include, url
from rest_framework import routers
from .views import ImageViewSet, UserView  


router = routers.DefaultRouter()
router.register(r'v0/images', ImageViewSet)
router.register(r'user', UserView, 'user')

urlpatterns = [
    url(r'^', include(router.urls)),
]
