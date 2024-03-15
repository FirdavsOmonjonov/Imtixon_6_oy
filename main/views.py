from django.shortcuts import render
from django.db import models
from . import models

def index(request):
    """Index-Asosiy saxifa"""
    about= models.About.objects.last()
    services = models.Service.objects.all()
    blogs = models.Blog.objects.all()


    context = {
        'about':about,
        'services':services,
        'blogs':blogs,
    }
    return render(request, 'index.html', context)


def about(request):
    """About-Korxona haqida ma'lumot"""
    abouts= models.About.objects.all()
    context = {
        'abouts':abouts,
    }
    return render(request, 'about.html', context)

def service(request):
    """Service-xizmat ko'rsatish"""
    services = models.Service.objects.all()
    context = {
      'services':services,
    }
    return render(request, 'service.html', context)
    

def blog(request):
    """Blog-foydalanuvchilarni fikrlari"""
    blogs = models.Blog.objects.all()
    context = {
      'blogs':blogs,
    }
    return render(request, 'blog.html', context)


def contact(request):
    """Contact-xabar qoldirish uchun"""
    if request.method == 'POST':
        try:
            models.Contact.objects.create(
                name=request.POST['name'],
                phone=request.POST['phone'],
                email=request.POST['email'],
                body=request.POST['message']
            )
        except:
            ...
    return render(request, 'contact.html')

