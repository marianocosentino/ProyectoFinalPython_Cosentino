from django import forms
from .models import MovieReview, Comment

class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['title', 'director', 'sinopsis', 'calificacion', 'review', 'cover_image']
        labels = {
            'title': 'Título',
            'director': 'Director',
            'sinopsis': 'Sinopsis',
            'calificacion': 'Calificación',
            'review': 'Review',
            'cover_image': 'Imagen de portada',
        }
        help_texts = {
            'calificacion': 'Calificación de la película (ej. 7.5)',
        }
        error_messages = {
            'title': {
                'required': 'Este campo es obligatorio.',
                'max_length': 'El título es demasiado largo.',
            },
            'director': {
                'required': 'Este campo es obligatorio.',
                'max_length': 'El nombre del director es demasiado largo.',
            },
            'sinopsis': {
                'required': 'Este campo es obligatorio.',
            },
            'calificacion': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Introduce un número válido.',
            },
            'review': {
                'required': 'Este campo es obligatorio.',
            },
            'cover_image': {
                'invalid_image': 'El archivo no es una imagen válida.',
            },
        }
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}))
    director = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Director'}))
    sinopsis = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Sinopsis', 'rows': 3}))
    calificacion = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Calificación', 'step': '0.1'}))
    review = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Review', 'rows': 5}))
    cover_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

class SearchForm(forms.Form):
    query = forms.CharField(
        label='Buscar por título',
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por título...'
        })
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': 'Comentario',
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }