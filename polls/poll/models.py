from django.db import models


# 질문 테이블()
class Question(models.Model):   # 상속관계
    # 필드
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self):  # 객체 정보를 문자열로 반환
        return self.question_text


# 항목 테이블(엔티티)
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

# >>> q = Question(question_text='당신의 취미는 무엇인가요?', pub_date=timezone.now())
# >>> q.save()
# >>> q.id
# 1
# >>> q.question_text
# '당신의 취미는 무엇인가요?'
# >>> q.pub_date
# datetime.datetime(2023, 6, 15, 3, 2, 58, 866836, tzinfo=datetime.timezone.utc)
# >>> q2 = Question(question_text='당신이 좋아하는 음식은 무엇인가요?', pub_date=timezone.now())
# >>> q2.save()
# >>> Question.objects.all()
# <QuerySet [<Question: Question object (1)>, <Question: Question object (2)>]>
# >>> quit()
# (myvenv) PS C:\mypyweb\polls> python manage.py shell
# Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from poll.models import Question
# >>> from django.utils import timezone
# >>> Question.objects.all()
# <QuerySet [<Question: 당신의 취미는 무엇인가요?>, <Question: 당신이 좋아하는 음식은 무엇인가요?>]>
# >>> Question.objects.get(id=2)
# <Question: 당신이 좋아하는 음식은 무엇인가요?>
# >>> data = Question.objects.get(id=2)
# >>> data.question_text
# '당신이 좋아하는 음식은 무엇인가요?'
# >>> data.question_text = '당신이 좋아하는 영화는 무엇인가요?'    # 수정
# >>> data.save()
# >>> c = Choice(choice_text='영화감상', votes=0, question=q)
# >>> c.save()
# >>> c.choice_text
# '영화감상'
# >>> c = Choice(choice_text='컴퓨터게임', votes=0, question=q)
# >>> c.save()
# >>> c = Choice(choice_text='독서', votes=0, question=q)
# >>> c.save()
# >>> q.choice_set.all()
# <QuerySet [<Choice: 영화감상>, <Choice: 컴퓨터게임>, <Choice: 독서>]>
