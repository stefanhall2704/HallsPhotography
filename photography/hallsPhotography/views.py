from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def home(request):
    photos = ["photo1", "photo2", "photo3", "photo4", "photo5"]
    template = loader.get_template("home.html")
    context = {
        "photos": photos
    }
    return HttpResponse(template.render(context))