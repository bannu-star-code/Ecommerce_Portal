from django import template

register=template.Library()

@register.filter(name='total_cart')
def total_cart(cart):
    return sum([i for i in cart])
   

@register.filter(name='is_in_cart')
def is_in_cart(product , cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==product.id:
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product , cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==product.id:
            return cart.get(id)
    return 0
    # return cart.get(str(product.id))

@register.filter(name='total_price')
def total_price(product, cart):
    return product.price*cart_quantity(product,cart)

@register.filter(name='total_cart_price')
def total_cart_price(products, cart):
    sum=0
    for p in products:
        sum+=total_price(p, cart)
    return sum

@register.filter(name='currency')
def currency(number):
    return 'Rs ' + str(number)

@register.filter(name='multiply')
def multiply(number, number1):
    return number*number1
