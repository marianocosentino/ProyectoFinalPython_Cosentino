from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Introduce tu correo electrónico'})
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Introduce tu contraseña'})
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirma tu contraseña'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'description', 'avatar']
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'description': 'Descripción',
            'avatar': 'Avatar',
        }
        help_texts = {
            'username': None,
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce tu nombre de usuario'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Introduce tu correo electrónico'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce tu nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce tu apellido'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe una breve descripción', 'rows': 3}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password' in self.fields:
            del self.fields['password']
        if 'password1' in self.fields:
            self.fields['password1'].help_text = None

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Nombre de Usuario',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce tu nombre de usuario'})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Introduce tu contraseña'})
    )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'description', 'avatar']
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo electrónico',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'description': 'Descripción',
            'avatar': 'Avatar',
        }
        error_messages = {
            'username': {
                'required': 'Este campo es obligatorio.',
                'unique': 'Este nombre de usuario ya está en uso.',
            },
            'email': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Introduce una dirección de correo electrónico válida.',
            },    
            'first_name': {
                'required': 'Este campo es obligatorio.',
            },
            'last_name': {
                'required': 'Este campo es obligatorio.',
            },
            'description': {
                'max_length': 'La descripción es demasiado larga.',
            },
            'avatar': {
                'invalid_image': 'El archivo no es una imagen válida.',
            },
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce tu nombre de usuario'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Introduce tu correo electrónico'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce tu nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce tu apellido'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe una breve descripción', 'rows': 3}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Contraseña Actual",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'current-password', 'autofocus': True, 'placeholder': 'Introduce tu contraseña actual'}),
        strip=False,
    )
    new_password1 = forms.CharField(
        label="Nueva Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password', 'placeholder': 'Introduce tu nueva contraseña'}),
        strip=False,
        help_text="Tu contraseña debe tener al menos 8 caracteres.",
    )
    new_password2 = forms.CharField(
        label="Confirmar Nueva Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password', 'placeholder': 'Confirma tu nueva contraseña'}),
        strip=False,
    )

    error_messages = {
        'password_mismatch': "Las contraseñas no coinciden.",
    }