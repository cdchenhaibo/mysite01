from django.urls import re_path
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    re_path(r'^signup/$', accounts_views.signup, name="signup"),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^settings/$', accounts_views.UserUpdateView.as_view(), name='settings'),
    re_path(r'^password_change/$', accounts_views.UserPasswordChangeView.as_view(), name='password_change'),
    re_path(r'^password_change_done/$', accounts_views.UserPasswordChangeDoneView.as_view(), name='password_change_done'),
]
