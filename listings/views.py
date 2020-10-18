from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Listing, Category
from .forms import ListingForm

from .models import Listing
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

import stripe
import json

stripe.api_key = 'sk_test_R96LxBUcGDCLB4bxMLOPN6u900vzU7ySpx'

def all_listings(request):
    """ A view to show all listings, including sorting and search queries """

    listings = Listing.objects.filter(paid=True).all()
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
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            listings = listings.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            listings = listings.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('listings'))
            
            queries = Q(name__icontains=query) | Q(about__icontains=query)
            listings = listings.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'listings': listings,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'listings/listings.html', context)

def listing_detail(request, listing_id):
    """ A view to show individual listing details """

    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
    }

    return render(request, 'listings/listing_detail.html', context)

from django.conf import settings # new
from django.shortcuts import render

def add_listing(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()
            messages.success(request, 'Successfully added listing!')
            return redirect(reverse('listing_payment', args=[listing.id]))
        else:
            messages.error(request, 'Failed to add listing. Please ensure the form is valid.')
    else:
        form = ListingForm()
        
    template = 'listings/add_listing.html'
    context = {
        'form': form,
        'stripe_public_key': 'pk_test_4KgVlDgFauT9Sfs8TtAN5Tjd00qMznyVjp',
        'client_secret': 'sk_test_R96LxBUcGDCLB4bxMLOPN6u900vzU7ySpx',
    }
    return render(request, template, context)


def edit_listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    if request.user.is_authenticated and (request.user.is_staff or listing.owner == request.user):
        if request.method == 'POST':
            form = ListingForm(request.POST, request.FILES, instance=listing)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully updated listing!')
                return redirect(reverse('listing_detail', args=[listing.id]))
            else:
                messages.error(request, 'Failed to update listing. Please ensure the form is valid.')
        else:
            form = ListingForm(instance=listing)
            messages.info(request, f'You are editing {listing.name}')

        template = 'listings/edit_listing.html'
        context = {
            'form': form,
            'listing': listing,
        }

        return render(request, template, context)
    return HttpResponse(status=400)


def delete_listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    if request.user.is_authenticated and (request.user.is_staff or listing.owner == request.user):
        listing.delete()
    messages.success(request, 'Listing deleted!')
    return redirect(reverse('listings'))
    
@csrf_exempt    
def create_session(request):
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'eur',
                        'unit_amount': 5000,
                        'product_data': {
                            'name': 'The Premium Business Directory',
                            'images': ['https://imgur.com/gallery/HHOfop7'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url="https://8000-a2ffc051-50db-4045-aa9f-031a0938f4ce.ws-eu01.gitpod.io/listings/",
            cancel_url="https://8000-a2ffc051-50db-4045-aa9f-031a0938f4ce.ws-eu01.gitpod.io/listings/",
            metadata={"listing_id":json.loads(request.body)["listing_id"]}
        )
        return JsonResponse({'id': checkout_session.id})
    except Exception as e:
        return JsonResponse({"error":str(e)})

def listing_payment(request, listing_id):
    """ A view to show individual listing details """

    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
    }

    return render(request, 'listings/listing_payment.html', context)

@csrf_exempt
def my_webhook_view(request):
  payload = request.body
  event = None

  try:
    event = stripe.Event.construct_from(
      json.loads(payload), stripe.api_key
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)

  # Handle the event
  if event.type == 'checkout.session.completed':
    session = event.data.object
    listing_id = int(session.metadata.listing_id)
    listing = Listing.objects.get(pk=listing_id)
    listing.paid = True
    listing.save()
  return HttpResponse(status=200)