from django.shortcuts import render, redirect
from django.utils import timezone

from blog.forms import PostForm
from blog.models import Post, Category


def index(request):
    return render(request, 'blog/index.html')


# 포스트 목록
def post_list(request):
    # post_list = Post.objects.all()  # import
    post_list = Post.objects.order_by('-pub_date')  # 생성일 기준 내림차순 정렬
    categories = Category.objects.all()     # 카테고리 추가
    context = {'post_list': post_list, 'categories': categories}
    return render(request, 'blog/post_list.html', context)


# 상세 페이지
def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    categories = Category.objects.all()     # 카테고리 추가
    context = {'post': post, 'categories': categories}
    return render(request, 'blog/detail.html', context)


# 글쓰기
def post_create(request):
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
    context = {'form': form}
    return render(request, 'blog/post_form.html', context)


# 카테고리 페이지 처리 메서드
def category_page(request, slug):
    current_category = Category.objects.get(slug=slug)  # 현재 카테고리 가져오기
    post_list = Post.objects.filter(category=current_category)  # 현재 카테고리의 포스트 검색
    post_list = post_list.order_by('-pub_date')     # 생성일 내림차순
    categories = Category.objects.all()     # 전체 카테고리(사이드바 구현을 위해)
    context = {'current_category': current_category, 'post_list': post_list, 'categories': categories}
    return render(request, 'blog/post_list.html', context)
