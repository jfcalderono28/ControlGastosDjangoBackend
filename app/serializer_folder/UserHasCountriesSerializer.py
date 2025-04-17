from ..serializer_folder import serializers
from ..models_folder import UserHasCountriesModel

class UserHasCountriesSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = UserHasCountriesModel
        fields = ('id_user','id_country')