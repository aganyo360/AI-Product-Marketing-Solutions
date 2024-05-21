
from django.shortcuts import render, redirect
from .forms import BusinessForm
from .models import Business

def add_business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('business_list')
    else:
        form = BusinessForm()
    return render(request, 'businesses/add_business.html', {'form': form})

def business_list(request):
    businesses = Business.objects.all()
    return render(request, 'businesses/business_list.html', {'businesses': businesses})

def business_detail(request, pk):
    business = Business.objects.get(pk=pk)
    return render(request, 'businesses/business_detail.html', {'business': business})
