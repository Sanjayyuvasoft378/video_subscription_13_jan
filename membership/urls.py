
from django.urls import path
from .views import *

app_name = 'membership'

urlpatterns = [
    path('',MembershipSelectView.as_view(),name='select'),
    path('payment',PaymentView,name='payment'),
]

