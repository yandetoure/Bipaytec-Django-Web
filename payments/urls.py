from django.urls import path
from .views import payment_process

urlpatterns = [
    path('payment/', payment_process, name='payment_process'),
]
