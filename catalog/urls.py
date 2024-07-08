from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", contacts, name="contacts"),
    path("", home, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
