from django.contrib import admin
from .models import Post    # import 후 from 다음에 blog 부분을 삭제함

# 관리자 페이지에 Post를 등록
admin.site.register(Post)
