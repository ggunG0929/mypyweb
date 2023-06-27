from django.shortcuts import render, get_object_or_404

from shop.models import Category, Product


def index(request):
    return render(request, 'shop/index.html')


def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()     # 카테고리 목록   # import category
    products = Product.objects.filter(available_display=True)   # import Product
    if category_slug:
        # 현재 카테고리 1개 가져옴
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)
    context = {
        'current_category': current_category,
        'categories': categories,
        'products': products,
    }
    return render(request, 'shop/list.html', context)


# 상세 페이지
def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    context = {'product': product}
    return render(request, 'shop/detail.html', context)
