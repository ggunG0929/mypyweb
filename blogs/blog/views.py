from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from blog.forms import PostForm
from blog.models import Post, Category


def index(request):
    # 최신글 3개 보내기
    new_post = Post.objects.order_by('-pub_date')[0:3]
    # post_list = Post.objects.all()
    # # 게시글 총 개수
    # total_post = len(post_list)
    # categories = Category.objects.all()     # 카테고리 추가
    context = {'new_post': new_post,
               # 'total_post': total_post, 'categories': categories,    # 개인적으로 인덱스에는 검색, 카테고리, 페이지기호 안넣음
               }
    return render(request, 'blog/index.html', context)


# 포스트 목록
def post_list(request):
    # post_list = Post.objects.all()  # import
    post_list = Post.objects.order_by('-pub_date')  # 생성일 기준 내림차순 정렬
    categories = Category.objects.all()     # 카테고리 추가
    # 게시글 총 개수
    total_post = len(post_list)
    # 검색 처리
    kw = request.GET.get('kw', '')  # 입력폼에서 넘어온 키워드
    if kw:
        post_list = post_list.filter(
            Q(title__icontains=kw) |    # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(author__username__icontains=kw)   # 글쓴이 검색
        ).distinct()
    # 페이지 처리
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 5)     # 페이지당 포스트 개수 - 5   # import
    page_obj = paginator.get_page(page)
    context = {'post_list': page_obj, 'categories': categories, 'total_post': total_post, 'kw': kw, }
    return render(request, 'blog/post_list.html', context)


# 상세 페이지
def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    categories = Category.objects.all()     # 카테고리 추가
    # post_list = Post.objects.all()    # 개인적으로 상세페이지에 검색, 카테고리, 페이지기호 안넣음
    # # 게시글 총 개수
    # total_post = len(post_list)
    context = {'post': post, 'categories': categories,
               # 'total_post': total_post,
               }
    return render(request, 'blog/detail.html', context)


# 글쓰기
@login_required(login_url='common:login')   # import
def post_create(request):
    categories = Category.objects.all()     # 전체 카테고리 가져옴
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)    # (일반속성, 파일)  # 내용과 파일이 들어있는 폼
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()  # 현재 시간  # import django
            post.author = request.user  # 로그인한 사람을 글쓴이로
            post.save()
            return redirect('blog:post_list')   # import
    else:
        form = PostForm()   # 비어있는 폼
    context = {'form': form, 'categories': categories, }
    return render(request, 'blog/post_form.html', context)


# 카테고리 페이지 처리 메서드
def category_page(request, slug):
    current_category = Category.objects.get(slug=slug)  # 현재 카테고리 가져오기
    post_list = Post.objects.filter(category=current_category)  # 현재 카테고리의 포스트 검색
    post_list = post_list.order_by('-pub_date')     # 생성일 내림차순
    categories = Category.objects.all()     # 전체 카테고리(사이드바 구현을 위해)
    all_post_list = Post.objects.all()  # 전체 게시글 목록
    total_post = len(all_post_list)     # 게시글 총 개수
    # 페이지 처리
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 5)  # 페이지당 포스트 개수 - 5   # import
    page_obj = paginator.get_page(page)
    context = {'current_category': current_category, 'post_list': page_obj, 'categories': categories,
               'total_post': total_post, }
    return render(request, 'blog/post_list.html', context)


@login_required(login_url='common:login')
def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)     # 삭제할 포스트
    post.delete()
    return redirect('blog:post_list')


@login_required(login_url='common:login')
def post_modify(request, post_id):
    post = get_object_or_404(Post, pk=post_id)  # post_id를 pk로 함
    categories = Category.objects.all()     # 카테고리 전체 정보 가져오기
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)    # post의 정보를 가져옴
        if form.is_valid():                     # 유효성검사 후
            post = form.save(commit=False)      # 가저장
            post.modify_date = timezone.now()   # 수정일을 지정
            post.save()                         # 찐저장
            return redirect('blog:detail', post_id=post_id)    # 수정한 post 페이지로 넘어가기
    else:
        form = PostForm(instance=post)
    context = {'form': form, 'categories': categories, }
    return render(request, 'blog/post_form.html', context)
