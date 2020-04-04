from django.shortcuts import render

# Create your views here.

def index_view(rq, *a, **kw):
    context = {}
    return render(rq, 'index.html/', context)

def list_coord_view(rq, *a, **kw):
    from .models import Location
    context = {'list': Location.objects.all()}
    return render(rq, 'list_coord.html', context)

def config_view(rq, *a, **kw):
    from .models import Location
    lat_from = rq.GET.get('latfrom', '')
    long_from = rq.GET.get('longfrom', '')
    lat_to = rq.GET.get('latto', '')
    long_to = rq.GET.get('longto', '')
    if lat_from == '' or long_from == '' or lat_to == '' or lat_from == '':
        return render(rq, 'config.html', {'values': True})

    Location.objects.create(lat_from=lat_from, lat_to=lat_to, 
        long_from=long_from, long_to=long_to)
    context = {
        'lat_from': lat_from,
        'lat_to': lat_to,
        'long_from': long_from,
        'long_to': long_to
    }
    return render(rq, 'config.html', context)

def map_view(rq, *a, **kw):
    from .models import Location
    l = list(Location.objects.filter())[-1]
    context = {
        'lat_to': l.lat_to,
        'long_to': l.long_to,
        'lat_from': l.lat_from,
        'long_from': l.long_from
    }
    return render(rq, 'map.html', context)