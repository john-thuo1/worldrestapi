from countries.models import Continent, Country, Cities, API, Subscription
# The built in Django serializers method is used to convert python databases objects(Complex data) to JSON objects
from rest_framework import serializers

class ContinentSerializer(serializers.ModelSerializer):
     # The JSON object to returned will be labeled values, that will get its data from a class method called get_continent_values
    values = serializers.SerializerMethodField('get_continent_values')
    
    class Meta:
        model = Continent
        fields = ['values']
    
    def get_continent_values(self, continent):
        # Why did we use continent variable instead of Continent?
        return continent.values('id','name')

class CountrySerializer(serializers.ModelSerializer):
    values = serializers.SerializerMethodField('get_country_values')

    class Meta:
        model = Country
        fields = ['values']
    # This method is responsible for returning the country id, country name and country code
    def get_country_values(self, country):
        return country.values('id','name', 'code')



class CitiesSerializer(serializers.ModelSerializer):
    values = serializers.SerializerMethodField('get_country_values')

    class Meta:
        model = Cities
        fields = ['values']
    # This method is responsible for returning the cities name
    def get_cities_values(self, cities):
        return cities.values('name')


class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = API
        # Why are we getting API id?
        fields = ['id','name','code']
    

class SubscriptionSerializer(serializers.ModelSerializer):
    values = serializers.SerializerMethodField('get_subscription_values')
    class Meta:
        model = Subscription
        fields=['values']
    
    # This method is responsible for returning the subscribed A.P.I. id and A.P.I. name
    def get_subscription_values(self, subscription):
        return subscription.values('api__id','api__name')