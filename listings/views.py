from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Listing, Category

# Create your views here.

def all_listings(request):

    listings = Listing.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                listings = listings.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category_name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            listings = listings.order_by(sortkey)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            listings = listings.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.erro(request, "No search words were entered")
                return redirect(reverse('listings'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            listings = listings.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'listings': listings,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    
    return render(request, 'listings/listings.html')

def listing_detail(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
    }
    
    return render(request, 'listings/listing_detail.html', context)