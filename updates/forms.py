from django import forms
from updates.models import Updates


class UpdateModelForm(forms.ModelForm):
    class Meta:
        model = Updates
        fields = [
            'user',
            'content',
        ]