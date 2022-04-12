from django.urls import path,include

from . import views

urlpatterns = [
    path('checkout/', views.CheckOut.as_view()),
]