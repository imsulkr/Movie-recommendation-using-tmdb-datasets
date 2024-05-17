import streamlit as st
import pandas as pd
import pickle
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similsrity.pkl','rb'))
def recommend(movie):
    movies_index = movies[movies['title']== movie].index[0]
    distance = similarity[movies_index]
    movies_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommend_movie = []
    for i in movies_list:
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie

st.title('Movie Recommender system')
selected_movie = st.selectbox('Movies',movies['title'].values)
if st.button('Recommend'):
    recommendation = recommend(selected_movie)
    for i in recommendation:
        st.write(i)


