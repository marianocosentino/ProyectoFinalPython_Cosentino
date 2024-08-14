from django.urls import path
from .views import register, login_view, edit_profile, CustomPasswordChangeView, user_profile
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('change_password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('profile/', user_profile, name='user_profile'),
]
