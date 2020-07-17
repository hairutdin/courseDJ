from datetime import datetime

from django.shortcuts import render
from django.views.generic.base import View

from .models import Category, Post




class HomeView(View):
    """Home page"""
    def get(self, request):
        category_list = Category.objects.all()
        post_list = Post.objects.filter(published_date__lte=datetime.now(), published=True)
        return render(request, "blog/post_list.html", {"categories": category_list})


class CategoryView(View):
    """Вывод статей категории"""
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        return render(request, "blog/post_list.html", {"category": category})


class PostDetailView(View):
    """Вывод полной статьи"""
    def get(self, request, category, slug):
        category_list = Category.objects.all()
        post = Post.objects.get(slug=slug)
        return render(request, "blog/detail.html", {"categories": category_list, "post": post})
