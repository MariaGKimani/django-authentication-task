from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, PasswordResetView
from .views import signup_view, password_reset_confirm, password_reset_request
from django.contrib.auth.mixins import LoginRequiredMixin


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('signup/', signup_view, name='signup'),
    path('password-reset/', password_reset_request, name='password_reset_request'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', password_reset_confirm,
         name='password_reset_confirm'),  # Custom confirmation view
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
