from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    """Модель категорий"""
    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField("url", max_length=100)
    description = models.TextField("Описание", max_length=1000, default="", blank=True)
    parent = TreeForeignKey(
        'self',
        verbose_name='Родительская категория',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    template = models.CharField("Шаблон", max_length=500, default="news/post_list.html")
    published = models.BooleanField("Отоброжать?", default=True)
    paginated = models.PositiveIntegerField("Количество новостей на странице", default=5)
    sort = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    

class Tag(models.Model):
    """Модель тегов"""
    name = models.CharField("Тег", max_length=50, unique=True)
    slug = models.SlugField("url", max_length=100, unique=True)
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = "Теги"
    
    def __str__(self):
        return self.name


class Post(models.Model):
    """Класс модели поста"""
    author = models.ForeignKey(
        User,
        verbose_name="",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField("Заголовок", max_length=500)
    slug = models.SlugField("url", max_length=100, unique=True)
    subtitle = models.CharField("Подзаголовок", max_length=500, blank=True, null=True)
    mini_text = models.TextField("Краткое содержание", max_length=5000)
    text = models.TextField("Полное содержание", max_length=10000000)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        default=timezone.now,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
            "Дата публикации",
            default=timezone.now,
            blank=True,
            null=True
    )
    image = models.ImageField("Главная фотография", upload_to="post/", null=True, blank=True)
    tags = models.ManyToManyField(Tag, verbose_name="Тег", blank=True)
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.CASCADE,
        null=True
    )
    template = models.CharField("Шаблон", max_length=500, default="news/post_detail.html")
    
    published = models.BooleanField("Опубликовать?", default=True)
    viewed = models.PositiveIntegerField("Просмотрено", default=0)
    status = models.BooleanField("Для зарегистрированных", default=True)
    sort = models.PositiveIntegerField("Порядок", default=0)
     
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = "Новости"
        ordering = ["sort", "-published_date"]
    
    def get_absolute_url(self):
        return reverse("detail_post", kwargs={"category": self.category.slug, "post": self.slug})
    
    def __str__(self):
        return "{}".format(self.title)


class Comment(models.Model):
    """Модель комментариев"""
    author = models.ForeignKey(
        User,
        verbose_name="",
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(Post, verbose_name="Статья", on_delete=models.CASCADE)
    text = models.TextField("Кoмментарий")
    create_date = models.DateTimeField("Дата создания", auto_now=True)
    moderation = models.BooleanField(default=True)
    

    class Meta:
        verbose_name ='Комментарий'
        verbose_name_plural = "Комментарии"
