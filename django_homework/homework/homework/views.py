import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template

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

QUESTION_TEMPLATE = """<html>
<head>
    <title>Pokemon</title>
</head>
<body>
    <a href="/index">RETURN TO INDEX</a>
</body>
</html>
"""

POKEMON_URL = 'https://pokeapi.co/api/v2/'


def health_check(request):
    return HttpResponse("OK")


# def index(request):
#     return HttpResponse(SIMPLE_TEMPLATE)

def index(request):
    template = get_template('index.html').render()
    return HttpResponse(template)


def question(request):
    response = requests.get(f'{POKEMON_URL}/type/3')
    data = [f"{p['pokemon']['name']}" for p in response.json()['pokemon']]
    context = {'data': data}
    html = get_template('pokemon.html').render(context)
    return HttpResponse(html)
