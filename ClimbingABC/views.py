from django.shortcuts import render
from ClimbingABC.models import Category
from ClimbingABC.models import Post

# Create your views here.


def index(request):
    categories = Category.objects.all()
    newest_posts = Post.objects.order_by('-published_date')[:3]
    gallery = Post.objects.order_by('?')[:4]
    return render(request, 'index.html', {'categories': categories,
                                          'newest_posts': newest_posts,
                                          'gallery': gallery})


def category(request, category_id):
    categories = Category.objects.all()
    current_category = categories.get(id=category_id)
    posts = Post.objects.all().filter(category=category_id)
    return render(request, 'category.html', {'current_category': current_category,
                                             'posts': posts,
                                             'categories': categories})


def article(request, category_id, post_id):
    categories = Category.objects.all()
    current_category = categories.get(id=category_id)
    post = Post.objects.get(id=post_id)
    return render(request, 'article.html', {'categories': categories,
                                            'current_category': current_category,
                                            'post': post})
