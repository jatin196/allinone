from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic
from .models import product, OrderItem, Order
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


class ProductList(generic.ListView):
    model = product
    paginate_by = 3
    template_name = 'ecommerce/list.html'
    context_object_name = 'products'


class ProductDetail(generic.DetailView):
    model = product
    template_name = 'ecommerce/detail.html'
    context_object_name = 'product'


def ProductCreate(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('ecom:list'))

    context = {
        'form' : form
    }
    return render(request, 'ecommerce/ProductForm.html', context)

def ProductUpdate(request, pk):
    pdt = get_object_or_404(product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=pdt)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('ecom:detail', kwargs={
            'pk':pk
            }))
    context = {
        'form' : form
    }
    return render(request, 'ecommerce/ProductForm.html', context)


@login_required()
def AddToCart(request, pk):
    item = get_object_or_404(product, pk=pk)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user = request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk):
            order_item.qty += 1
            order_item.save()
            return redirect('ecom:cart')

        else:
            order.items.add(order_item)
            return redirect('ecom:cart')
    else:
        order = Order.objects.create(
            user=request.user,
            ordered_date=timezone.now()
        )
        order.items.add(order_item)
        return redirect('ecom:cart')

@login_required()
def Cart(request):
    order = Order.objects.filter(user=request.user, ordered=False)
    print(order[0].items.all())
    context = {
        'object':order[0]
    }
    return render(request, 'ecommerce/summary.html', context)
