from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


from ..mycore.views import TenantListView

static_patterns = static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT) + \
                  static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tenant/List/', TenantListView.as_view()),
] + static_patterns
