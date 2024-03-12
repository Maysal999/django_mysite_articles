from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect 
from .models import Article
def index(request):
    articles_value = Article.objects.all()
    
    return render(request,'articles/main.html',{'article5' : articles_value})
def detail(request,article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        return Http404
    return render(request, 'articles/detail.html', {'article' : a})

