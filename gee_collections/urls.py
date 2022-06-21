from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from order.views import admin_order_pdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/admin_order_pdf/<str:order_id>/', admin_order_pdf, name='admin_order_pdf'),
    path('api/v1/',include('djoser.urls')),
    path('api/v1/',include('djoser.urls.authtoken')),
    path('api/v1/',include('product.urls')),
    path('api/v1/',include('order.urls')),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

