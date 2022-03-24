from dataclasses import field
from unicodedata import category
from django.forms import ModelForm
from .models import Note, Category

from django import forms

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'image', 'description', 'category']
        widgets = {

           'category': forms.CheckboxSelectMultiple(),

        }

    def __init__(self, *args, **kwargs):

        super(NoteForm, self).__init__(*args, **kwargs)

        # self.fields['title'].widget.attrs.update({'class':'input'})
        
        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class':'input'})


class CategoryForm(ModelForm):
    class Meta:
            model = Category
            fields = ['name']
    def __init__(self, *args, **kwargs):

            super(CategoryForm, self).__init__(*args, **kwargs)