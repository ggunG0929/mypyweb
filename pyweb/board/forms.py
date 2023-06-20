from django import forms

from board.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:     # 중첩클래스
        model = Question    # import
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',    # 한글로 뜨도록
            'content': '내용'
        }
        

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer  # import
        fields = ['content']
        labels = {
            'content': '답변 내용'
        }
