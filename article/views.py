from django.shortcuts import render, HttpResponse, redirect
from .forms import ArticleForm
from django.contrib import messages
from .models import Article


# Create your views here.
def index(request):
     return render(request, 'index.html',{'number':[1,2,3,4,5]})

def about(request):
     return render(request, 'about.html')  

def detail(request,id):
     return HttpResponse('Detail:' +str(id)) 

def dashboard(request):
     articles = Article.objects.filter(author=request.user)
     context ={
          "articles":articles
     }

     return render(request, 'dashboard.html',context)     

def addArticle(request):
     form = ArticleForm(request.POST or None)

     if form.is_valid():
          article = form.save(commit=False)

          article.author = request.user
          article.save()
          messages.success(request, "Article created successfully")
          return redirect("index")


     return render(request, 'addarticle.html',{"form":form})        

