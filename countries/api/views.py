# This method is used to return back the HTTP response status of a request
from rest_framework import status
# The method used to retunr back a response to the caller
from rest_framework.response import Response
# api_view: Python decorator used to restrict a method's access only via POST request
# permission_classes: Python decorator used to set the permisions required to access a view mwethod
from rest_framework.decorators import api_view, permission_classes
# The class used to force a user to first authenticate by passing their token before getting access to the view's data
from rest_framework.permissions import IsAuthenticated
# The class that states the type of authentication expected
from rest_framework.authentication import TokenAuthentication
# A class used to return a list of python data objects
from rest_framework.generics import ListAPIView

from countries.models import (Continent, Country, Cities, API, Subscription)
# The serializers created to transform their related database python objects to JSON objects
from .serializers import (ContinentSerializer, CountrySerializer, CitiesSerializer, APISerializer, SubscriptionSerializer)

# This class wil return the list of APIs supported by the system
class APIListView(ListAPIView):
    queryset = API.objects.all()
    serializer_class = APISerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

# This view method can only be accessed via a GET request
@api_view(['GET'])
# A user is required to authenticate, by passing their token with the header
@permission_classes((IsAuthenticated,))
# This view is used by a user to subscribe to a particular A.P.I. for access
def subscribe_to_api(request, api_id):
    # Try getting the specific API a user wants to subscribe to, if the API record does not exist, send back a HTTP 404 error
    try:
        api = API.objects.get(pk=api_id)
    except API.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Pass the user and the requested API to the subscription model for subscription
    # If a user already subscribed or a new subscription has been made inform the user appropriately
    operation = Subscription.objects.get_or_create(api=api,user=request.user)
    data = {}
    if operation:
        data['message'] = 'subscription successful'
    else:
        data['message'] = 'subscription failed'
    return Response(data=data)

# This view method can only be accessed via a GET request
@api_view(['GET'])
# A user is required to authenticate, by passing their token with the header
@permission_classes((IsAuthenticated,))
# This view is used by a user to get APIs subscribed to
def get_subscribed_apis(request):
    try:
        # Try getting all subscriptions related to the user, if the subscription data does not exist, return a HTTP 404 error
        subscriptions = Subscription.objects.filter(user=request.user)
    except Subscription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Else if the data exists, pass the python database objects to it is serializer for convertion to JSON objects
    serialise = SubscriptionSerializer(subscriptions)
    # invoke the response class to return the JSON subscription objects
    return Response(serialise.data)

# This view method can only be accessed via a DELETE request
@api_view(['DELETE'])
# A user is required to authenticate, by passing their token with the header
@permission_classes((IsAuthenticated,))
# This view is used by a user to unsubscribe from an API, it expects the API id as a parameter
def unsubscribe_from_api(request, api_id):
    try:        
        # Using the API id passed and the authenticated user try getting the subscribed API from the subscription table 
        # If the subscription data does not exist, return a HTTP 404 error

        subscription = Subscription.objects.get(api_id=api_id, user=request.user)
    except Subscription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # if the subscription exists, delete it and inform the user appropriately
    operation = subscription.delete()
    data = {}
    if operation:
        data['success'] = 'unsubscribed successfully'
    else:
        data['failure'] = 'failed to unsubscribe'
    return Response(data=data)

# This view method can only be accessed via a GET request
@api_view(['GET'])
# A user is required to authenticate, by passing their token with the header
@permission_classes((IsAuthenticated,))
# This view is used by a user to access the continents API data
def get_continents(request):
    try:
        # We first try to confirm if the authenticated user has subscribed to use this A.P.I. if not send back a HTTP 404 error
        Subscription.objects.get(user=request.user, api_id=2)
                # Subscription.objects.get(user=request.user,api_id=2)

    except Subscription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        # If the user is authorised to access the continents API, get all continents.
        # If the continent data does not exist, return a HTTP 404 error
        continents = Continent.objects.all()
    except Continent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    # Else if the continent data exists, pass the python database objects to it is serializer for conversion to JSON objects
    serialise = ContinentSerializer(continents)    
    # invoke the response class to return the JSON continents objects
    return Response(serialise.data)


# This view method can only be accessed via a GET request
@api_view(['GET'])
# A user is required to authenticate, by passing their token with the header
@permission_classes((IsAuthenticated,))
# This view is used by a user to access the country's API data, it expects the continent id as a parameter
def get_country(request,continent_id):
    try:
        # We first try to confirm if the authenticated user has subscribed to use this A.P.I. if not send back a HTTP 404 error
        Subscription.objects.get(user=request.user,api_id=1)
    except Subscription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        # using the continent id, we will get the specific continent
        # If the continent does not exist, return a HTTP 404 error
        continent = Continent.objects.get(pk=continent_id)
    except Continent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        # using the returned continent, we will get the specific countries related to the continent
        # If the countries do not exist, return a HTTP 404 error
        countries = Country.objects.filter(continent=continent)
    except Country.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Else if the countries data exists, pass the python database objects to it is serializer for convertion to JSON objects
    serialise = CountrySerializer(countries)
    # invoke the response class to return the JSON countries objects
    return Response(serialise.data)


# This view method can only be accessed via a GET request
@api_view(['GET'])
# A user is required to authenticate, by passing their token with the header
@permission_classes((IsAuthenticated,))
# This view is used by a user to access the cities's API data, it expects the country id as a parameter
def get_cities(request,country_id):
    try:
        # We first try to confirm if the authenticated user has subscribed to use this A.P.I. if not send back a HTTP 404 error
        Subscription.objects.get(user=request.user,api_id=3)
    except Subscription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        # using the country id, we will get the specific country
        # If the country does not exist, return a HTTP 404 error
        country = Country.objects.get(pk=country_id)
    except Country.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        # using the returned country, we will get the specific cities related to the country
        # If the country do not exist, return a HTTP 404 error
        city = Cities.objects.filter(country=country)
    except Cities.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Else if the cities data exists, pass the python database objects to it is serializer for convertion to JSON objects
    serialise = CitiesSerializer(city)
    # invoke the response class to return the JSON cities objects
    return Response(serialise.data)