from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from adminlte.models import Product
from adminlte.forms import ProductForm
from django.contrib import messages


def addProduct(request):
    form = ProductForm
    context = {'form':form}
    return render(request, 'products/add.html', context) 

def insertProduct(request):
    form = ProductForm
    # validate request method: POST 
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully ..")
            return redirect('product-list')
        elif(form.errors): 
            messages.error(request, "Sorry, product wasn't created.")
    return render(request, 'products/add.html')


    
def editProduct(request, pk):
    # get product data from db
    product_id = Product.objects.get(id = pk)
    form = ProductForm(instance = product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product_id)
        if form.is_valid():
            form.save()
            messages.success(request, "Product data updated successfully ... ")
            return redirect('product-list')
    context = {'form':form}
    return render(request, 'products/edit.html', context)
    

def delProduct(request, pk):
    form = Product.objects.get(id=pk)
    form.delete()
    messages.info(request, "Product was deleted successfully ... ")
    return redirect('product-list')


def bulkDelProduct(request):
    if request.method == "POST":
        p_IDs = request.POST.getlist('product_id')
        form = Product.objects.filter(pk__in=p_IDs)
        form.delete()
        messages.info(request, "Products were deleted successfully ... ")
        return redirect('product-list')
    
    