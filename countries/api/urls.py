from django.urls import path
from .views import APIListView, subscribe_to_api, get_subscribed_apis, unsubscribe_from_api, get_continents, get_country, get_cities

app_name = 'countries'

# countries/apis endpoints
urlpatterns = [
    path('',APIListView.as_view(), name='api-list'),
    path('subscribed/',get_subscribed_apis, name = 'api-subscribed'),
    path('subscribe/<int:api_id>/',subscribe_to_api, name = 'api-subscribe'),
    path('unsubscribe/<int:api_id>/',unsubscribe_from_api, name = 'api-unsubscribe'),
    
    path('continents/',get_continents, name = 'api-continents'),
    path('country/<int:continent_id>/',get_country, name = 'api-country'),
    path('cities/<int:country_id>/',get_cities, name = 'api-cities'),
]