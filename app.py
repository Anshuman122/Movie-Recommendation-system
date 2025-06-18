

import streamlit as st
import pickle

# Load the data
movies = pickle.load(open("movies_list.pk1", 'rb'))
similarity = pickle.load(open("similarity.pk1", 'rb'))

# Get the list of movie titles
movies_list = movies['title'].values

# Streamlit header
st.header("Movie Recommender System")

# Dropdown to select a movie
select_values = st.selectbox("Select movie from dropdown", movies_list)

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    
    recommend_movies = []
    for i in distance[1:6]:  # Start from 1 to skip the selected movie itself
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

# Button to show recommendations
if st.button("Show recommend"):
    movie_name = recommend(select_values)
    col1, col2, col3, col4, col5 = st.columns(5)  # Corrected to st.columns(5)
    
    with col1:
        st.text(movie_name[0])
    with col2:
        st.text(movie_name[1])
    with col3:
        st.text(movie_name[2])
    with col4:
        st.text(movie_name[3])
    with col5:
        st.text(movie_name[4])
