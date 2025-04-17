from ..serializer_folder import serializers
from ..models_folder import UserHasCurrencyModel

class UserHasCurrencySerializer(serializers.ModelSerializer):
  
    class Meta:
        model = UserHasCurrencyModel
        fields = ('id_user','id_currency')