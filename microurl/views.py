from django.shortcuts import render, redirect
from microurl.forms import URLform
from microurl.models import MicroUrl


def home(request):
    def encode(id):  # encoding function
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
    shorturl, shortenurl, latesturlid = '', '', int
    if MicroUrl.objects.all():  # if any urls in db.
        latesturlid = MicroUrl.objects.latest('shorturl').id + 100000000
    else:
        latesturlid = 1
    if request.method == "POST":  # checking the request
        form = URLform(request.POST)
        if form.is_valid():
            url = form.cleaned_data['longurl']
            if MicroUrl.objects.filter(longurl=url):
                #  if it's been converted before
                shorturl = MicroUrl.objects.get(longurl=url).shorturl
            else:
                obj = MicroUrl()
                obj.longurl = form.cleaned_data['longurl']
                obj.shorturl = encode(latesturlid)
                obj.save()  # submit to database
                shorturl = MicroUrl.objects.get(longurl=url).shorturl
            shortenurl = f'http://bla.co/{shorturl}'
    else:
        form = URLform()
    context = {
        'shorturl': shortenurl,
        'form': form

    }
    return render(request, "microurl/index.html", context)
