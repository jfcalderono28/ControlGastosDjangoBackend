from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Puedes agregar más claims personalizados si querés
        token['email'] = user.email
        return token

    def validate(self, attrs):
        # Modificamos para aceptar email en vez de username
        attrs['username'] = attrs.get('email')
        return super().validate(attrs)
