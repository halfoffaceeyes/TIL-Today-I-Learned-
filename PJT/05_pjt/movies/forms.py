from django import forms
from .models import Movie,Comment

class Movieform(forms.ModelForm):
    score= forms.FloatField(max_value=5,min_value=0,step_size=0.5)
    class Meta:
        model = Movie
        fields = ('title','description','genre','score',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)