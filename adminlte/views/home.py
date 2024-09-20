from django.db.models.expressions import Value
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from adminlte.models import Product
from adminlte.models import Category
from django.db.models import Count
from adminlte.views import category
from adminlte.views import products
from django.contrib import messages

# Create your views here.
def pro_index(request):
    form = Product.objects.all()
    context = {'form':form}
    return render(request, 'products/index.html', context)
    

def cat_index(request):
    form = Category.objects.all()
    context = {'form':form}
    return render(request, 'categories/index.html', context)
