from django.shortcuts import render,redirect,get_object_or_404
from .cart import Cart
from cart.forms import CartAddProductForm
from shop.models import Product
from django.views.decorators.http import require_POST
# Create your views here.

@require_POST
def cart_add(request , product_id):
    print('########################')
    cart=Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form =CartAddProductForm(request.POST)
    if form.is_valid():
        cd =form.cleaned_data
        quantity =cd['quantity']
        update=cd['update']
        cart.add(product = product, quantity = quantity ,update_quantity = update)  
    return redirect('cart:cart_detail')


def cart_remove(request,product_id):
    cart = Cart(request)
    product =get_object_or_404(Product, id =product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart=Cart(request)
    print('!!!!!!!!' , len(cart))
    #form =CartAddProductForm()
    return render(request ,'cart/detail.html' ,{'cart':cart} )
