from django.shortcuts import render
from .models import carousel

# Create your views here.

def index(request):

    carousel_top = carousel.objects.all()

    context = {

        'carousel_top': carousel_top
    }

    return render(request, 'carousel/index.html', context)