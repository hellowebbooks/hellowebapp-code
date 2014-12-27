from django.shortcuts import render

from collection.models import Thing


# the rewritten view!
def index(request):
    number = 6
    # don't forget the quotes because it's a string, not an integer
    thing = "Thing name"
    return render(request, 'index.html', {
        'number': number,
        # don't forget to pass it in, and the last comma
        'thing': thing,
    })

def thing_detail(request, slug):
    # grab the object...
    thing = Thing.objects.get(slug=slug)
    # and pass to the template
    return render(request, 'things/thing_detail.html', {
        'thing': thing,
    })
