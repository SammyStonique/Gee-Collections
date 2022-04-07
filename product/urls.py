from django.urls import path,include

from . import views

urlpatterns = [
    path('latest-products/', views.LatestProduct.as_view()),
    path('category/', views.ProductCategory.as_view()),
    path('latest-products/<int:pk>/', views.ProductDetail.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('user-profile/', views.UserProfile.as_view()),
    path('user-profile/<str:pk>/', views.ProfileDetail.as_view()),
]