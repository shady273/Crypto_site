from django.urls import path
from . import views

urlpatterns = [
    path('<int:crypto_id>/', views.get_crypto_info_by_id),
    path('<str:crypto_symbol>/', views.get_crypto_info),

]
