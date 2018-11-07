from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import pre_save, post_save

from tags.models import Tag
from rejuvahome.utils import unique_slug_generator

BLOG_STATUS_CHOICES = (('draft','Draft'),
    ('published','Published'),)

User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True,db_index=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blogs:category_detail', None, kwargs={'slug': self.slug,})

def category_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(category_pre_save_reciever, sender=Category)

class BlogQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(status='published', featured=True, active=True)

    def published(self):
        return self.filter(status="published", active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) | Q(content__icontains=query) | Q(author__icontains=query) | Q(tag__title__icontains=query) | Q(category__icontains=query))        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.filter(lookups).distinct()

class BlogManager(models.Manager):
    def get_queryset(self):
        return BlogQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self): #Custom Query Set
        return self.get_queryset().featured()

    def published(self): #Custom Query Set
        return self.get_queryset().published()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Blog.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)

class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blogs/%Y/%m/%d', blank=True, null=True)
    featured = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    status = models.CharField(max_length=120, default='draft', choices = BLOG_STATUS_CHOICES)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    slug = models.SlugField(blank=True, unique=True, db_index=True)
    tags = models.ManyToManyField(Tag, blank=True)

    objects = BlogManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return "/Blogs/{slug}/".format(slug=self.slug)
        return reverse("blogs:detail", kwargs={'slug': self.slug})

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

def blog_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(blog_pre_save_reciever, sender=Blog)
