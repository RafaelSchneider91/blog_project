from django.shortcuts import render, get_object_or_404  # <------ NEW IMPORT
# import Article model
from .models import Article

# Create your views here.


def index(request):
    # add article
    articles = Article.objects.all()
    return render(request, 'posts.html', {'articles': articles})


def post_detail(request, id):  # <------ NEW
    # display detail page.
    details = get_object_or_404(Article, id=id)
    return render(request, 'details.html', {'details': details})
