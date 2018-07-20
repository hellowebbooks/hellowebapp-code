from django.shortcuts import render, redirect

from collection.forms import ThingForm
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


def edit_thing(request, slug):
    # grab the object...
    thing = Thing.objects.get(slug=slug)

    # set the form we're using...
    form_class = ThingForm

    # if we're coming to this view from a submitted form,
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=thing)

        if form.is_valid():
            # save the new data
            form.save()
            return redirect('thing_detail', slug=thing.slug)

    # otherwise just create the form
    else:
        form = form_class(instance=thing)

    # and render the template
    return render(request, 'things/edit_thing.html', {
        'thing': thing,
        'form': form,
    })
