from django.urls import path

from . import views

urlpatterns = [
    path('latest-products/', views.LatestProduct.as_view()),
    path('category/', views.ProductCategory.as_view()),
    path('latest-products/<int:pk>/', views.ProductDetail.as_view()),
    path('latest-products/<str:name>/', views.ProductDetail.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('user-list/', views.UserList.as_view()),
    path('user-list/<int:pk>/', views.UserDetails.as_view()),
    path('my-account/activate/<uid>/<token>/', views.ActivateUser.as_view({'get':'activation'}))
]