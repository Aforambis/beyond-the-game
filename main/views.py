from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Beyond the Game',
        'name': 'Rusydan Mujtaba Ibnu Ramadhan',
        'class': 'PBP F'
    }
    return render(request, "main.html", context)