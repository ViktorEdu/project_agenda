
from importlib.metadata import MetadataPathFinder
from typing import Any
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from contact.models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = 'first_name','last_name','phone'

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


    

def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
            }
        return render(
            request,
            'contact/create.html',
            context
            )

    context = {
        'form': ContactForm()
        }
    
    return render(
        request,
        'contact/create.html',
        context
    )