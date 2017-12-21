from django import forms
from .models import MusicTrackPage


class MusicTrackForm(forms.ModelForm):
    class Meta:
        model = MusicTrackPage

        fields = ['title', 'intro', 'body', 'date']