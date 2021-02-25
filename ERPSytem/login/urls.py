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
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)




# from rest_framework_simplejwt import views as jwt_views

# from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()

# router.register('login',views.LoginAPIView.,basename='login')
router.register('profilelist',views.UserProfileViewSet)




# router.register('register',views.RegisterViewSet)
# router.register('email-verify',views.VerifyEmail,name='email-verify')

router.register('attendance',views.AttendanceViewSet)
# router.register('checkin',views.CheckInViewSet)
router.register('department',views.DeptViewSet)
router.register('salary', views.SalaryReportApiView)
router.register('leave',views.LeaveViewSet,basename='leave')
router.register('leavetype',views.LeaveTypeViewSet)
router.register('holiday',views.HolidayViewSet)
router.register('dailyupdate',views.DailyUpdateViewSet)
# router.register('userdetail',views.VerifyEmailUserDetailViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/',include('rest_framework.urls')),
    # path('api-token-auth/', views.CustomAuthToken.as_view())
    # path('api/register/',RegisterViewSet.as_view({'get': 'list'}),name='register')
    # path('register/',views.RegisterViewSet.as_view({'get': 'list'}),name ='register'),
    path('register/',views.RegisterView.as_view(),name ='register'),
    path('register/<int:pk>/',views.RUDRegisterView.as_view(),name ='rudregister'),
    # path('remainingLeave/',views.RemainingLeaveView.as_view(),name ='register'),
    path('userdetail/',views.UserDetailView.as_view(),name ='userdetail'),
    path('login/',views.LoginAPIView.as_view(),name = 'login' ),
    path('logout/', views.LogoutAPIView.as_view(), name="logout"),
    path('email-verify/', views.VerifyEmail.as_view(), name="email-verify"),
    # path('email-verfy1/', views.VerifyEmailUserDetail.as_view(), name="email-verify1"),
    path('checkin/', views.CheckInViewSet.as_view({'post': 'create'}), name="checkin"),
    path('checkout/', views.CheckOutViewSet.as_view({'post': 'create'}), name="checkout"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('request-reset-email/', views.RequestPasswordResetEmail.as_view(), name="request-reset-email"),
    # path('password-reset/<uidb64>/<token>/', views.PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    # path('password-reset-complete', views.SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

urlpatterns +=[
    path('api-auth/',include('rest_framework.urls'))
]