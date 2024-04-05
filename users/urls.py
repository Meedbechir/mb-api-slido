from django.urls import path
from users.views import UserRegistrationView, UserLoginView, SendPasswordResetEmailView, UserPasswordResetView, CheckEmailExistsView

urlpatterns = [
        path('register/', UserRegistrationView.as_view(), name='register'),
        path('check-email/', CheckEmailExistsView.as_view(), name='check_email_exists'),
        path('login/', UserLoginView.as_view(), name='login'),
        path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
        path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
       
]