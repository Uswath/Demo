
from django import forms
from moviee.models import movies

class movieeform(forms.ModelForm):
    class Meta:
        model = movies
        fields = '__all__'
