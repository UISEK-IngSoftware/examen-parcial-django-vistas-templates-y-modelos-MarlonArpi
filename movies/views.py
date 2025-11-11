from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all().order_by('year')
    context = {'movies': movies, 'total_movies': movies.count()}
    return render(request, 'movies/movie_list.html', context)

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if not movie:
        movie = None
    context = {'movie': movie}
    return render(request, 'movies/movie_details.html', context)