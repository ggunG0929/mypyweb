from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)    # 제목
    content = models.TextField()                # 내용
    pub_date = models.DateTimeField()           # 발행일
    modify_date = models.DateTimeField(null=True, blank=True)   # 입력 폼이 비어도 됨
    photo = models.ImageField(upload_to='blog/images/%Y/%m/%d/',    # 저장될 위치지정. 날짜별로 소문자 m이어야 달(월)
                              null=True, blank=True)    # null 허용, 파일 첨부 X일 수 있음
    
    def __str__(self):
        return self.title   # 이게 있어야 관리자 페이지에서 한글로 나온다고 함
