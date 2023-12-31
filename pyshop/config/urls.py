from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('shop/', include('shop.urls')),    # import include
    path('cart/', include('cart.urls')),
]

urlpatterns += static(settings.MEDIA_URL,   # import static, settings - django.conf
                      document_root=settings.MEDIA_ROOT)
