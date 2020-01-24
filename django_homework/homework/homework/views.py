import requests
from django.http import HttpResponse

from django.template.loader import get_template

from .settings import POKEMON_URL


def health_check(request):
    return HttpResponse("OK")


def index(request):
    template = get_template('index.html').render()
    return HttpResponse(template)


def question(request):
    response = requests.get(f'{POKEMON_URL}/type/3')
    data = [f"{p['pokemon']['name']}" for p in response.json()['pokemon']]
    context = {'data': data}
    html = get_template('pokemon.html').render(context)
    return HttpResponse(html)
