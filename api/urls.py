from django.urls import path
from api.views import CheckoutSessionView, ItemPageView, IndexPageView

urlpatterns = [

    path('', IndexPageView.as_view(), name='index'),
    path('item/<int:pk>', ItemPageView.as_view(), name='item'),
    path('buy/<int:pk>/', CheckoutSessionView.as_view(), name='checkout')
]
