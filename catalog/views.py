from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog.models import Product


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Имя: {name} \nНомер: {phone} \nСообщение: {message}")
    return render(request, "contacts.html")


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


def user_account(request):
    return render(request, "user_account.html")


class ProductCreateView(CreateView):
    model = Product
    fields = (
        "name",
        "description",
        "price_for_buy",
        "category",
        "image",
    )
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = (
        "name",
        "description",
        "price_for_buy",
        "category",
        "image",
    )
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
