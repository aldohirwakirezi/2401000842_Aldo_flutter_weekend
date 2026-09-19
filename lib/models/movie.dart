class Movie {
  final String id;
  final String title;
  final String posterUrl;
  final String description;
  final String genre;
  final int year;
  bool isWatched;

  Movie({
    required this.id,
    required this.title,
    required this.posterUrl,
    required this.description,
    required this.genre,
    required this.year,
    this.isWatched = false,
  });

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'title': title,
      'posterUrl': posterUrl,
      'description': description,
      'genre': genre,
      'year': year,
      'isWatched': isWatched,
    };
  }

  factory Movie.fromJson(Map<String, dynamic> json) {
    return Movie(
      id: json['id'],
      title: json['title'],
      posterUrl: json['posterUrl'],
      description: json['description'],
      genre: json['genre'],
      year: json['year'],
      isWatched: json['isWatched'] ?? false,
    );
  }
}