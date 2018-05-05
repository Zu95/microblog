from django.shortcuts import render
from ClimbingABC.models import Category
from ClimbingABC.models import Post

# Create your views here.


def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def category(request, category_id):
    categories = Category.objects.all()
    current_category = categories.get(id=category_id)
    posts = Post.objects.all().filter(category=category_id)
    return render(request, 'category.html', {'current_category': current_category, 'posts': posts, 'categories': categories})