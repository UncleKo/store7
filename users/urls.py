from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [

    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit-profile/', edit_profile, name='edit-profile'),

    path('fav-items/', FavItemsListView.as_view(), name='fav-items'),
    path('order-history', order_history,
         name='order-history'),

    path('shipping-address/create/',
         ShippingAddressCreateView.as_view(), name='create-shipping-address'),
    path('shipping-address/<int:pk>/update',
         ShippingAddressUpdateView.as_view(), name='update-shipping-address'),
    path('shipping-address/<int:pk>/delete',
         ShippingAddressDeleteView.as_view(), name='delete-shipping-address'),
    path('primary-shipping-address/', PrimaryShippingAddress.as_view(),
         name='primary-shipping-address'),

    path('billing-address/create/',
         BillingAddressCreateView.as_view(), name='create-billing-address'),
    path('billing-address/<int:pk>/update',
         BillingAddressUpdateView.as_view(), name='update-billing-address'),
    path('billing-address/<int:pk>/delete',
         BillingAddressDeleteView.as_view(), name='delete-billing-address'),
    path('primary-billing-address/', PrimaryBillingAddress.as_view(),
         name='primary-billing-address'),

]
