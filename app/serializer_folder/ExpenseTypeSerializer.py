from ..serializer_folder import serializers
from ..models_folder import ExpenseTypeModel

class ExpenseTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExpenseTypeModel
        fields = ('id_user','name_type')