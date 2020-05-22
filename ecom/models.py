from django.db import models
from django.conf import settings
from tinymce.models import HTMLField


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

    def __str__(self):
        return "{name} by {brand}".format(name=self.product_name, brand=self.product_brand)


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return "{qty} of {item} by {user}".format(qty=self.qty, item=self.item.product_name, user=self.user.username)
    def get_items_price(self):
        return self.item.product_price*self.qty


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)


    def __str__(self):
        return "order by {user}".format( user=self.user.username)

    def get_all_items(self):
        return self.item
    def total_price(self):
        c=0
        for i in self.items.all():
            c += i.get_items_price()
        return c
