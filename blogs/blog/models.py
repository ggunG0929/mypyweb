from django.contrib.auth.models import User
from django.db import models


# 카테고리 모델   # 포스트보다 위쪽에 작성해야 함
class Category(models.Model):
    # unique=True: 중복불허, 하지만 PK는 아님
    name = models.CharField(max_length=50, unique=True)
    # url주소 - 문자, allow_unicode - 한글 등 허용
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    
    def __str__(self):
        return self.name
    
    # 카테고리 url 주소
    def get_absolute_url(self):
        return f'/blog/category/{self.slug}'
    
    # 관리자 페이지에서 적용
    class Meta:
        ordering = ['name']     # 이름순 정렬
        verbose_name = 'category'
        verbose_name_plural = 'categories'  # 여러개일때는 문법적으로 복수형으로, 안붙이면 그냥 categorys가 됨


# 포스트 모델
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 글쓴이   # import
    title = models.CharField(max_length=100)    # 제목
    content = models.TextField()                # 내용
    pub_date = models.DateTimeField()           # 발행일
    modify_date = models.DateTimeField(null=True, blank=True)   # 입력 폼이 비어도 됨
    photo = models.ImageField(upload_to='blog/images/%Y/%m/%d/',    # 저장될 위치지정. 날짜별로 소문자 m이어야 달(월)
                              null=True, blank=True)    # null 허용, 파일 첨부 X일 수 있음
    category = models.ForeignKey(Category, null=True, blank=True,   # 카테고리를 외래키로. 이래서 카테고리를 더 위에 적어야 함
                                 on_delete=models.SET_NULL)     # 카테고리가 삭제되어도 Null이 될 뿐 삭제되지는 않음
    
    def __str__(self):
        return self.title   # 이게 있어야 관리자 페이지에서 한글로 나온다고 함
