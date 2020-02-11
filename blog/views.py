from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.shortcuts import redirect
# Create your views here.
from .forms import PostForm
from .models import Post
from django.conf import   settings
from django.db.models import Q
# from django.contrib.auth.models import User



@login_required
def post_list_view(request):
    post_list = Post.objects.filter(user = request.user, is_published = True).order_by('-published_date')
    context = {'post_list':post_list}
    return render(request,'post_list.html',context)

@login_required
def home(request):
    post_list = Post.objects.filter(is_published=True,post_type="PUB").order_by('-published_date')
    context = {'post_list':post_list}
    return render(request,'home.html',context)
    
@login_required
def post_form(request):
    user = request.user
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # user = user
            post_title = form.cleaned_data.get('post_title')
            post_description = form.cleaned_data.get('post_description')
            is_published = form.cleaned_data.get('is_published')
            type_of_post = form.cleaned_data.get('type_of_post')
            post = form.save(commit = False)
            post.user = user
            post.save()
            return redirect("/")
    else:
        form = PostForm()
        context = {'form':form}
        return render(request,'post_form.html',context)


@login_required
def post_search_view(request):
    query = request.GET.get('q').lower()
    object_list = Post.objects.filter(Q(post_title__contains=query) | Q(post_description__contains=query) | Q(user__username__contains=query),is_published = True, post_type ="PUB")
    context = {'object_list':object_list}
    return render(request,'search_result.html',context)

@login_required
def delete_post_view(request,pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect("/")

@login_required
def edit_post_view(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            post.save()
            return redirect("/")
        else:
            form = PostForm(instance = post)
    else:
        form = PostForm(instance = post)
    return render(request,'edit_post.html',context={'form':form})
