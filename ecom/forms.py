from django import forms
from .models import product


class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['product_name', 'product_price', 'product_category', 'product_brand', 'product_cover', 'product_specs']