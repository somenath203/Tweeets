from django.shortcuts import render


def index(request):

    return render(request, 'rootpage/index.html')