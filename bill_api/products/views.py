#from django.shortcuts import render
from django.http import  JsonResponse
from .models import Products

# Create your views here.
def index(request):
    #return HttpResponse("Hola, estoy  en la vista productos")

    if request.method == 'GET':
        products = list(Products.objects.all().values("id_product",
                                                    "name_prod",
                                                    "price_prod",
                                                    "stock_prod"))
        #retun HttpRespose(productos)
        return JsonResponse(data={'message':'ok', 'Products':products})
                                

