
# Movie Recommendation System

This is a Movie Recommendation System built using **Streamlit** and **Machine Learning**. The system recommends movies based on a user's selected movie. The recommendations are made using a similarity-based model that compares movie embeddings.

## Features

- **Movie Selection**: Users can select a movie from a dropdown list.
- **Movie Recommendations**: Based on the selected movie, the system provides recommendations of similar movies.
- **Poster Display**: Each recommended movie is displayed with its poster.
- **Smooth Carousel**: The recommended movies are presented in a smooth horizontal scrolling carousel for easy browsing.

## Tech Stack

- **Streamlit**: Used for building the web interface.
- **Pickle**: Used for saving and loading the machine learning model and movie data.
- **TMDB API**: Provides movie poster images and additional data like movie titles.
- **Scikit-learn**: Used for machine learning and calculating similarity between movie embeddings.
- **NLTK**: Used for text cleaning (such as removing stop words and punctuation).

## Requirements

To run this project locally, make sure you have the following dependencies installed:

- Python 3.6+
- streamlit
- requests
- pandas
- scikit-learn
- nltk

You can install the required libraries using:

```bash
pip install streamlit requests pandas scikit-learn nltk
```

## How to Run

1. **Download the files from the Link txt file**: Extract the `similarity.zip` file to get the `similarity.pkl` file. This file is required for the system to run.
2. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

3. Visit the URL provided by Streamlit in your browser (typically `http://localhost:8501`).

## How It Works

- The system loads a dataset of movies from a CSV file containing movie details such as `id`, `title`, `overview`, and `genre`.
- The system computes movie similarity using a pre-trained model that calculates the similarity between movie embeddings.
- When the user selects a movie, the system calculates the closest matching movies based on the similarity index and displays them with posters and titles.
- The posters are fetched from **The Movie Database (TMDb)** API using the movie `id` to get high-quality images.

## Improvements & Future Work

- **Enhanced Recommendation System**: Improve the recommendation model by considering more features such as cast, director, and user ratings.
- **User Profiles**: Allow users to create profiles and get personalized recommendations based on their watching history.
- **Better Poster Design**: Enhance the carousel to allow for a better user experience on mobile devices.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **TMDB API**: For providing movie poster images.
- **Streamlit**: For making web app development easier.
- **Scikit-learn**: For machine learning tools that helped with movie similarity.
