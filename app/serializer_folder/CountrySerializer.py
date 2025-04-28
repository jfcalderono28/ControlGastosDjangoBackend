from rest_framework import serializers
from ..models_folder.CountryModel import CountryModel

class CountrySerializer(serializers.ModelSerializer):


    class Meta:
        model = CountryModel
        fields = ['name_country', 'name_currency']
        extra_kwargs = {
            'name_currency': {'many': True}
        }