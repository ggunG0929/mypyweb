from django.urls import path

from cart import views

app_name = 'cart'

urlpatterns = [
    path('', views.detail, name='detail'),  # 장바구니 상세페이지    # import path, views
    path('add/<int:product_id>/', views.add, name='product_add'),   # 장바구니에 제품추가
    path('remove/<int:product_id>/', views.remove, name='product_remove'),  # 장바구니에 제품삭제
]
