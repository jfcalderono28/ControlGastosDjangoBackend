from rest_framework import serializers
from ..models_folder.CountriesHasCurrenciesModel import CountriesHasCurrenciesModel

class CountriesHasCurrenciesSerializer(serializers.ModelSerializer):
    currency_name = serializers.CharField(source='id_currency.name_currency')
    country_name = serializers.CharField(source='id_country.name_country')
  
    class Meta:
        model = CountriesHasCurrenciesModel
        fields = ('id_currency','id_country','currency_name', 'country_name')
        
        