from django.shortcuts import render
from product.models import Product
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from product.models import Product
from product.forms import ProductForm

def home(request):
    
    products = Product.objects.all()
     
    context = {"products":products}
    return render(request,'home.html',context)


    

# @login_required
def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product =  form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'create_product.html', context)



def delete_product(request,pk):
    
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    
    context = {'product':product}
    return render(request, 'delete_product.html',context)