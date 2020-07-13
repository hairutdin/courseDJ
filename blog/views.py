from django.shortcuts import render
from django.views.generic.base import View

from .models import Category, Post



class HomeView(View):
    """Home page"""
    def get(self, request):
        category_list = Category.objects.all()
        return render(request, "blog/home.html", {"categories": category_list})

    def get_post(self, request):
        list_of_posts = Post.objects.all()
        return  render(request, "blog/home.html", {"posts": list_of_posts})

class CategoryView(View):
    """Вывод статей категории"""
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        return render(request, "blog/post_list.html", {"category": category})

    def get_post(self, request):
        post = Post.objects.get(slug=slug)
        return render(request, "blog/post_list.html", {"post": post})
