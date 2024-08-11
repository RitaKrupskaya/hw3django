from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    ContactsView,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("", ProductListView.as_view(), name="product_list"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("catalog/create", ProductCreateView.as_view(), name="product_create"),
    path(
        "catalog/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
