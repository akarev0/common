from django.core import serializers
from django.http import HttpResponse
from django.template.loader import render_to_string

from mycore import models


def health_check(request):
    return HttpResponse("OK")


def index(request):
    return HttpResponse(render_to_string('index.html', {'title': 'Concierge'}))


def api_serializer(request, object_type, object_id):
    try:
        model = getattr(models, object_type.capitalize()).objects.all()
        return HttpResponse(
            serializers.serialize("xml", [model.objects.get(id=object_id)])
        )
    except AttributeError:
        # do 404 page
        ...
    return HttpResponse("DOESN'T WORK")
