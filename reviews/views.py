from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import MovieReview, Comment
from .forms import MovieReviewForm, SearchForm, CommentForm
from django.db.models import Q
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'reviews/index.html')

def review_list(request):
    reviews = MovieReview.objects.all().order_by('-created_at')
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

def review_detail(request, pk):
    review = get_object_or_404(MovieReview, pk=pk)
    comments = review.comments.all()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.review = review
            new_comment.author = request.user
            new_comment.save()
            return redirect('review_detail', pk=review.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'reviews/review_detail.html', {
        'review': review,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def review_create(request):
    if request.user.is_staff:
        return HttpResponseForbidden("Los administradores no pueden crear posteos propios. Deben contar con una cuenta normal para realizar publicaciones")
    
    if request.method == 'POST':
        form = MovieReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('review_detail', pk=review.pk)
    else:
        form = MovieReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form, 'is_edit': False})

@login_required
def review_edit(request, pk):
    review = get_object_or_404(MovieReview, pk=pk)
    if review.author != request.user and not request.user.is_staff:
        return redirect('review_detail', pk=pk)
    
    if request.method == 'POST':
        form = MovieReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post actualizado correctamente')
            return redirect('review_detail', pk=review.pk)
    else:
        form = MovieReviewForm(instance=review)
    return render(request, 'reviews/review_form.html', {'form': form, 'is_edit': True})

@login_required
def user_posts(request):
    reviews = MovieReview.objects.filter(author=request.user)
    return render(request, 'reviews/user_posts.html', {'reviews': reviews})

@login_required
def review_delete(request, pk):
    review = get_object_or_404(MovieReview, pk=pk)

    # Solo el autor o un administrador pueden eliminar el post
    if review.author != request.user and not request.user.is_staff:
        return HttpResponseForbidden("No tienes permiso para eliminar este posteo.")
    
    if request.method == 'POST':
        review.delete()
        return redirect('review_list')
    
    return render(request, 'reviews/review_confirm_delete.html', {'review': review})

def review_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = MovieReview.objects.filter(Q(title__icontains=query))

    return render(request, 'reviews/review_search.html', {'form': form, 'query': query, 'results': results})

@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    
    if request.user != comment.author and not request.user.is_staff:
        return redirect('review_detail', pk=comment.review.pk)

    form = CommentForm(request.POST or None, instance=comment)
    if form.is_valid():
        form.save()
        return redirect('review_detail', pk=comment.review.pk)

    return render(request, 'reviews/comment_form.html', {'form': form, 'is_edit': True})

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    
    if request.user != comment.author and not request.user.is_staff:
        return redirect('review_detail', pk=comment.review.pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('review_detail', pk=comment.review.pk)
    
    return render(request, 'reviews/comment_confirm_delete.html', {'comment': comment})

def about_me(request):
    return render(request, 'reviews/about_me.html')