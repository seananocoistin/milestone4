from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Listing

# Create your views here.

def all_listings(request):

    listings = Listing.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.erro(request, "No search words were entered")
                return redirect(reverse('listings'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            listings = listings.filter(queries)

    context = {
        'listings': listings,
        'search_term': query,
    }
    
    return render(request, 'listings/listings.html')

def listing_detail(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
    }
    
    return render(request, 'listings/listing_detail.html', context)