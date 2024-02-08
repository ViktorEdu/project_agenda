from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from . import models



class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'classe-a classe-b',
            'placeholder': 'Digite Aqui',
            }
        ),
        label= 'Primeiro Nome',
        help_text='Digite seu primeiro nome aqui'
    )
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args ,**kwargs)

    #     self.fields['first_name'].widget.attrs.update({
    #         'class': 'classe-a classe-b',
    #         'placeholder': 'Primeiro Nome',
    #         })
    class Meta:
        model = models.Contact
        fields =( 
            'first_name','last_name','phone'
        )

        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class':'classe-a classe-b',
        #             'placeholder':'Primeiro Nome',
        #         }
        #     )
        # }
    def clean(self):
        cleaned_data = self.cleaned_data
        
        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )
        
        return super().clean()
