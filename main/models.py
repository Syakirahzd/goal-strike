from django.utils import timezone
import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('balls', 'Balls'),
        ('socks', 'Socks'),
        ('gloves', 'Gloves'),
        ('backpacks', 'Backpacks'),
        ('soccer cleats', 'Soccer Cleats'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    product_views = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_product(self):
        self.product_views += 1
        self.save()

### DEMO Tugas 2 ###
# spek: Employee -> name (text under 255), age (bilangan bulat), persona (text sepanjang panjang)
# # lakukan migrasi, buat views.py dengan add_employee -> ngecreate employee baru dengan, httpresponese, hubungin dengan urls

# class Employee(models.Model):
#     name = models.CharField(max_length=255)
#     age = models.IntegerField()
#     persona = models.TextField()

#     def __str__(self):
#         return self.title