from django.urls import path,include

from . import views

urlpatterns = [
    path('user-list/', views.UserList.as_view()),
    path('user-list/<int:pk>/', views.UserDetails.as_view()),
    path('my-account/activate/<uid>/<token>/', views.ActivateUser.as_view({'get':'activation'})),
]