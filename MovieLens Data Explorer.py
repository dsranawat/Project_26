# before moving forward Download Movielens dataset (ml-latest-small.zip) from "https://grouplens.org/datasets/movielens/latest/"

import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data():
    try:
        movies = pd.read_csv("movies.csv")
        ratings = pd.read_csv("ratings.csv")
        return movies, ratings
    except FileNotFoundError:
        print("CSV files not found. Ensure 'movies.csv' and 'ratings.csv' are n the directory.")
        exit()

def merge_data(movies, ratings):
    return pd.merge(movies, ratings, on="movieId")

def show_top_rated(data):
    top = data.groupby("title")["rating"].mean().sort_values(ascending=False).head(10)
    print("\n Top Rated Movies:\n", top)

def show_most_rated(data):
    most = data["title"].value_counts().head(10)
    print("\n Most Rated Movies:\n", most)
    most.plot(kind="barh", title="Top 10 Most Rated Movies", color="orange")
    plt.xlabel("Number of Ratings")
    plt.tight_layout()
    plt.show()

def genre_analysis(data):
    data["genres"] = data["genres"].str.split("|")
    genre_data = data.explode("genres")
    avg_genre_rating = genre_data.groupby("genres")["rating"].mean().sort_values(ascending=False)
    print("\n Average Rating by Genre:\n", avg_genre_rating)

    avg_genre_rating.plot(kind="bar", color="green", title="Average Rating by Genre")
    plt.ylabel("Average Rating")
    plt.tight_layout()
    plt.show()

def plot_rating_distribution(data):
    data["rating"].plot(kind="hist", bins=10, color="purple", edgecolor="black", title="Rating Distribution")
    plt.xlabel("Rating")
    plt.tight_layout()
    plt.show()

def main():
    print(" MovieLens Data Explorer ")
    movies, ratings = load_data
    data = merge_data(movies, ratings)

    show_top_rated(data)
    show_most_rated(data)
    genre_analysis(data)
    plot_rating_distribution(data)

if __name__ == "__main__":
    main()