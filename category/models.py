from django.db import models
from django.urls import reverse
from accounts.models import Account
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

    
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique = True )
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length =255, blank=True)
    category_image = models.ImageField(upload_to = 'photos/categories/',blank=True)
     
    class Meta:
        verbose_name = 'category'
        verbose_name_plural =  'categories'

    def get_url(self):
        return reverse('products_by_category',args=[self.slug])


    def __str__(self):
        return self.category_name
    
class Category_Offer(models.Model):
    category = models.OneToOneField(Category,on_delete=models.CASCADE)
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    active = models.BooleanField( default=True)
    def __str__(self):
            return self.category.category_name

class banner(models.Model):
    banner_name = models.CharField(max_length=50, unique = True,null=True )
    banner_title = models.CharField(max_length=50, unique = True,null=True )
    banner_description = models.CharField(max_length=50, unique = True,null=True )
    banner_image =models.ImageField( upload_to='photos/banner', height_field=None, width_field=None, max_length=None,blank=True)
    
    is_selected = models.BooleanField(default=False)
    
class banneractive(models.Model):
    banner_name = models.CharField(max_length=50, unique = True,null=True )
    banner_title = models.CharField(max_length=50, unique = True,null=True )
    banner_description = models.CharField(max_length=50, unique = True,null=True )
    banner_image =models.ImageField( upload_to='photos/banner', height_field=None, width_field=None, max_length=None,blank=True)
    
    is_selected = models.BooleanField(default=False)
    
    

    