from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Product

def show_main(request):
    context = {
        'app_name': 'Beyond the Game',
        'name': 'Rusydan Mujtaba Ibnu Ramadhan',
        'class': 'PBP F'
    }
    return render(request, "main.html", context)

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
