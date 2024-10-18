def movie_organizer(*movies):
    genre_dict = {}

    for movie_name, genre in movies:
        if genre not in genre_dict:
            genre_dict[genre] = []
        genre_dict[genre].append(movie_name)

    # Sort genres
    sorted_genres = sorted(genre_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    # Output
    result = []
    for genre, movie_list in sorted_genres:
        result.append(f"{genre} - {len(movie_list)}")
        for movie in sorted(movie_list):
            result.append(f"* {movie}")

    return "\n".join(result)


# Examples
print(movie_organizer(("The Matrix", "Sci-fi")))

print(
    movie_organizer(
        ("The Godfather", "Drama"),
        ("The Hangover", "Comedy"),
        ("The Shawshank Redemption", "Drama"),
        ("The Pursuit of Happiness", "Drama"),
        ("The Hangover Part II", "Comedy"),
    )
)

print(
    movie_organizer(
        ("Avatar: The Way of Water", "Action"),
        ("House Of Gucci", "Drama"),
        ("Top Gun", "Action"),
        ("Ted", "Comedy"),
        ("Duck Soup", "Comedy"),
        ("The Dark Knight", "Action"),
        ("A Star Is Born", "Musicals"),
        ("The Warrior", "Action"),
        ("Like A Boss", "Comedy"),
        ("The Green Mile", "Drama"),
        ("21 Jump Street", "Comedy"),
    )
)
