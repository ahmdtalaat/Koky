from django.shortcuts import render
from microurl.forms import URLform
from microurl.models import MicroUrl


def home(request):  # home page
    def encode(id):
        # base 62 characters
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(characters)
        ret = []
        # convert base10 id into base62 id for having alphanumeric shorten url
        while id > 0:
            val = id % base
            ret.append(characters[val])
            id = id // base
        # since ret has reversed order of base62 id, reverse ret before return it
        return "".join(ret[::-1])
    shorturl = ''
    latesturlid = int
    if MicroUrl.objects.all():
        latesturlid = MicroUrl.objects.latest('shorturl').id + 100000000
    else:
        latesturlid = 1
    if request.method == "POST":
        form = URLform(request.POST)
        if form.is_valid():
            url = form.cleaned_data['longurl']
            if MicroUrl.objects.filter(longurl=url):
                shorturl = MicroUrl.objects.get(longurl=url).shorturl
            else:
                obj = MicroUrl()
                obj.longurl = form.cleaned_data['longurl']
                obj.shorturl = encode(latesturlid)
                obj.save()
                shorturl = MicroUrl.objects.get(longurl=url).shorturl
    else:
        form = URLform()
    shortenurl = f'http://bla.co/{shorturl}'
    context = {
        'shorturl': shortenurl,
        'form': form

    }
    return render(request, "microurl/index.html", context)
