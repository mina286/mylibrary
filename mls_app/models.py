from unicodedata import category
from django.db import models
from django.forms import ImageField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    class Meta:
        ordering=['id']

class Book(models.Model):
    status_book=[
        ('availble','availble'),
        ('rental','rental'),
        ('sold','sold'),

    ]
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True,blank=True)
    author = models.CharField(max_length=200,null=True,blank=True)
    
    title = models.CharField(max_length=200)

    price = models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)

    pages = models.IntegerField(null=True,blank=True)
    retal_period=models.IntegerField(null=True,blank=True)

    photo_book = models.ImageField(upload_to='photos/%Y/%m/%d/',null=True,blank=True,default='def/1.jpg')
    photo_author = models.ImageField(upload_to='photos/%Y/%m/%d/',null=True,blank=True,default='def/2.png')

    retal_price_day =models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    totol_renatl =models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)

    status = models.CharField(max_length=200,choices=status_book,null=True,blank=True)

    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title