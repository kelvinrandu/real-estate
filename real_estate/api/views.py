from django.shortcuts import render, redirect
from .models import Property,Unit,Tenant,Vendor,Lease,Payment,Expense
from .forms import PropertyForm
from django.contrib import messages

# Create your views here.

def index(request):

    return render(request, 'index.html')

def home(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_property = Property.objects.all
            messages.success(request, ('property has been added succesfully'))
            return render(request, 'home.html', {'all_property': all_property})

    else:
        all_property = Property.objects.all
        return render(request, 'home.html', {'all_property': all_property})


  