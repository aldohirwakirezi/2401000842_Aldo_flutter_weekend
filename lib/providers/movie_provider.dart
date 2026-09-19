import 'dart:convert';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/movie.dart';

class MovieNotifier extends Notifier<List<Movie>> {
  static const String moviesKey = 'movies';

  @override
  List<Movie> build() {
    return [
      Movie(
        id: '1',
        title: 'Inception',
        posterUrl:
            'https://image.tmdb.org/t/p/w500/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg',
        description:
            'A skilled thief enters dreams to steal secrets.',
        genre: 'Sci-Fi',
        year: 2010,
      ),
      Movie(
        id: '2',
        title: 'The Dark Knight',
        posterUrl:
            'https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg',
        description:
            'Batman faces a dangerous criminal mastermind.',
        genre: 'Action',
        year: 2008,
      ),
    ];
  }

  Future<void> loadMovies() async {
    final prefs = await SharedPreferences.getInstance();
    final savedMovies = prefs.getString(moviesKey);

    if (savedMovies == null) {
      return;
    }

    final List<dynamic> decoded = jsonDecode(savedMovies);

    state = decoded
        .map(
          (movie) => Movie.fromJson(
            Map<String, dynamic>.from(movie),
          ),
        )
        .toList();
  }

  Future<void> saveMovies() async {
    final prefs = await SharedPreferences.getInstance();

    final data = state
        .map((movie) => movie.toJson())
        .toList();

    await prefs.setString(
      moviesKey,
      jsonEncode(data),
    );
  }

  Future<void> addMovie(Movie movie) async {
    state = [...state, movie];
    await saveMovies();
  }

  Future<void> removeMovie(String id) async {
    state = state
        .where((movie) => movie.id != id)
        .toList();

    await saveMovies();
  }

  Future<void> toggleWatched(String id) async {
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

    await saveMovies();
  }
}

final movieProvider =
    NotifierProvider<MovieNotifier, List<Movie>>(
  MovieNotifier.new,
);