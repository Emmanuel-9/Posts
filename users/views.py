from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import PostForm
import datetime as dt
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import ListView,DetailView,UpdateView,DeleteView

# Create your views here.
#def index(request):
#    return render(request,'index.html')
    
    #def get_context_data(self, **kwargs):
    #    stuff = get_object_or_404(Post, id=self.kwargs['pk'])
    #    total_likes = stuff.total_likes()
    #    context['total_likes'] = total_likes
    #    return context

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-pub_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        return context

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title','content','pub_date','category','image']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html' 
    success_url = reverse_lazy('index')   
   
def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.first_name = current_user
            post.save()
        return redirect('index')

    else:
        form = PostForm()
        
    return render(request, 'post.html', {"form": form})
    

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)

            return redirect('index')
    
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }    
    return render(request,'registration/registration_form.html',context)

def settings(request):
    return render('request','user/settings.html')

def email(request):
    return render(request,'user/emails.html')

def bookmark(request):
    return render(request,'user/bookmarks.html')
        


