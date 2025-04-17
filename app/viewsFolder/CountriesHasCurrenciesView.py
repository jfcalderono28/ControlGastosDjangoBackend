# viewsFolder/userView.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from ..models_folder.CountriesHasCurrenciesModel import CountriesHasCurrenciesModel
from ..models_folder.CountryModel import CountryModel
from ..models_folder.CurrencyModel import CurrencyModel


from ..serializer_folder.CountriesHasCurrenciesSerializer import CountriesHasCurrenciesSerializer

from django.http.response import JsonResponse
 

@api_view(['POST'])
def AddCurrenciesToCountryView(request, country_id):
    try:
        country = CountryModel.objects.get(id=country_id)
    except CountryModel.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    currencies_ids = request.data.get("currencies_ids", [])
    if not isinstance(currencies_ids, list) or not currencies_ids:
        return Response({"error": "Se requiere una lista de IDs de países"}, status=status.HTTP_400_BAD_REQUEST)

    added_currencies = []
    for currency_id in currencies_ids:
        try:
            currency = CurrencyModel.objects.get(id=currency_id)
            # Evitar duplicados correctamente
            relation, created = CountriesHasCurrenciesModel.objects.get_or_create(id_country=country, id_currency=currency)
            if created:
                added_currencies.append(country.name_country)
        except CountryModel.DoesNotExist:
            continue

    return Response({
        "message": "Países agregados correctamente",
        "paises_agregados": added_currencies
    }, status=status.HTTP_200_OK)
    
    
@api_view(["GET"])
def getCurrenciesOfCountry(request, country_id):
    name_country = CountryModel.objects.filter(id = country_id).values_list('name_country',flat=True)
    currencies = CountriesHasCurrenciesModel.objects.filter(id_country = country_id)
    
    print(currencies)
            
    if not currencies.exists():
        return Response(
            {"success": False, "message": "No hay resultados para su petición"},
            status=status.HTTP_200_OK,
        )

    contentSerialized = CountriesHasCurrenciesSerializer(currencies, many=True)

    return Response(
        {"success": True, "message": "","country":name_country, "currencies": contentSerialized.data},
        status=status.HTTP_200_OK,
    )