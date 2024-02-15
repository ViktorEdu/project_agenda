
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation

from . import models

class ContactForm(forms.ModelForm):

    picture = forms.ImageField(widget=forms.FileInput(
        attrs={'accept': 'image/*',
               }
        )   
    )
    class Meta:
        model = models.Contact
        fields =('first_name','last_name','phone',
                 'email', 'description','category',
                 'picture',
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
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        description = self.cleaned_data.get('description')

        if first_name == last_name:
            msg =ValidationError(
                'O Sobrenome não pode ser igual ao primeiro nome',
                code='invalid'
            )
            self.add_error('first_name',msg)
            self.add_error('last_name',msg)
            
        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Não digite "ABC" nesse campo !',
                    code='invalid'
                )
        )
        return first_name
    
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
        help_text='Digite o seu primeiro nome.',
        strip=True,
        label='Primeiro Nome'
        )
    last_name = forms.CharField(
        required=True,
        min_length=3,
        help_text='Digite o seu sobrenome.',
        strip=True
        )
    email = forms.EmailField(
        help_text='Digite o seu Email',
        )
    
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name','email', 
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email =self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('O email já existe',
                                code='invalid'))

        return email
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=3,
        max_length=50,
        required=True,
        )
    last_name = forms.CharField(
        min_length=3,
        max_length=50,
        required=True,
        )
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete":'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False)
    
    password2 = forms.CharField(
        label='Password 2',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete":'new-password'}),
        help_text='use the same password',
        required=False)
    
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name','email', 
            'username',
        )

    def clean_email(self):
        email =self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('O email já existe',
                                    code='invalid'))
        return email
    
    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')
        
        if password:
            user.set_password(password)
        if commit:
            user.save()
        
        return user
    
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senha não batem')
                )

        return super().clean()

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )

        return password1