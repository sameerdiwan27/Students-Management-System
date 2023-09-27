from django.shortcuts import render, redirect
from .models import Model


# Create your views here.
def index(request):
    data = Model.objects.all()
    users = {'data': data}
    return render(request, 'index.html', users)


def edit(request):
    data = Model.objects.all()
    users = {'data': data}
    return render(request, 'index.html', users)


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone   = request.POST.get('phone')
        data = Model(
            name=name,
            email=email,
            phone=phone

        )
        data.save()
        return redirect('index')


def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        data = Model(
            id=id,
            name=name,
            email=email,
            phone=phone
        )
        data.save()
        return redirect('index')


def delete(request, id):
    data = Model.objects.filter(id=id)
    data.delete()
    return redirect('index')
