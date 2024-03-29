from django.urls import path,include

from . import views

urlpatterns = [
    # path('checkout/', views.CheckOut.as_view()),
    path('checkout/', views.checkout),
    path('generate-receipt/', views.generate_receipt),
    path('mpesa-payments/',views.MpesaDetails.as_view()),
    path('orders/', views.OrdersList.as_view()),
    path('orders/<str:pk>/', views.OrdersDetails.as_view()),
    path('my-orders/', views.MyOrdersList.as_view()),
    # path('my-orders-pagination/', views.OrdersPagination.as_view()),
    path('my-orders/<str:pk>/', views.MyOrderDetails.as_view()),
    path('access/token/',views.getAccessToken),
    path('online/lipa/', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    # register, confirmation, validation and callback urls
    path('c2b/register', views.register_urls, name="register_mpesa_validation"),
    path('c2b/confirmation', views.confirmation, name="confirmation"),
    path('c2b/validation', views.validation, name="validation"),
    path('c2b/callback', views.call_back, name="call_back"),
    path('invoice-pdf/<str:order_id>/',views.orderInvoicePDF, name="invoice"),
    path('receipt-pdf/<str:order_id>/',views.orderReceiptPDF, name="receipt"),
    path('generate-coupon/', views.couponGen),
    path('coupons/', views.CouponsList.as_view()),
    path('coupons/<str:coupon_order>/', views.CouponDetails.as_view()),
    path('coupons-list/<str:pk>/', views.CouponDetails.as_view()),
]