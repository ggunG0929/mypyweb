from django.urls import path
from . import views     # 적어야 됨

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),        # 목록       # import path django
    path('<int:post_id>/', views.detail, name='detail'),            # 상세페이지
    path('post/create/', views.post_create, name='post_create'),    # 포스트 생성
    path('category/<str:slug>/', views.category_page, name='category_page'),    # 카테고리별 페이지
]
