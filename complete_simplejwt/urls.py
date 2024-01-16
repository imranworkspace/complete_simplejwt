from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from token_api import views

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
router = DefaultRouter()
router.register('studentapi',views.StudentModelView,basename='studentapi')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view()),
    path('refresh_token/',TokenRefreshView.as_view()),
    path('verify_token/',TokenVerifyView.as_view()),
]
