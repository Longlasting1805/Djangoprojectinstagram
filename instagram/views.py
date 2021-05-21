from django.shortcuts import render

# Create your views here.
from instagram.models import ImagesLoad


def index(request):
    images = ImagesLoad.objects.all()
    context = {
        "images": images

    }
    return render(request, "upload.html", context)
