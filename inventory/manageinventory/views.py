# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request,'manageinventory/index.html',context)


def detail(request,pk):
    product = get_object_or_404(Product,pk=pk)
    return render(request,'manageinventory/detail.html',{'product':product})

def addnew(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        print(dir(form))
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = ProductForm()
    return render(request,'manageinventory/new.html',{'form':form})

def edit(request,pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form =ProductForm(request.POST, instance = product)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm(instance=product)
    return render(request,'manageinventory/edit.html',{'form':form})

