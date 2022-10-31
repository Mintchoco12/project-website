from ast import If
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Reviews

# Create your views here.

def home(request):
    reviews = Reviews.objects
    return render(request, 'reviews/review.html', {'reviews': reviews})

def detail(request, review_id):
    review = get_object_or_404(Reviews, pk=review_id)
    return render(request, 'reviews/detail.html', {'review': review})

def create(request):
    if request.method == 'POST':
        if request.POST['film-title'] and request.POST['review-text'] and request.FILES['poster'] and request.POST['rating']:
            review = Reviews()
            review.film_title = request.POST['film-title']
            review.review_text = request.POST['review-text']
            review.poster = request.FILES['poster']
            review.rating = request.POST['rating']
            review.publisher = request.user
            review.publish_date = timezone.datetime.now()
            review.save()
            return redirect('/reviews/' + str(review.id))
        else:
            return render(request, 'reviews/create.html', {'error': 'All fields are required.'})
    else:
        return render(request, 'reviews/create.html')