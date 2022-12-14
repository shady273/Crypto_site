from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('calculator', views.calculator, name='calc'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('type', views.get_type_info),
    path('type/<str:type_crypto>', views.get_type, name='type'),
    path('<int:crypto_id>', views.get_crypto_info_by_id),
    path('<str:crypto_symbol>', views.get_crypto_info, name='crypto_name'),
]
