from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


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