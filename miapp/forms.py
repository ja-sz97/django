from wsgiref.validate import validator
from django import forms
from django.core import validators

class FormArticle(forms.Form):
    title = forms.CharField(
        label = "Titulo",
        max_length=20,
        widget = forms.TextInput(
            attrs={
                'class':'form-group col-3'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'Titulo demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñ ]*$','Titulo mal formado', 'invalid_title')
        ]
    )
    content = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea(
            attrs={
                'class':'form-control'
            }
        ),
        validators = [
            validators.MaxLengthValidator(20, 'Mucho texto')
        ]

    )

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]
    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices = public_options
    )