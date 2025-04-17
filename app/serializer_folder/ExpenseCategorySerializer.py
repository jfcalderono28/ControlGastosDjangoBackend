from ..serializer_folder import serializers
from ..models_folder import ExpenseCategoryModel

class ExpenseCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExpenseCategoryModel
        fields = ('id_user','name_category')