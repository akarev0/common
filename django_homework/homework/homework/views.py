import requests
from django.http import HttpResponse

SIMPLE_TEMPLATE = """
<html>
<head>
    <title>Pokemon</title>
</head>
<body>
    <a href="/question">GIVE ME POKEMONS</a>
</body>
</html>
"""

POCKEMON_URL = 'https://pokeapi.co/api/v2/'


def health_check(request):
    return HttpResponse("OK")


def index(request):
    return HttpResponse(SIMPLE_TEMPLATE)


def question(request):
    response = requests.get(f'{POCKEMON_URL}/type/3')
    return HttpResponse([f"{p['pokemon']['name']}<br />" for p in response.json()['pokemon']])
