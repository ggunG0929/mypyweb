from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# UserCreationForm을 상속받은 UserForm 정의함
class UserForm(UserCreationForm):   # import
    email = forms.EmailField(label='이메일')   # import django.forms

    class Meta:     # 중첩클래스 - 내부
        model = User    # import
        fields = ('username', 'email')  # 튜플 구조(리스트와 비교하면 수정하지 못하게 강제성이 있음)
