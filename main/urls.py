from django.urls import path

from . import views2


urlpatterns = [
    path('', views2.fff, name='hi'),

]