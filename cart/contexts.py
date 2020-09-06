from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from listings.models import Listing

def cart_contents(request):

    cart_items = []
    total = 0
    listing_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        listing = get_object_or_404(Listing, pk=item_id)
        total += quantity * listing.price
        listing_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'listing': listing,
        })
      
    grand_total = total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'listing_count': listing_count,
        'grand_total': grand_total,
    }

    return context