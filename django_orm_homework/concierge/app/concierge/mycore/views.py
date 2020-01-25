

from django.core.cache import cache
from django.shortcuts import render

# Create your views here.
from django.utils.datetime_safe import date
from django.views.generic import ListView

from .models import Tenant


def tenant_view(request):
    context = dict(
        title='Tenant list',
        object_list=Tenant.objects.all()
    )
    return render(request, 'tenant_list_2.html', context=context)


class TenantListView(ListView):
    model = Tenant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

