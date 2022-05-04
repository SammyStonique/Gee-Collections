from django.urls import path,include

from . import views

urlpatterns = [
    # path('checkout/', views.CheckOut.as_view()),
    path('checkout/', views.checkout),
    path('my-orders/', views.OrdersList.as_view()),
    path('my-orders/<str:pk>/', views.OrderDetails.as_view()),
    path('access/token/',views.getAccessToken),
    path('online/lipa/', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    # register, confirmation, validation and callback urls
    path('c2b/register', views.register_urls, name="register_mpesa_validation"),
    path('c2b/confirmation', views.confirmation, name="confirmation"),
    path('c2b/validation', views.validation, name="validation"),
    path('c2b/callback', views.call_back, name="call_back"),
]