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
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

# router.register('login',views.LoginAPIView.,basename='login')
router.register('profilelist',views.UserProfileViewSet)




# router.register('register',views.RegisterViewSet)
# router.register('email-verify',views.VerifyEmail,name='email-verify')

router.register('attendance',views.AttendanceViewSet)
# router.register('checkin',views.CheckInViewSet)
router.register('department',views.DeptViewSet)
router.register('salary', views.SalaryReportApiView, basename='salary')
# router.register('leave',views.LeaveViewSet)
# router.register('userdetails',views.UserDetailViewSet)
router.register('leave',views.LeaveViewSet,basename='leave')
router.register('leavetype',views.LeaveTypeViewSet)
# router.register('userdetails',views.UserDetailViewSet)
# router.register('userdetail',views.VerifyEmailUserDetailViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/',include('rest_framework.urls')),
    # path('api-token-auth/', views.CustomAuthToken.as_view())
    # path('api/register/',RegisterViewSet.as_view({'get': 'list'}),name='register')
    # path('register/',views.RegisterViewSet.as_view({'get': 'list'}),name ='register'),
    path('register/',views.RegisterView.as_view(),name ='register'),
    path('register/<int:pk>/',views.RUDRegisterView.as_view(),name ='rudregister'),
    path('userdetail/',views.UserDetailView.as_view(),name ='userdetail'),
    path('login/',views.LoginAPIView.as_view(),name = 'login' ),
    path('logout/', views.LogoutAPIView.as_view(), name="logout"),
    path('email-verify/', views.VerifyEmail.as_view(), name="email-verify"),
    # path('email-verfy1/', views.VerifyEmailUserDetail.as_view(), name="email-verify1"),
    path('checkin/', views.CheckInViewSet.as_view({'post': 'create'}), name="checkin"),
    path('checkout/', views.CheckOutViewSet.as_view({'post': 'create'}), name="checkout"),





]

urlpatterns +=[
    path('api-auth/',include('rest_framework.urls'))
]
