from django.contrib.auth import views as auth_views      # views 때문에 겹쳐서 따로 별칭 지정해줌-path도 별칭으로 변경
from django.urls import path
from common import views

app_name = 'common'

urlpatterns = [
    # import django, django.contrib.auth
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
