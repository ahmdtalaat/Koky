from django.shortcuts import render
from microurl.forms import URLform


def home(request):  # home page

    if request.method == "POST":
        form = URLform(request.POST)
    else:
        form = URLform()

    return render(request, "microurl/index.html", {"form": form})
