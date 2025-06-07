from django.urls import path

from . import views2


urlpatterns = [
    path('', views2.fff, name='hi'),
    path('lotto_predict/', views2.lotto_predict, name='lotto_predict'),
    path('fortune_check/', views2.fortune_check, name='fortune_check'),
    path('lotto_history/', views2.lotto_history, name='lotto_history'),
    path('lotto_combiner/', views2.lotto_combiner, name='lotto_combiner'),
]