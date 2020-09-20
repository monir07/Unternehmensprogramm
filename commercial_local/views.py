from django.shortcuts import render

# Create your views here.


def commercial_local(request):
    context = {

    }
    return render(request, "commercial_local/commercial_local.html", context)