from django.contrib.auth.decorators import permission_required
from django.urls import path

from .views import index, health_check, my_core_serializer, JournalView, tenant_list, rooms_list, journal_list, \
    TenantListView

urlpatterns = [
    path('', index, name='index'),
    path('health-check/', health_check, name='health-check'),
    path('<str:object_type>/<int:object_id>', my_core_serializer, name='my_core_serializer'),
    path('key-transfer/', JournalView.as_view(), name='key-transfer'),
    path('tenant-list/', tenant_list, name='tenant_list'),
    path('rooms-list/', rooms_list, name='rooms-list'),
    path('journal-view/', journal_list, name='journal_view'),
    path('tenant/list/', permission_required('mycore.view_tenant')(TenantListView.as_view())),
]
