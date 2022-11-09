from django.urls import path
from . import views

urlpatterns = [
    path('<crypto_symbol>/', views.get_crypto_info)
]
