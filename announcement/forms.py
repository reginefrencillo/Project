from django import forms
from .models import Announcement

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'body', 'slug']  # Exclude 'date' since it's auto-added

    def __init__(self, *args, **kwargs):
        super(AnnouncementForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
