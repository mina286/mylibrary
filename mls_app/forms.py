from dataclasses import fields
from django import  forms
from .models import Book,Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={"class": "form-control"}) 
        }

class BookForm(forms.ModelForm):

    class Meta:
        model=Book
        fields='__all__'
        widgets = {
            'category':forms.Select(attrs={"class": "form-control"}),
            'author':forms.TextInput(attrs={"class": "form-control"}),
            'title':forms.TextInput(attrs={"class": "form-control"}),
            'price':forms.NumberInput(attrs={"class": "form-control"}),
            'pages':forms.NumberInput(attrs={"class": "form-control"}),
            'photo_book':forms.FileInput(attrs={"class": "form-control"}),
            'photo_author':forms.FileInput(attrs={"class": "form-control"}),
            'retal_price_day':forms.NumberInput(attrs={"class": "form-control",'id':'retal_price_day'}),
            'retal_period':forms.NumberInput(attrs={"class": "form-control",'id':'retal_period'}),
            'totol_renatl':forms.NumberInput(attrs={"class": "form-control",'id':'totol_renatl'}),
            'status':forms.Select(attrs={"class": "form-control"}),
            'is_active':forms.CheckboxInput(),

        }
 
class SignupForm(UserCreationForm):
     class Meta:
         model=User
         fields=['first_name','last_name','email','username','password1','password2'] 