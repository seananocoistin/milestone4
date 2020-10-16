from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_listings, name='listings'),
    path('<int:listing_id>/', views.listing_detail, name='listing_detail'),
    path('add/', views.add_listing, name='add_listing'),
    path('edit/<int:listing_id>/', views.edit_listing, name='edit_listing'),
    path('delete/<int:listing_id>/', views.delete_listing, name='delete_listing'),
    path('create-session', views.create_session),
    path('payment/<int:listing_id>', views.listing_payment, name='listing_payment')
]