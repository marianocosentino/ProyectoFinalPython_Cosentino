from django.urls import path
from .views import review_list, review_detail, review_create, review_edit, user_posts, review_delete, review_search, index, comment_delete, comment_edit, about_me

urlpatterns = [
    path('', index, name='index'),
    path('review/list', review_list, name='review_list'),
    path('review/<int:pk>/', review_detail, name='review_detail'),
    path('review/new/', review_create, name='review_create'),
    path('review/<int:pk>/edit/', review_edit, name='review_edit'),
    path('user_posts/', user_posts, name='user_posts'),
    path('review/<int:pk>/delete/', review_delete, name='review_delete'),
    path('search/', review_search, name='review_search'),
    path('comment/<int:pk>/edit/', comment_edit, name='comment_edit'),
    path('comment/<int:pk>/delete/', comment_delete, name='comment_delete'),
    path('about/', about_me, name='about_me'),
]
