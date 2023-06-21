from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from board.models import Question
from board.forms import QuestionForm, AnswerForm


def index(request):
    return render(request, 'board/index.html')      # import
    # return HttpResponse("<h1>웹 메인페이지 입니다.</h1>")


def question_list(request):
    # question_list = Question.objects.all()      # import
    question_list = Question.objects.order_by('-create_date')    # 내림차순
    context = {'question_list': question_list}
    return render(request, 'board/question_list.html', context)


def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    # 모델에서 데이터가 있으면 가져오고 없으면 404 페이지 오류 처리를 함
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'board/detail.html', context)


# 질문 등록
@login_required(login_url='common:login')   # 비로그인시 로그인 페이지로 이동 # import
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)   # 입력된 데이터가 있는 폼
        if form.is_valid():     # 폼이 유효성 검사를 통과했다면
            question = form.save(commit=False)      # 가저장(날짜가 없음)
            question.author = request.user  # 로그인한(세션 권한이 있는) 글쓴이
            question.create_date = timezone.now()   # 등록일 생성    # import
            form.save()     # 실제저장
            return redirect('board:question_list')     # 질문 목록 페이지 이동  # import # 콜론 뒤에 띄어쓰면 안됨
    else:
        form = QuestionForm()   # 폼 객체 생성(빈 폼)   # import
    context = {'form': form}
    return render(request, 'board/question_form.html', context)  # get 방식


# 답변 등록
@login_required(login_url='common:login')
def answer_create(request, question_id):
    # 질문이 1개 지정되어야 답변을 등록할 수 있음
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":    # 소문자(post)이면 답변이 등록되지 않음
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)        # content만 저장
            answer.author = request.user  # 로그인한(세션 권한이 있는) 글쓴이
            answer.create_date = timezone.now()     # 답변등록일
            answer.question = question  # 외래키 생성
            form.save()
            return redirect('board:detail', question_id=question.id)    # question.id 주의
    else:
        form = AnswerForm()     # 빈 폼 생성
    context = {'question': question, 'form': form}
    return render(request, 'board/detail.html', context)


# 질문삭제
@login_required(login_url='common:login')
def question_delete(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('board:question_list')

# delete 연습 (shell)
# >>> from board.models import Question
# >>> Question.objects.all()
# <QuerySet [<Question: 여름철 실내 적정온도는 얼마인가요?>, <Question: 파이썬 웹 개발 패턴인 MTV가 무엇인가요?>, <Question: 깃허브란 무엇인가요?>, <Quest
# ion: 좋아하는 색상은?>, <Question: test>, <Question: test>, <Question: test2>, <Question: 취미는?>]>
# >>> q = Question.objects.get(id=5)
# >>> q.subject
# 'test'
# >>> q.delete()
# (1, {'board.Question': 1})
# >>> Question.objects.all()
# <QuerySet [<Question: 여름철 실내 적정온도는 얼마인가요?>, <Question: 파이썬 웹 개발 패턴인 MTV가 무엇인가요?>, <Question: 깃허브란 무엇인가요?>, <Quest
# ion: 좋아하는 색상은?>, <Question: test>, <Question: test2>, <Question: 취미는?>]>
# >>> quit()
