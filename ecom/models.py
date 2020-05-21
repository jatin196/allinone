from django.db import models
from tinymce.models import HTMLField


# Create your models here.

categories = [
    ('Electronics', 'electronics'),
    ('Clothes', 'clothes'),
    ('Shoes', 'shoes'),

]
class product(models.Model):
    product_name = models.CharField(max_length=65)
    product_price = models.IntegerField()
    product_category = models.CharField(
        max_length=15,
        choices=categories,
        default='elec',
        null=True,
        blank=True
    )
    product_brand = models.CharField(max_length=45)
    product_cover = models.ImageField()
    product_specs = HTMLField('Specs')
