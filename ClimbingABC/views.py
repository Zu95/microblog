from django.shortcuts import render
from ClimbingABC.models import Category
from ClimbingABC.models import Post
from ClimbingABC.models import QuestionAnswer
from .forms import QuestionForm
from django.shortcuts import redirect
from django.utils import timezone

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


def question(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.asked_date = timezone.now()
            question.save()
            return redirect('question_asked')
    else:
        form = QuestionForm()
    return render(request, 'question.html', {'categories': categories,
                                             'form': form,})


def question_asked(request):
    categories = Category.objects.all()
    return render(request, 'question_asked.html', {'categories': categories})


def questionanswers(request):
    categories = Category.objects.all()
    questions_answers = QuestionAnswer.objects.filter(published=True)
    return render(request, 'questions_answers.html', {'categories': categories,
                                                      'questions_answers': questions_answers})
