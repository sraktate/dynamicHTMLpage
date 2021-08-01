from django import forms
from .models import EventDetails


class EventModelform(forms.ModelForm):
    class Meta:
        model = EventDetails
        # fields = '__all__'
        exclude = ('is_like', )
        widgets = {
            'date': forms.NumberInput(attrs={'type':'date'}),
            'time': forms.TimeInput(format='%H:%M',attrs={'placeholder': 'Hr:Min'}),

        }