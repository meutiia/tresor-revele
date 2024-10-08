from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render, redirect, reverse
from main.forms import GoodsEntryForm
from main.models import GoodsEntry
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):

    context = {
        'name' : request.user.username,
        'npm' : '2306165635',
        'class' : 'PBP B',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_goods_entry(request):
    form = GoodsEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        goods_entry = form.save(commit=False)
        goods_entry.user = request.user
        goods_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_goods_entry.html", context)

def show_xml(request):
    data = GoodsEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = GoodsEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = GoodsEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = GoodsEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_goods(request, id):
    # Get goods entry berdasarkan id
    goods = GoodsEntry.objects.get(pk = id)

    # Set goods entry sebagai instance dari form
    form = GoodsEntryForm(request.POST or None, instance=goods)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_goods.html", context)

def delete_goods(request, id):
    # Get goods berdasarkan id
    goods = GoodsEntry.objects.get(pk = id)
    # Hapus goods
    goods.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_goods_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    category = strip_tags(request.POST.get("category"))
    condition = request.POST.get("condition")
    user = request.user

    new_goods = GoodsEntry(
        name=name, price=price, description=description,
        category=category, condition=condition,
        user=user
    )
    new_goods.save()

    return HttpResponse(b"CREATED", status=201)