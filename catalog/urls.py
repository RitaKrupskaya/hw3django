from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    contacts,
    product_list,
    product_detail,
    user_account,
    create_product,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", contacts, name="contacts"),
    path("", product_list, name="product_list"),
    path("catalog/<int:pk>/", product_detail, name="product_detail"),
    path("user_account/", user_account, name="user_account"),
    path("create_product/", create_product, name="create_product"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
