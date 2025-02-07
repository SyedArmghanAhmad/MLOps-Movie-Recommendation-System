import pickle
import streamlit as st
import requests
from streamlit.components.v1 import html

# Load the movie titles and embeddings
def fetch_poster(movie_id):
    api_key = "a380c88c0581bf6da559a86daaae1dc3"
    url = f"http://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data =requests.get(url)
    data=data.json()
    poster_path = data['poster_path']
    full_path = "http://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Load the movie data and similarity matrix
movies = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
movies_list = movies['title'].values


def recommend_movie(movie):
    index = movies[movies['title'] == movie].index[0]

    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])

    recommended_movies = []
    recommended_posters = []
    for i in distance[1:10]:
        movies_id = movies.iloc[i[0]]['id']
        recommended_movies.append(movies.iloc[i[0]]["title"])
        recommended_posters.append(fetch_poster(movies_id))
    
    return recommended_movies, recommended_posters


# Streamlit App
st.title("🎬 Movie Recommendation System")
st.write("Find your next favorite movie based on your selection!")

# Dropdown for movie selection
selected_movie = st.selectbox("Select a Movie", movies_list)

# Recommend movies when button is clicked
if st.button("Recommend"):
    with st.spinner("Fetching recommendations..."):
        recommended_movies, recommended_posters = recommend_movie(selected_movie)

    st.subheader(f"Recommendations for **{selected_movie}**")

    # Display recommendations as a smooth horizontal scrollable carousel
    carousel_html = """
    <style>
        /* General Carousel Styles */
        .carousel-container {
            display: flex;
            overflow-x: auto;
            gap: 20px;
            padding: 10px;
            scrollbar-width: thin; /* For Firefox */
            scrollbar-color: #888 transparent;
            scroll-behavior: smooth; /* Smooth scrolling */
            -webkit-overflow-scrolling: touch;
        }
        .carousel-container::-webkit-scrollbar {
            height: 8px; /* Scrollbar height */
        }
        .carousel-container::-webkit-scrollbar-thumb {
            background: #888; /* Scrollbar thumb color */
            border-radius: 10px; /* Rounded scrollbar */
        }
        .carousel-container::-webkit-scrollbar-track {
            background: transparent; /* Transparent track */
        }

        /* Individual Carousel Item Styles */
        .carousel-item {
            flex: 0 0 auto; /* Prevent shrinking */
            text-align: center;
            user-select: none; /* Disable selection */
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        }

        .carousel-item img {
            width: 200px;
            height: 300px;
            border-radius: 10px; /* Rounded corners for posters */
            pointer-events: none; /* Prevent poster selection */
            transition: transform 0.3s ease-in-out;
        }

        .carousel-item:hover img {
            transform: scale(1.05); /* Slight zoom effect */
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3); /* Shadow effect */
        }

        /* Movie Title Styles */
        .carousel-item p {
            margin-top: 10px;
            font-size: 16px;
            color: #fff;
            font-family: 'Roboto', sans-serif; /* Modern, clean font */
            user-select: none; /* Disable text selection */
            transition: color 0.3s ease, transform 0.3s ease;
        }

        .carousel-item p:hover {
            color: #F39C12; /* Highlight color on hover */
            transform: translateY(-3px); /* Slight upwards movement */
        }
    </style>
    <div class="carousel-container" onwheel="event.preventDefault(); this.scrollLeft += event.deltaY * 2;">
    """
    for movie, poster in zip(recommended_movies, recommended_posters):
        carousel_html += f"""
    <div class="carousel-item">
        <img src="{poster}" alt="{movie}">
        <p>{movie}</p>
    </div>
    """
    carousel_html += "</div>"

    html(carousel_html, height=350)
