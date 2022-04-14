from dataclasses import fields
from django.contrib import admin
from mls_app.models import Book
from mls_app.models import Category

# Register your models here.
class adminbook(admin.ModelAdmin):
    list_display=['title','price','photo_book','status','category']
    search_fields=['title']
    list_filter=['price']
  
admin.site.register(Book,adminbook)
admin.site.register(Category)
