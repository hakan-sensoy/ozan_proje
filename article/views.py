from django.contrib import admin
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm,projeForm
from .models import Article,Comment,proje
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})

def proje_get(request):
    keyword = request.GET.get("keyword")

    if keyword:
        projex = proje.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"projex":projex})
    projex = proje.objects.all()

    return render(request,"articles.html",{"articles":projex})

def index(request):
    return render(request,"index.html")
    
def about(request):
    return render(request,"about.html")

@login_required(login_url = "user:login")
def dashboard_two(request):
    articles = proje.objects.filter(author = request.user)
    
    context = {
        "articles":articles
    }
    return render(request,"dashboard_two.html",context)

@login_required(login_url = "user:login")
def add(request):
    form = projeForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        new = form.save(commit=False)
        
        new.author = request.user
        new.save()

        messages.success(request,"product has been successfully created.")
        return redirect("article:dashboard_two")
    return render(request,"Add.html",{"form":form})


def detail(request,id):
    #article = Article.objects.filter(id = id).first()   
    article = get_object_or_404(Article,id = id)

    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})

@login_required(login_url = "user:login")
def update(request,id):

    projex = get_object_or_404(proje,id = id)
    form = projeForm(request.POST or None,request.FILES or None,instance = projex)
    if form.is_valid():
        projex = form.save(commit=False)
        
        projex.author = request.user
        projex.save()

        messages.success(request,"Product has been successfully updated.")
        return redirect("article:dashboard_two")


    return render(request,"update.html",{"form":form})



@login_required(login_url = "user:login")
def delete(request,id):
    projex = get_object_or_404(proje,id = id)

    projex.delete()

    messages.success(request,"The product has been successfully deleted.")

    return redirect("article:dashboard_two")

def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))
    