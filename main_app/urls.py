from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from main_app import views


urlpatterns = [
    url(r'^$', views.index),

]
