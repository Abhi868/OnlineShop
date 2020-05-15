from django.db import models
from django.urls import reverse
# Create your models here.
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name=models.CharField(max_length = 200 ,help_text=_('name'), db_index=True)
    slug=models.SlugField(max_length=200, unique =True , help_text=_('slug'))

    class Meta:
        ordering=('name',)
        verbose_name =_('category')
        verbose_name_plural=_('categories')


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('shop:product_list_by_category' ,args=[self.slug])

class Product(models.Model):
    category=models.ForeignKey(Category, related_name='products', help_text=_('category'),on_delete =models.CASCADE)
    name =models.CharField(max_length=200, db_index=True , help_text=_('name'))
    slug = models.SlugField(max_length=200, db_index=True , help_text=_('slug'))
    description=models.TextField(blank=True , help_text=_('description'))
    price = models.DecimalField(max_digits =10, decimal_places =2 , help_text=_('price'))
    available= models.BooleanField(default=True , help_text=_('available'))
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now =True)
    image =models.ImageField(upload_to = 'products/%Y/%m/%d' , blank=True)

    class Meta:
        ordering=('name',)
        index_together=(('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
