from django.shortcuts import render, get_object_or_404
from . models import Post, Category

# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts': posts})

def category(request, category_id):
    #category = Category.objects.get(id=category_id) con get encontramos 
    category = get_object_or_404(Category, id=category_id) # CONTROLANDO ERRORES CON 404
    #posts = Post.objects.filter(categories=category) #--Buscar en el template de manera inversa
    return render(request, "blog/category.html", {'category': category})