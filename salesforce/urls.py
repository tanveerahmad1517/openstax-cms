from django.conf.urls import include, url
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'', views.SchoolViewSet)

urlpatterns = [
    url(r'^schools/', include(router.urls)),
]
