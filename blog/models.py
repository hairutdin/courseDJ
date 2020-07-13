from django.db import models


class Category(models.Model):
    """Модель категорий"""
    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField("url", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    """Модель тегов"""
    name = models.CharField("Тег", max_length=100)
    slug = models.SlugField("url", max_length=100)


class Post(models.Model):
    """Модель постов"""
    title = models.CharField("Заголовок", max_length=100)
    mini_text = models.TextField("Мини-текст", max_length=100)
    text = models.TextField("Текст", max_length=1000)
    created_date = models.DateTimeField("Дата создания", max_length=100)
    slug = models.SlugField("url", max_length=100)
    

class Comment(models.Model):
    """Модель комментариев"""
    text = models.TextField("Текст", max_length=100)
    created_date = models.DateTimeField("Дата создания", max_length=100)
    moderation = models.BooleanField("Модерация")