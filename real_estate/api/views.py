from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Property, Unit, Tenant, Vendor, Lease, Payment, Expense
from .forms import PropertyForm, TenantForm 
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('property has been added succesfully'))
            return render(request=request, 
                          template_name='index.html',
                          context={"all_property": Property.objects.all})

    else:
        all_property = Property.objects.all
        return render(request=request, 
                      template_name='index.html',
                      context={"all_property": Property.objects.all})




def unit(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('property has been added succesfully'))
            return render(request=request, 
                          template_name='unit.html',
                          context={"all_property": Property.objects.all})

    else:
        all_property = Property.objects.all
        return render(request=request, 
                      template_name='index.html',
                      context={"all_property": Property.objects.all})


def tenant(request):
    if request.method == 'POST':
        form = TenantForm(request.POST or None)

        if form.is_valid():
            form.save()
            form = TenantForm(request.POST or None)
            messages.success(request, ('property has been added succesfully'))
            return render(request=request, 
                          template_name='tenant.html',
                          context={"all_tenant": Tenant.objects.all})

    else:
        all_property = Property.objects.all
        return render(request=request, 
                      template_name='tenant.html',
                      context={"all_tenant": Tenant.objects.all})


def vendor(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('property has been added succesfully'))
            return render(request=request, 
                          template_name='index.html',
                          context={"all_property": Property.objects.all})

    else:
        all_property = Property.objects.all
        return render(request=request, 
                      template_name='index.html',
                      context={"all_property": Property.objects.all})


def lease(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('property has been added succesfully'))
            return render(request=request, 
                          template_name='index.html',
                          context={"all_property": Property.objects.all})

    else:
        all_property = Property.objects.all
        return render(request=request, 
                      template_name='index.html',
                      context={"all_property": Property.objects.all}) 


def payment(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('property has been added succesfully'))
            return render(request=request, 
                          template_name='index.html',
                          context={"all_property": Property.objects.all})

    else:
        all_property = Property.objects.all
        return render(request=request, 
                      template_name='index.html',
                      context={"all_property": Property.objects.all})


def expense(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('property has been added succesfully'))
            return render(request=request, 
                          template_name='index.html',
                          context={"all_property": Property.objects.all})

    else:
        all_property = Property.objects.all
        return render(request=request, 
                      template_name='index.html',
                      context={"all_property": Property.objects.all})