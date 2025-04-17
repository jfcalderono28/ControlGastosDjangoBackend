from ..serializer_folder import serializers
from ..models_folder import UserHasPoketModel

class UserHasPoketSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = UserHasPoketModel
        fields = ('name')