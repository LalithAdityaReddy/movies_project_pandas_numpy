import pandas as pd
import numpy as np
 
class TeluguMoviesDataset:
    def __init__(self,dataset_path):
        self.dataset_path=dataset_path
        self.df=pd.read_csv(dataset_path)
    def display_dataset(self):
        print(self.df.head()) #Display the first 5 rows of the dataset.
    def add_movie(self,title,genre,rating):
        new_movie = {
            "MovieID":self.df["MovieID"].max()+1,
            "Title":title,
            "Genre":genre,
            "Rating":rating
        }
        self.df=pd.concat([self.df,pd.DataFrame([new_movie])],ignore_index=True)
    def save_dataset(self):
        self.df.to_csv(self.dataset_path,index=False)
    def filter_by_genre(self,genre):
        filtered=self.df[self.df['Genre'].str.contains(genre,case=False)]
        print(filtered)
        return filtered
    def calculate_statistics(self):
        print("AVERAGE RATING : ",self.df["Rating"].mean())
        print("HIGHEST RATING : ",self.df["Rating"].max())
        print("LOWEST RATING : ",self.df["Rating"].min())
    def recommend_movies(self,threshold=4.5):
          """Recommend movies with a rating above a certain threshold."""
          recommended=self.df[self.df["Rating"]>=threshold]
          print("Recommended Movies : ")
          print(recommended)
def analyze_ratings_distribution(df):
        """Analyze the distribution of ratings using NumPy."""        
        ratings=df['Rating'].to_numpy()
        print("Rating Statistics : ")
        print(f"MEAN : {np.mean(ratings):.2f}, MEDIAN : {np.median(ratings):.2f},STANDARD DEVIATION:{np.std(ratings):.2f}")
        return ratings


def main():
    dataset_path='/Users/lalithadityareddy/Desktop/movie_project/telugu_movies_corrected.csv'
    dataset=TeluguMoviesDataset(dataset_path)

    print("Intial Dataset : ")
    dataset.display_dataset()

    # Add a new movie
    print("\nAdding a new movie...")
    dataset.add_movie("Gopala Gopala","Capitative,Drama", 4.2)
    dataset.save_dataset()
    
    # Filter movies by genre
    print("\nMovies in the 'Action' genre:")
    dataset.filter_by_genre("Drama")
    
    # Calculate statistics
    print("\nDataset Statistics:")
    dataset.calculate_statistics()
    
    # Recommend movies
    print("\nRecommended Movies:")
    dataset.recommend_movies(4.6)
    
    # Analyze ratings distribution
    print("\nRatings Distribution Analysis:")
    analyze_ratings_distribution(dataset.df)

if __name__ == "__main__":
    main()   

