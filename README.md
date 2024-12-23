Movie Management System
Overview
The Movie Management System is a Python-based project that allows users to store and manage movies with details like Title, Genre, Rating, and other attributes. This system uses Pandas for data manipulation and OOP principles for structuring the code. It includes features like adding movies, viewing movie details, filtering movies by genre, and removing duplicate entries.

This project is a simple, efficient, and extensible way to manage a movie database, and can serve as a foundation for more complex movie-related applications.

Features
Add Movies: Allows users to add new movies with details like title, genre, and rating.
View Movies: Displays a list of all movies stored in the system.
Filter by Genre: Filters and displays movies that match the given genre.
Remove Duplicates: Removes duplicate movie entries based on specific attributes or all columns.
Data Storage: Uses a CSV file to store movie information for persistence.
Object-Oriented Design: The project is structured using classes, methods, and attributes to follow Object-Oriented Programming principles.
Technologies Used
Python: Programming language for the project.
Pandas: Library used for handling and manipulating data in tabular form (DataFrame).
CSV: File format for storing movie data.
Installation
To get started with the Movie Management System, follow these steps:


Functionality:

Add a Movie: To add a movie, use the add_movie function. This allows you to input the movie's title, genre(s), and rating.

View All Movies: To view all movies in the system, the view_movies function displays a list of all movies.

Filter Movies by Genre: Use the filter_by_genre function to filter movies based on a specific genre. You can input multiple genres, and the system will return movies that match any of the genres.

Remove Duplicates: The system will automatically remove duplicate movies based on the Title and Genre. You can use drop_duplicates() to clean the dataset.

Sample Input/Output:

python
Copy code
# Sample input for adding a movie
movie_system.add_movie('Movie 1', 'Action, Drama', 4.7)
movie_system.add_movie('Movie 2', 'Romance, Comedy', 4.5)

# Sample output when viewing all movies
movie_system.view_movies()

# Sample output for filtering by genre
movie_system.filter_by_genre('Action')
Code Structure
movie_manager.py
Contains the MovieManager class which is responsible for managing movie data.
Methods include:
add_movie(): Adds a movie to the system.
view_movies(): Displays all movies.
filter_by_genre(): Filters movies based on genre.
remove_duplicates(): Removes duplicate movie entries.
main.py
The main entry point of the program where users interact with the movie management system.
Initializes the MovieManager class and invokes the respective methods based on user input.
movies.csv
CSV file where movie data is stored and read/written from.
The CSV includes columns like MovieID, Title, Genre, and Rating.
Example Code
Example of Adding a Movie:
python
Copy code
import pandas as pd
from movie_manager import MovieManager

# Initialize MovieManager
movie_system = MovieManager('movies.csv')

# Add a movie
movie_system.add_movie('Movie 1', 'Action, Drama', 4.7)
Example of Filtering Movies by Genre:
python
Copy code
# Filter movies by genre
filtered_movies = movie_system.filter_by_genre('Action')
print(filtered_movies)
Example of Removing Duplicates:
python
Copy code
# Remove duplicates based on 'Title' and 'Genre'
movie_system.remove_duplicates()

Acknowledgments
Pandas: The project heavily utilizes the Pandas library for data manipulation.
Python: The core language used to develop the entire system.
CSV: Simple and effective way to store and persist movie data.
This README.md file provides a clear overview of your project, installation instructions, usage guidelines, code structure, and example code for users and developers. It will help others understand your project, contribute to it, and utilize it in their own work.







