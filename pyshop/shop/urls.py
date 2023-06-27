from django.urls import path

from . import views     # shop 지우고 .으로

app_name = 'shop'

urlpatterns = [
    path('', views.product_in_category, name='product_all'),  # import views # import path
    # 뷰는 같고 path, name은 다름
    path('<slug:category_slug>/', views.product_in_category, name='product_in_category'),
    path('<int:id>/<product_slug>/', views.product_detail, name='product_detail'),
]
