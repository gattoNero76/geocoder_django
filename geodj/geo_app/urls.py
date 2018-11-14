from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),
    # ???
    # url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
    # path('download/', views.download, name='download'),
]
