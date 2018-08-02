from django.shortcuts import render,get_list_or_404,redirect

from . import views
from . import models
from django.views.generic import *
from django.contrib.auth.mixins import *
from django.urls import reverse_lazy

# Create your views here.

class TrainingViews(ListView):
    context_object_name='training_list'
    template_name='app/layout.html'
    model=models.Training

class AddTrainingView(LoginRequiredMixin,CreateView):
    login_url='/login'
    model=models.Training
    fields=['thumb','training_type','description',]
    context_object_name='training'
    template_name='app/add_training.html'

class TrainingDetailView(DetailView):
    model=models.Training

    template_name='app/training_detail.html'

class TrainingDeleteView(DeleteView):
    model=models.Training
    context_object_name='training_delete'
    success_url=reverse_lazy('training_list')

class ArticleViews(ListView):

    template_name='app/layout.html'
    model=models.Article
    context_object_name='article_list'


class AddArticleView(LoginRequiredMixin,CreateView):
    login_url='/login'
    model=models.Article
    fields=['title','slug','body','thumb']
    context_object_name='form'
    template_name='app/create_article.html'

class ArticleDetailView(DetailView):
    model=models.Article
    context_object_name='article_detail'

    template_name='app/article_detail.html'
class ArticleDeleteView(DeleteView):
    model=models.Article
    context_object_name='article_delete'
    success_url=reverse_lazy('article_list')

class ActivityViews(TemplateView):
    context_object_name='activity_list'
    template_name='app/layout.html'
    model=models.Activity



class ActivityDetailView(DetailView):
    model=models.Activity

    template_name='app/activity_detail.html'






def login(request):
    if request.method=="GET":
        return render(request,"app/login.html")

    elif request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        user=auth.authenticate(username=username,password=password,email=email)

        if user is not None:
                if user.is_active:
                    auth.login(request,user)
                    next=""
                    if "next" in request.GET:
                            next=request.GET['next']
                    if next == None or next=="":
                        next='/'
                    return redirect(next)

                else:


                    return render(request,"app/login.html",{'error_message':'your account is disabled'})
        else:


            return render(request,"app/login.html",{'error_message':"INVALID USERNAME AND PASSWORD"})

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        auth.models.User.objects.create_user(username=username,password=password,email=email).save()

        user=auth.authenticate(username=username,password=password)
        auth.login(request,user)
        return redirect('/article/create')

    elif request.method=="GET":
        return render(request,"app/register.html")
