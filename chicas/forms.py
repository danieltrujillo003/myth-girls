from django import forms
from django.contrib.auth.models import User
from chicas.models import new_entry #entry_reply, UserProfile, 

class new_entryForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    entry = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = new_entry
        fields = ('name','entry')
