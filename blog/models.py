from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from froala_editor.fields import FroalaField
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    cslug=models.SlugField(max_length=50,unique=True)
    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    title=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/',default='featured_image/default.jpg')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="posts")
    body=FroalaField()
    views=models.IntegerField(default=0)
    publish = models.DateTimeField(default=timezone.now)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    tags=TaggableManager()
    class meta:
        ordering = ('-created_at',)
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.slug])
    def __str__(self):
            return self.title
class Comment(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    class meta:
         ordering =('-created')
    def __str__(self):
        return self.email+self.comment
class Contact(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    message=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email+self.message
    class meta:
         ordering =('-created')