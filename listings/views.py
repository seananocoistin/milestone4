from django.shortcuts import render, get_object_or_404
from .models import Listing

# Create your views here.

def all_listings(request):

    listings = Listing.objects.all()

    context = {
        'listings': listings,
    }
    
    return render(request, 'listings/listings.html')

def listing_detail(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
    }
    
    return render(request, 'listings/listing_detail.html', context)