from django.forms import ModelForm
from collection.models import Thing


class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ('name', 'description',)
