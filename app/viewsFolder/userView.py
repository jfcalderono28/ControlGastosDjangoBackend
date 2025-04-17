# viewsFolder/userView.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


# Serializers
from ..serializer_folder.UserSerializer import UserSerializer

# Models
from ..models_folder.UserModel import UserModel
from ..models_folder.CountryModel import CountryModel
from ..models_folder.UserHasCountriesModel import UserHasCountriesModel

# Crear usuario
@api_view(['POST'])
def RegisterUserView(request):  
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Usuario creado exitosamente"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def InfoUserView(request):
    user = request.user

    user_data = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone": user.phone,
        "photo": user.photo,
        "status_id": user.id_status,
        "is_superuser": user.is_superuser,
        "is_staff": user.is_staff,
    }

    return Response(user_data, status=status.HTTP_200_OK)
from django.db.models import Q

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def SearchUserView(request):
    query = request.query_params.get("query", None)  # Use query_params for GET requests
    print(query)

    if not query:
        return Response({"error": "Se requiere un parámetro de búsqueda (query)"}, status=status.HTTP_400_BAD_REQUEST)

    users = UserModel.objects.filter(
        Q(email__icontains=query) |
        Q(name__icontains=query) |
        Q(id__iexact=query)
    )

    if not users.exists():
        return Response({"error": "No se encontraron usuarios"}, status=status.HTTP_404_NOT_FOUND)

    user_data = [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
            "photo": user.photo,
            "status_id": user.id_status,
            "is_superuser": user.is_superuser,
            "is_staff": user.is_staff,
        }
        for user in users
    ]

    return Response(user_data, status=status.HTTP_200_OK)

# Actualizar usuario
@api_view(['PUT', 'PATCH'])
def UpdateUserView(request, user_id):  
    try:
        user = UserModel.objects.get(id=user_id)
    except UserModel.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, data=request.data, partial=True)  # actualiza parcialmente
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Usuario actualizado correctamente"}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Agregar países a usuario
@api_view(['POST'])
def AddCountriesToUserView(request, user_id):
    try:
        user = UserModel.objects.get(id=user_id)
    except UserModel.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    country_ids = request.data.get("country_ids", [])
    if not isinstance(country_ids, list) or not country_ids:
        return Response({"error": "Se requiere una lista de IDs de países"}, status=status.HTTP_400_BAD_REQUEST)

    added_countries = []
    for country_id in country_ids:
        try:
            country = CountryModel.objects.get(id=country_id)
            # Evita duplicados
            relation, created = UserHasCountriesModel.objects.get_or_create(id_user=user, id_country=country)
            if created:
                added_countries.append(country.name_country)
        except CountryModel.DoesNotExist:
            continue

    return Response({
        "message": "Países agregados correctamente",
        "paises_agregados": added_countries
    }, status=status.HTTP_200_OK)


