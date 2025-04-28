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
def RegisterCountryView(request):
    country_id = request.data.get("country_id")
    name_country = request.data.get("name_country")
    currencies_ids = request.data.get("currencies_ids", [])

    added_currencies = []

    if not country_id and name_country:
        try:
            country = CountryModel.objects.get(name_country=name_country)
            country_id = country.id
        except CountryModel.DoesNotExist:
            # Crear el país si no existe
            country = CountryModel.objects.create(name_country=name_country)
            country_id = country.id

    elif not country_id and not name_country:
        return Response({"error": "Se requiere un ID de país o un nombre de país"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        country = CountryModel.objects.get(id=country_id)
        # Actualizar el nombre del país si es necesario
        if name_country and country.name_country != name_country:
            country.name_country = name_country
            country.save()
    except CountryModel.DoesNotExist:
        return Response({"error": "País no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if not isinstance(currencies_ids, list) or not currencies_ids:
        return Response({"error": "Se requiere una lista de IDs de monedas"}, status=status.HTTP_400_BAD_REQUEST)

    # Actualizar las monedas asociadas al país
    existing_relations = CountriesHasCurrenciesModel.objects.filter(
        id_country=country)
    existing_relations.delete()  # Eliminar relaciones existentes para actualizar

    for currency_id in currencies_ids:
        try:
            currency = CurrencyModel.objects.get(id=currency_id)
            relation, created = CountriesHasCurrenciesModel.objects.get_or_create(
                id_country=country, id_currency=currency)
            if created:
                added_currencies.append(currency.name_currency)
        except CurrencyModel.DoesNotExist:
            continue

    return Response({
        "message": "País y monedas actualizados correctamente",
        "monedas_agregadas": added_currencies
    }, status=status.HTTP_200_OK)


@api_view(['PUT'])
def UpdateCountryView(request):
    country_id = request.data.get("country_id")
    name_country = request.data.get("name_country")
    currencies_ids = request.data.get("currencies_ids", [])

    # Validación: se requiere un ID de país
    if not country_id:
        return Response({"error": "Se requiere un ID de país"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        country = CountryModel.objects.get(id=country_id)
    except CountryModel.DoesNotExist:
        return Response({"error": "País no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    # Actualizar el nombre del país si se proporciona
    if name_country and country.name_country != name_country:
        country.name_country = name_country
        country.save()

    # Validación: se requiere una lista de IDs de monedas
    if not isinstance(currencies_ids, list) or not currencies_ids:
        return Response({"error": "Se requiere una lista de IDs de monedas"}, status=status.HTTP_400_BAD_REQUEST)

    # Actualizar las monedas asociadas al país
    added_currencies = []
    existing_relations = CountriesHasCurrenciesModel.objects.filter(
        id_country=country)
    existing_relations.delete()  # Eliminar relaciones existentes para actualizar

    for currency_id in currencies_ids:
        try:
            currency = CurrencyModel.objects.get(id=currency_id)
            relation, created = CountriesHasCurrenciesModel.objects.get_or_create(
                id_country=country, id_currency=currency)
            if created:
                added_currencies.append(currency.name_currency)
        except CurrencyModel.DoesNotExist:
            continue

    return Response({
        "message": "País y monedas actualizados correctamente",
        "monedas_agregadas": added_currencies
    }, status=status.HTTP_200_OK)


@api_view(["GET"])
def getCurrenciesOfCountry(request, country_id):
    name_country = CountryModel.objects.filter(
        id=country_id).values_list('name_country', flat=True)
    currencies = CountriesHasCurrenciesModel.objects.filter(
        id_country=country_id)

    print(currencies)

    if not currencies.exists():
        return Response(
            {"success": False, "message": "No hay resultados para su petición"},
            status=status.HTTP_200_OK,
        )

    contentSerialized = CountriesHasCurrenciesSerializer(currencies, many=True)

    return Response(
        {"success": True, "message": "", "country": name_country,
            "currencies": contentSerialized.data},
        status=status.HTTP_200_OK,
    )
