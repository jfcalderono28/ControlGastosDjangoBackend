from rest_framework import serializers
from ..models_folder.CurrencyModel import CurrencyModel

class CurrencySerializer(serializers.ModelSerializer):


    class Meta:
        model = CurrencyModel
        fields = ['name_currency']