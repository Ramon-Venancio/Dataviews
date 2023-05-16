from django.shortcuts import render
from .models import dados

# Create your views here.


def index(request):
    dt = [x.value for x in dados.objects.all()]
    return render(request, 'dashboard/index.html', {'data': dt})