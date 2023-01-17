from django.shortcuts import render, redirect,  HttpResponse
from django.contrib import messages
from products.models import Product

def view_bag(request):
    """ A view to show bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {Product.name}'
                         f' quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
    request.session['bag'] = bag
    return redirect(redirect_url)

    # cart
    
def adjust_basket(request, item_id):
    """ Adjust the quantity of the specific product in the basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f'Updated {product.name}'
                         f' quantity to {bag[item_id]}')
    else:
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_basket(request, item_id):
    """ Remove item from the bag """

    product = get_object_or_404(Product, pk=item_id)

    try:

        basket = request.session.get('bag', {})
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from basket')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

