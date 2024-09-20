from django.forms import ModelForm, fields
from django import forms
from .models import Product, Category



class ProductForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    desc = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    status = forms.ChoiceField(widget=forms.RadioSelect, choices=Product.availability)
    image = forms.ImageField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    
    class Meta:
        model = Product
        fields = '__all__'


class CategoryForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    
    class Meta:
        model = Category
        fields = '__all__'