from django.contrib import admin
from .models import MovieReview, Comment
# Register your models here.

admin.site.register(MovieReview)
admin.site.register(Comment)