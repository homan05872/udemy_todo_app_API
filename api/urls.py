from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('tasks', views.TaskViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    path('myself/', views.ManageUserView.as_view(), name='myself'),
    path('', include(router.urls)),
]
