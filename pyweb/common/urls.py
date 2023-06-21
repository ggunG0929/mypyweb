from django.contrib.auth import views as auth_views     # 동시에 적용이 안되어서 as를 통해 별칭을 만들어주어 그냥 views와 구분해준다
from django.urls import path
from common import views

app_name = 'common'

urlpatterns = [
    # 클래스형 LoginView를 사용
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),   # import django.contrib.auth views
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup')
]
