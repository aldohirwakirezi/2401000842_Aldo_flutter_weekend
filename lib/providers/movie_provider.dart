import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/movie.dart';

class MovieNotifier extends Notifier<List<Movie>> {
  @override
List<Movie> build() {
  return [
    Movie(
      id: '1',
      title: 'Inception',
      posterUrl:
          'https://image.tmdb.org/t/p/w500/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg',
      description: 'A skilled thief enters dreams to steal secrets.',
      genre: 'Sci-Fi',
      year: 2010,
    ),
    Movie(
      id: '2',
      title: 'The Dark Knight',
      posterUrl:
          'https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg',
      description: 'Batman faces a dangerous criminal mastermind.',
      genre: 'Action',
      year: 2008,
    ),
  ];
}
  void addMovie(Movie movie) {
    state = [...state, movie];
  }

  void removeMovie(String id) {
    state = state.where((movie) => movie.id != id).toList();
  }

  void toggleWatched(String id) {
    state = [
      for (final movie in state)
        if (movie.id == id)
          Movie(
            id: movie.id,
            title: movie.title,
            posterUrl: movie.posterUrl,
            description: movie.description,
            genre: movie.genre,
            year: movie.year,
            isWatched: !movie.isWatched,
          )
        else
          movie,
    ];
  }
}

final movieProvider =
    NotifierProvider<MovieNotifier, List<Movie>>(MovieNotifier.new);