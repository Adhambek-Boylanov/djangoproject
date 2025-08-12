from msilib.schema import ListView

from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView,ListView,UpdateView
from .models import *
from .forms import NewsForm,SearchForm
from .models import *
def info(request):
    cat = Category.objects.all()
    news = News.objects.all()
    context = {
        "cat":cat,
        "news":news
    }
    return render(request,'index.html',context=context)

def category(request,pk):
    cat = Category.objects.all()
    news = News.objects.filter(category_id = pk)
    context = {
        "cat":cat,
        "news":news
    }
    return render(request,'category.html',context=context)

def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request,'add_news.html',{'form':form})

def detail_new(request,pk):
    new = get_object_or_404(News,id = pk)
    context = {
        'new':new
    }
    return render(request,'detail_new.html',context=context)

def del_new(request,pk):
    new = get_object_or_404(News,id = pk)
    new.delete()
    cat = Category.objects.all()
    news = News.objects.all()
    context = {
        "cat": cat,
        "news": news
    }
    return render(request, 'index.html', context=context)

def update_new(request,pk):
    new = get_object_or_404( News, id = pk)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=new)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm(instance=new)
    return render(request,'update_new.html',{'form':form,'new':new})


def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():






# class HomeNews(ListView):
#     model = News
#     template_name = 'index.html'
#     context_object_name = 'news'
#     # extra_context = {'title':'News title'}
#     def get_context_data(self,*,object_list=None,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title']='News title'
#         context['cat'] = Category.objects.all()
#         return context
#     def get_queryset(self):
#         return News.objects.filter(is_bool = True)
#
# class NewsByCategory(ListView):
#     model = News
#     template_name = 'detail_new.html'
#     context_object_name = 'news'
#     allow_empty = False
#     def get_context_data(self,*,object_list = None,**kwargs):
#         context = super().get_context_data(*kwargs)
#         context['cat']= Category.objects.all()
#         context['news'] = News.objects.all()
#         return context
#     def get_queryset(self):
#         return News.objects.filter(category=self.kwargs['pk'])
# class ViewNews(DetailView):
#     model = News
#     context_object_name = 'news'
#     template_name = 'index.html'
#     pk_url_kwarg = 'pk'
#
# class CreateNews(CreateView):
#     form_class = NewsForm
#     template_name = 'add_news.html'
#     success_url = reverse_lazy('home')
#
# class UpdateNews(UpdateView):
#     form_class = NewsForm
#     template_name = 'update_new.html'
#     success_url = reverse_lazy('home')
#     pk_url_kwarg = 'pk'







































