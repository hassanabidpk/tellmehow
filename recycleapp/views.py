from django.shortcuts import render, get_object_or_404, redirect



def index(request):
    context = {}
    return render(request, "recycleapp/index.html", context)

