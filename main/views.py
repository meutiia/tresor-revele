from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Meutia Fajriyah',
        'npm' : '2306165635',
        'class' : 'PBP B',
    }

    return render(request, "main.html", context)