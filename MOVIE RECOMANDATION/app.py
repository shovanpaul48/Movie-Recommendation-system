import streamlit as st 
import pickle as pk
import pandas as pd
import requests


def fetch_movie_data(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=32c834e8c8462c1b3add4f21e1c8e688".format(movie_id)

    data = requests.get(url)
    data = data.json()
    # print(data)
    poster_path = data['poster_path']
    rating = data['vote_average']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path,rating

def recommend(movie, no_recommendation):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_rating = []
    for i in distances[1:no_recommendation+1]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        poster,rating = fetch_movie_data(movie_id)
        recommended_movie_posters.append(poster)
        recommended_movie_rating.append(rating)
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters,recommended_movie_rating

movies_dict = pk.load(open(r'movies_dict.plk','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pk.load(open(r'similarity.pkl','rb'))

st.title('Movie Recommenndation System')

Choosed_movie_name = st.selectbox(
'Enter movie name',
movies['title'].values)


# if st.button('Recommend'):
#     recommends = recommend(Choosed_movie_name)
#     for i in recommends:
#         st.write(i)

import streamlit as st
import streamlit.components.v1 as components



if st.button('Recommend'):
    
    no_recommendation = 7
    recommended_movie_names,recommended_movie_posters,recommended_movie_rating = recommend(Choosed_movie_name, no_recommendation)
    col = st.columns(no_recommendation)
    for i in range(no_recommendation):
        
        with col[i]:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])
            st.text(recommended_movie_rating[i])

