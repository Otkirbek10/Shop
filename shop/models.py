from django.db import models
# from django.forms import BooleanField, DecimalField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',args=[self.slug])
    

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    name = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(max_length=255,db_index=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'))

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id, self.slug])
