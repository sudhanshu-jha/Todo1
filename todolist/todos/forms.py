from django import forms

from .models import Todo


class EditForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("Title", "Description")

    widgets = {
        "Title": forms.TextInput(attrs={"class": "textinputclass"}),
        "Description": forms.Textarea(
            attrs={"class": "editable medium-editor-textarea postcontent"}
        ),
    }
