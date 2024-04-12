from django.shortcuts import render,redirect
from .forms import Movieform,CommentForm
from .models import Movie,Comment
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context ={
        'movies':movies,
    }
    return render(request, 'movies/index.html',context)

def create(request):
    if request.method =='POST':
        form = Movieform(request.POST)
        if form.is_valid():
            article =form.save(commit=False)
            article.user=request.user
            article.save()
            return redirect('movies:index')
    else:
        form = Movieform()
    context = {
        'form' : form,
    }
    return render(request, 'movies/create.html',context)

def detail(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    form = CommentForm()
    comments=movie.comment_set.all()
    context={
        'movie':movie,
        'form': form,
        'comments':comments
    }
    return render(request,'movies/detail.html',context)

@login_required
def update(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comments=movie.comment_set.all()
    if request.method =='POST':
        form = Movieform(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie_pk)
    else:
        form = Movieform(instance=movie)
    context = {
        'form':form,
        'movie' : movie,
        'comments':comments
    }
    return render(request,'movies/update.html',context)


@login_required
def comments_create(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    form = CommentForm(request.POST)
    if request.method =='POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user=request.user
            comment.movie = movie
            comment.save()
            return redirect('movies:detail', movie_pk)
    context={
        'movie':movie,
        'form' :form,
    }
    return render(request,'movies/detail.html',context)

@login_required
def delete(request,movie_pk):
    movie= Movie.objects.get(pk=movie_pk)
    if request.method =='POST':
        movie.delete()
        return redirect('movies:index')

@login_required
def comments_delete(request,movie_pk,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method =='POST':
        comment.delete()
        return redirect('movies:detail', movie_pk)
    

