from django.http import HttpResponse
from django.template.loader import render_to_string


def key_transfer_created(request):
    return HttpResponse("KEY TRANSFER WAS CREATED")


def index(request):
    return HttpResponse(render_to_string('index.html', {'title': 'Concierge'}))
