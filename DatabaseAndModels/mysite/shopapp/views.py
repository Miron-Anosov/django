from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import Group
from shopapp.models import Product, Order


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "Customers": "Customers", 'name_block': 'people:',
        "customers_orm_obj": [
            {"name": "bob", "age": 34, "order": 1000},
            {"name": "tom", "age": 22, "order": 5555},
            {"name": "rik", "age": 31, "order": 177}
            ],
    }

    return render(request=request, template_name="shopapp/shop-index.html",
                  context=context)


def get_groups(request: HttpRequest) -> HttpResponse:
    context = {"groups": Group.objects.prefetch_related("permissions").all()}

    return render(request=request, template_name="shopapp/group.html", context=context)


def get_products(request: HttpRequest) -> HttpResponse:
    context = {"products": Product.objects.all()}
    return render(request=request, template_name="shopapp/products.html", context=context)


def get_orders(request: HttpRequest) -> HttpResponse:
    context = {"orders": (Order.objects.select_related("user").
                          prefetch_related("product").all())}
    return render(request=request,
                  template_name="shopapp/orders.html",
                  context=context)