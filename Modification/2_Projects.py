import pickle
import streamlit as st
import requests
st.title("")
st.sidebar.success("SELECT A PAGE ABOVE.")
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters
# Add CSS with custom font and additional styling
st.markdown(
    """
    <style>
    /* Custom font */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    body {
        font-family: 'Roboto', Segoe Script;
        background-color: #F8ECDF;
    }
    .movie-header {
        font-size: 2em;
        text-align: center;
        color: #333;
    }
    .movie-card {
        background-color: #CCFFFF;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin-bottom: 20px;
    }
    .movie-card h3 {
        margin-bottom: 10px;
        color: #333;
    }
    .movie-card img {
        max-width: 100%;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<h1 class="movie-header">MOVIE RECOMMENDER SYSTEM</h1>', unsafe_allow_html=True)
movies = pickle.load(open('pages\movie_list.pkl','rb'))
similarity = pickle.load(open('pages\similarity.pkl','rb'))
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    for i in range(len(recommended_movie_names)):
        if i % 5 == 0:
            with col1:
                st.markdown('<div class="movie-card"><h3>{}</h3><img src="{}"></div>'.format(recommended_movie_names[i], recommended_movie_posters[i]), unsafe_allow_html=True)
        elif i % 5 == 1:
            with col2:
                st.markdown('<div class="movie-card"><h3>{}</h3><img src="{}"></div>'.format(recommended_movie_names[i], recommended_movie_posters[i]), unsafe_allow_html=True)
        elif i % 5 == 2:
            with col3:
                st.markdown('<div class="movie-card"><h3>{}</h3><img src="{}"></div>'.format(recommended_movie_names[i], recommended_movie_posters[i]), unsafe_allow_html=True)
        elif i % 5 == 3:
            with col4:
                st.markdown('<div class="movie-card"><h3>{}</h3><img src="{}"></div>'.format(recommended_movie_names[i], recommended_movie_posters[i]), unsafe_allow_html=True)
        else:
            with col5:
                st.markdown('<div class="movie-card"><h3>{}</h3><img src="{}"></div>'.format(recommended_movie_names[i], recommended_movie_posters[i]), unsafe_allow_html=True)