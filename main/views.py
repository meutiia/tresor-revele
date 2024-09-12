from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from main.forms import GoodsEntryForm
from main.models import GoodsEntry

def show_main(request):
    goods_entries = GoodsEntry.objects.all();

    context = {
        'name' : 'Meutia Fajriyah',
        'npm' : '2306165635',
        'class' : 'PBP B',
        'goods_entries' : goods_entries,
    }

    return render(request, "main.html", context)

def create_goods_entry(request):
    form = GoodsEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_goods_entry.html", context)

def show_xml(request):
    data = GoodsEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = GoodsEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = GoodsEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = GoodsEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")