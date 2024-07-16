from django.shortcuts import render, get_object_or_404

from catalog.models import Product

"""def home(request):
    return render(request, "home.html")"""


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Имя: {name} \nНомер: {phone} \nСообщение: {message}")
    return render(request, "contacts.html")


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)


def user_account(request):
    return render(request, "user_account.html")


def create_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        category = request.POST.get("category")
        description = request.POST.get("description")
        price_for_buy = request.POST.get("price_for_buy")
        image = request.POST.get("image")
        print(
            f"Название: {name} \nКатегория: {category} \nОписание: {description} \nЦена: {price_for_buy}, Изображение: {image}"
        )
    return render(request, "create_product.html")
