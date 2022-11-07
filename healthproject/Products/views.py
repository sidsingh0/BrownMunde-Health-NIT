import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Product


def homepage(request):
    if request.method == "POST":
        msg = ""
        query = request.POST.get("searchQuery")
        products = Product.objects.filter(name__icontains=query)
        if not products:
            msg = "Did not find an item related to the search query. Try Again"
        return render(request, "home.html", {"products": products, "msg": msg, "alert": "danger"})
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})


def add(request):
    if request.method == "POST":
        new_product = Product(
            name=request.POST.get("prodname"),
            price=request.POST.get("prodprice"),
            quantity=request.POST.get("prodqty")
        )
        new_product.save()
        return redirect("/")


def delete(request, id):
    prod = Product.objects.filter(id=id).first()
    prod.delete()
    return redirect("/")


def get(request, id):
    prod = Product.objects.filter(id=id).first()
    response = json.dumps({"id": id, "name": prod.name, "price": prod.price, "qty": prod.quantity})
    return JsonResponse(response, safe=False)


def edit(request):
    if request.method == "POST":
        id = request.POST.get("editprodid")
        prod = Product.objects.filter(id=id).first()
        prod.name = request.POST.get("editprodname")
        prod.price = request.POST.get("editprodprice")
        prod.quantity = request.POST.get("editprodqty")
        prod.save()
    return redirect("/")