from http import HTTPStatus

from django.core import serializers
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from django.views.generic import FormView

from mycore import models
from mycore.forms import JournalForm
from .models import Tenant, Room, Journal


def index(request):
    tenants = Tenant.objects.all()
    rooms = Room.objects.all()
    transfers = Journal.objects.all()
    context = {'tenants': tenants, 'rooms': rooms, 'transfers': transfers}
    return render(request, 'index.html', context)


def health_check(request):
    return HttpResponse("OK")


def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenant_list.html', {'tenants': tenants})


def rooms_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms_list.html', {'rooms': rooms})


def journal_list(request):
    transfers = Journal.objects.all()
    return render(request, 'journal_view.html', {'transfers': transfers})


def my_core_serializer(request, object_type, object_id):
    try:
        model = getattr(models, object_type.capitalize())
        return HttpResponse(
            serializers.serialize(
                request.GET['format'],
                [model.objects.get(id=object_id)])
        )
    except AttributeError:
        return HttpResponse(status=HTTPStatus.NOT_FOUND)


class JournalView(FormView):
    template_name = 'key_transfer_form.html'
    form_class = JournalForm
    success_url = '/mycore/'

    def form_valid(self, form):
        form.save_key_transfer()
        return HttpResponse(status=HTTPStatus.CREATED)
