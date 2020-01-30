from http import HTTPStatus

from django.core import serializers
from django.core.serializers import SerializerDoesNotExist
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import FormView

import mycore.models as models
from mycore.forms import KeyTransferForm


def health_check(request):
    return HttpResponse("OK")


def index(request):
    return HttpResponse(render_to_string('index.html', {'title': 'Concierge'}))


def api_serializer(request, object_type, object_id):
    try:
        model = getattr(models, object_type.capitalize())
        return HttpResponse(
            serializers.serialize(
                request.GET['format'],
                [model.objects.get(id=object_id)])
        )
    except (AttributeError, SerializerDoesNotExist, models.Tenant.DoesNotExist,
            models.Key.DoesNotExist, models.Room.DoesNotExist):
        return HttpResponse(status=HTTPStatus.NOT_FOUND)


class KeyTransferView(FormView):

    template_name = 'key_transfer_form.html'
    form_class = KeyTransferForm

    def form_valid(self, form):
        form.save_key_transfer()

    def form_invalid(self, form):
        form
