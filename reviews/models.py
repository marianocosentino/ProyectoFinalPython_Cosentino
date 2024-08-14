from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class MovieReview(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    sinopsis = models.TextField(help_text="Sinopsis de la película")
    calificacion = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        help_text="Calificación de la película (entre 1 y 10)",
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(10.0)
        ]
    )
    review = models.TextField(help_text="Review del usuario")
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.author.username}"
    
class Comment(models.Model):
    review = models.ForeignKey(MovieReview, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.review.title}"