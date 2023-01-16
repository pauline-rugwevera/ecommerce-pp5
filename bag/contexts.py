from django.conf import settings
from decimal import Decimal

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0


    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
     
    
    grand_total = total



    context = {
        
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }
    return context