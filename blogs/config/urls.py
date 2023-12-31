from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('blog/', include('blog.urls')),    # import django
    path('common/', include('common.urls')),    # 일반 로그인
    path('accounts/', include('allauth.urls')),     # 소셜 로그인
]

urlpatterns += static(settings.MEDIA_URL,   # import django.conf
                      document_root=settings.MEDIA_ROOT)
