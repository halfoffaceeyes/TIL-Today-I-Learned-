from django.shortcuts import render,redirect
from .models import Movie
from .forms import MovieForm,CommentForm
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context={
        'movies':movies,
    }
    return render(request,'movies/index.html',context)

def create(request):
    if request.method =='POST':
        form =MovieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context={
        'form' : form
    }
    return render(request,'movies/create.html',context)

def detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    comment_form=CommentForm()
    comments=movie.comment_set.all()
    context = {
        'movie' : movie,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request,'movies/detail.html',context)

def update(request,pk):
    movie =Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form =MovieForm(request.POST,request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form' : form,
        'movie':movie,
    }
    return render(request,'movies/update.html',context)

def delete(request,pk):
    if request.method =='POST':
        movie=Movie.objects.get(pk=pk)
        movie.delete()
        return redirect('movies:index')
    
def comment_create(request,pk):
    movie=Movie.objects.get(pk=pk)
    comment_form=CommentForm(request.POST)
    if comment_form.is_valid():
        comment=comment_form.save(commit=False)
        comment.movie=movie
        comment.save()
        return redirect('movies:detail', movie.pk)
    context={
        'movie':movie,
        'comment_form' : comment_form,
    }
    return render(request, 'movies/detail.html',context)