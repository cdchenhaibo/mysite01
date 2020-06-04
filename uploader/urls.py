from django.urls import re_path, path
from . import views

app_name = "uploader"

urlpatterns = [
    path('', views.upload, name='upload'),
    path('list/', views.list, name='list'),
    path('download/<id>',views.download, name='download'),
    path('delete/<id>', views.delete, name='delete'),
]