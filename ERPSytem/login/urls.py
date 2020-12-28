"""ERPSytem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
# from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()


router.register('department',views.DeptViewSet)
router.register('profile',views.UserProfileViewSet)
router.register('attendance',views.AttendanceViewSet)
router.register('salary', views.SalaryReportApiView)
router.register('registeruser',views.RegisterViewSet)
router.register('leave',views.LeaveViewSet)
# router.register('login', views.UserLoginApiView)

urlpatterns = [
    # path('hello-view/', views.HelloApiView.as_view()),
    # path('login/',views.UserLoginApiView.as_view()),
    path('api/', include(router.urls)),
    path('api-auth/',include('rest_framework.urls')),




]
