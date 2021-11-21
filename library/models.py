from django.db import models

# Create your models here.
class Book(models.Model):
    
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=32, null=True, blank=True)
    num_pages = models.IntegerField(default=0)
    date = models.DateField(blank=True, null=True)
    price = models.DecimalField(blank=True, null=True, default=0, decimal_places=2, max_digits = 8)
    isbn13 = models.CharField(max_length=13, blank=True, null=True)


    def __str__(self):
        return self.title
