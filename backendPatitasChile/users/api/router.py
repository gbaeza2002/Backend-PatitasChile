from django.urls import path

from users.api.views import (
    RegisterView, 
    UserView, 
    VerifyCodeView, 
    RequestPasswordResetView, 
    VerifyResetCodeView, 
    ResetPasswordView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('me/', UserView.as_view()),
    
    path('verify-code/', VerifyCodeView.as_view(), name='verify_code'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('request-password-reset/', RequestPasswordResetView.as_view(), name='request_password_reset'),
    path('verify-reset-code/', VerifyResetCodeView.as_view(), name='verify_reset_code'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
]