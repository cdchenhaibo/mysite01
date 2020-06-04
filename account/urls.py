from django.conf.urls import re_path
from . import views

from django.conf import settings
from django.contrib.auth import views as auth_views

app_name = "account"
urlpatterns = [
    # re_path(r'^login/$', views.user_login, name='user_login'),
    re_path(r'^login/$', auth_views.login_required(), name='user_login'),
]