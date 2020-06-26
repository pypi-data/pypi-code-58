from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from djangopost.models import CategoryModel
from django.contrib.contenttypes.models import ContentType
from djangopost.managers import ArticleModelManager
from taggit.managers import TaggableManager


class ArticleModel(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('publish', 'Publish'),
        ('withdraw', 'Withdraw'),
        ('private', 'Private')
    )

    serial         = models.IntegerField(blank=True, null=True)
    cover_image    = models.ImageField(null=True, blank=True, upload_to="uploads")
    title          = models.CharField(max_length=95, unique=True, blank=False, null=False)
    slug           = models.CharField(max_length=95, unique=True, blank=False, null=False)
    category       = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    description    = models.TextField(blank=True, null=True)
    content        = models.TextField()
    author         = models.ForeignKey(User, on_delete=models.CASCADE)
    status         = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    verification   = models.BooleanField(default=False)
    is_promote     = models.BooleanField(default=False)
    is_trend       = models.BooleanField(default=False)
    is_promotional = models.BooleanField(default=False)
    is_opinion     = models.BooleanField(default=False)
    total_views    = models.IntegerField(blank=True, null=True, default=0)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    # overright the save method.
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        no_of_opinion = ArticleModel.objects.opinion().count()
        if no_of_opinion > 3:
            for _ in range(no_of_opinion - 2):
                instance = ArticleModel.objects.opinion().last()
                ArticleModel.objects.filter(pk=instance.pk).update(is_opinion=False)
        elif no_of_opinion == 3:
            instance = ArticleModel.objects.opinion().last()
            ArticleModel.objects.filter(pk=instance.pk).update(is_opinion=False)
        else:
            super(ArticleModel, self).save(*args, **kwargs)

    # call all the model manager.
    objects = ArticleModelManager()
    tags    = TaggableManager(blank=True)

    # str method.
    def __str__(self):
        return self.title

    # get absolute url.
    def get_absolute_url_for_detail_view(self):
        return reverse("djangopost:article_detail_view", kwargs={'article_slug': self.slug})

    def get_absolute_url_for_update_view(self):
        return reverse("djangopost:article_update_view", kwargs={'article_slug': self.slug})

    def get_absolute_url_for_delete_view(self):
        return reverse("djangopost:article_delete_view", kwargs={'article_slug': self.slug})

    def get_absolute_url_for_category_detail_view(self):
        return reverse("djangopost:category_detail_view", kwargs={'category_slug': self.category})

    @property
    def get_for_model(self):
        instance = self
        return ContentType.objects.get_for_model(instance.__class__)

    # class meta.
    class Meta:
        ordering = ['-pk']
        verbose_name = "Djangopost article"
        verbose_name_plural = "Djangopost articles"