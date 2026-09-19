import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/movie.dart';
import '../providers/movie_provider.dart';

class AddMovieScreen extends ConsumerStatefulWidget {
  const AddMovieScreen({super.key});

  @override
  ConsumerState<AddMovieScreen> createState() =>
      _AddMovieScreenState();
}

class _AddMovieScreenState
    extends ConsumerState<AddMovieScreen> {
  final _formKey = GlobalKey<FormState>();

  final titleController = TextEditingController();
  final genreController = TextEditingController();
  final yearController = TextEditingController();
  final posterController = TextEditingController();
  final descriptionController = TextEditingController();

  @override
  void dispose() {
    titleController.dispose();
    genreController.dispose();
    yearController.dispose();
    posterController.dispose();
    descriptionController.dispose();
    super.dispose();
  }

  Future<void> saveMovie() async {
    if (!_formKey.currentState!.validate()) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text(
            'Please correct the errors in the form.',
          ),
        ),
      );
      return;
    }

    final movie = Movie(
      id: DateTime.now().millisecondsSinceEpoch.toString(),
      title: titleController.text.trim(),
      genre: genreController.text.trim(),
      year: int.parse(yearController.text.trim()),
      posterUrl: posterController.text.trim(),
      description: descriptionController.text.trim(),
    );

    await ref.read(movieProvider.notifier).addMovie(movie);

    if (!mounted) return;

    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Text('Movie added successfully!'),
      ),
    );

    Navigator.pop(context);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Add Movie'),
      ),
      body: Form(
        key: _formKey,
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(16),
          child: Column(
            children: [
              TextFormField(
                controller: titleController,
                decoration: const InputDecoration(
                  labelText: 'Movie Title',
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value == null ||
                      value.trim().isEmpty) {
                    return 'Enter a movie title';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              TextFormField(
                controller: genreController,
                decoration: const InputDecoration(
                  labelText: 'Genre',
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value == null ||
                      value.trim().isEmpty) {
                    return 'Enter a genre';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 16),
              TextFormField(
                controller: yearController,
                keyboardType: TextInputType.number,
                decoration: const InputDecoration(
                  labelText: 'Year',
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value == null ||
                      value.trim().isEmpty) {
                    return 'Enter the movie year';
                  }

                  final year = int.tryParse(value);

                  if (year == null) {
                    return 'Enter a valid number';
                  }

                  if (year < 1900 ||
                      year > DateTime.now().year) {
                    return 'Enter a valid year';
                  }

                  return null;
                },
              ),
              const SizedBox(height: 16),
              TextFormField(
                controller: posterController,
                decoration: const InputDecoration(
                  labelText: 'Poster URL',
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value == null ||
                      value.trim().isEmpty) {
                    return 'Enter a poster URL';
                  }

                  if (!value.startsWith('http')) {
                    return 'Enter a valid URL';
                  }

                  return null;
                },
              ),
              const SizedBox(height: 16),
              TextFormField(
                controller: descriptionController,
                maxLines: 4,
                decoration: const InputDecoration(
                  labelText: 'Description',
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value == null ||
                      value.trim().isEmpty) {
                    return 'Enter a description';
                  }
                  return null;
                },
              ),
              const SizedBox(height: 24),
              SizedBox(
                width: double.infinity,
                child: ElevatedButton(
                  onPressed: saveMovie,
                  child: const Text('Save Movie'),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}