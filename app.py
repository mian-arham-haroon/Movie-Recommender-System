import ast
import requests  # type: ignore
import pandas as pd
import streamlit as st  # type: ignore
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=056ebc07d5771c5cfc5a75225c81b380&language=en-US".format(movie_id)
    data = requests.get(url, timeout=10)
    data = data.json()
    poster_path = data.get('poster_path')
    if not poster_path:
        return ""
    return "https://image.tmdb.org/t/p/w500/" + poster_path


@st.cache_data(show_spinner=False)
def load_movie_data():
    movies_df = pd.read_csv('tmdb_5000_movies.csv')
    movies_df['genres'] = movies_df['genres'].fillna('[]').apply(
        lambda value: ' '.join([genre.get('name', '') for genre in ast.literal_eval(value)])
    )
    movies_df['keywords'] = movies_df['keywords'].fillna('[]').apply(
        lambda value: ' '.join([keyword.get('name', '') for keyword in ast.literal_eval(value)])
    )
    movies_df['overview'] = movies_df['overview'].fillna('')
    movies_df['combined_features'] = movies_df['overview'] + ' ' + movies_df['genres'] + ' ' + movies_df['keywords']

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(movies_df['combined_features'])
    similarity = cosine_similarity(tfidf_matrix)
    return movies_df, similarity


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


st.header('Movie Recommender System')
movies, similarity = load_movie_data()

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie from the dropdown',
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])





