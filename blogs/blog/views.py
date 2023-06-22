from django.shortcuts import render, redirect
from django.utils import timezone

from blog.forms import PostForm
from blog.models import Post


def index(request):
    return render(request, 'blog/index.html')


# 포스트 목록
def post_list(request):
    post_list = Post.objects.all()  # import
    context = {'post_list': post_list}
    return render(request, 'blog/post_list.html', context)


# 상세 페이지
def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


# 글쓰기
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)    # (일반속성, 파일)  # 내용과 파일이 들어있는 폼
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()  # 현재 시간  # import django
            post.save()
            return redirect('blog:post_list')   # import
    else:
        form = PostForm()   # 비어있는 폼
    context = {'form': form}
    return render(request, 'blog/post_form.html', context)
