import re

from django import forms
from django.core.exceptions import ValidationError

from .models import *



class SearchForm(forms.Form):
    title = forms.CharField(max_length=150, label='News',
                                widget=forms.TextInput(attrs={"class":"form-control"}))

# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150,label='News',
#                             widget=forms.TextInput(attrs={"class":"form-control"}))
#     context = forms.CharField(label='Text',required=False,widget=forms.Textarea(attrs={
#         "class":"form-control",
#         "row":5
#     }))
#     is_bool = forms.BooleanField(label='is_bool',initial=True)
#     category = forms.ModelChoiceField(empty_label="Categories",
#                                       label="categories",queryset=Category.objects.all(),
#                                       widget=forms.Select(attrs={"class":"form-control"}))

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title','context','is_bool','category']
        widgets = {
            'title':forms.TextInput(attrs={"class":"form-control"}),
            'context':forms.Textarea(attrs={"class":"form-control"}),
            'category':forms.Select(attrs={"class":"form-control"}),
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d',title):
            raise ValidationError('Title raqam bulmasin')
        return title