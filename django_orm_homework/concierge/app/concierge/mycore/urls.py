from django.urls import path

from .views import index, my_core_serializer, tenant_list, rooms_list, journal_list, JournalCreateView

urlpatterns = [
    path('', index, name='index'),
    path('<str:object_type>/<int:object_id>', my_core_serializer, name='my_core_serializer'),
    path('key-transfer/', JournalCreateView.as_view(), name='journal_view'),
    path('tenant-list/', tenant_list, name='tenant_list'),
    path('rooms-list/', rooms_list, name='rooms-list'),
    path('journal-view/', journal_list, name='journal_view'),
]
