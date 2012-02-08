# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader

from things.models import Site
from things.models import Thing
from things.models import Note

def index(request):
    t = loader.get_template('index.html')
    site = Site.objects.all()[0]
    thing_list = Thing.objects.all()
    thing_complete_list = thing_list.filter(complete_date__isnull=False)
    complete_percentage = float(thing_complete_list.count()) / float(thing_list.count()) * 100
    c = Context({
        'thing_list': thing_list,
        'thing_complete_list': thing_complete_list,
        'site': site,
        'complete_percentage': complete_percentage,
    })
    return HttpResponse(t.render(c))

def detail(request, thing_id):
    t = loader.get_template('detail.html')
    p = Thing.objects.get(pk=thing_id)
    note_list = Note.objects.filter(id=thing_id)
    c = Context({
        'thing': p,
        'note_list': note_list,
    })
    return HttpResponse(t.render(c))
