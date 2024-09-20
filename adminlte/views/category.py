from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from adminlte.models import Category
from adminlte.forms import CategoryForm
from django.contrib import messages


def addCategory(request):
    form = CategoryForm
    context = {'form':form}
    return render(request, 'categories/add.html', context) 

def insertCategory(request):
    form = CategoryForm
    # validate request method: POST 
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added successfully ..")
            return redirect('category-list')
        elif(form.errors): 
            messages.error(request, "Sorry, category wasn't created.")
    return render(request, 'categories/add.html')


def editCategory(request, pk):
    category_id = Category.objects.get(id = pk)
    form = CategoryForm(instance = category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category_id)
        if form.is_valid():
            form.save()
            messages.success(request, "Category data updated successfully ...")
            return redirect('category-list')
    context = {'form':form}
    return render(request, 'categories/edit.html', context)
    

def delCategory(request, pk):
    form = Category.objects.get(id=pk)
    form.delete()
    messages.info(request, "Category was deleted successfully ... ")
    return redirect('category-list')



def bulkDelCategory(request):
    if request.method == "POST":
        c_IDs = request.POST.getlist('category_id')
        form = Category.objects.filter(pk__in=c_IDs)
        form.delete()
        messages.info(request, "Categories were deleted successfully ... ")
        return redirect('category-list')
    
    
