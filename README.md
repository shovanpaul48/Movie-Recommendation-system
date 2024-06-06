# Movie Recommendation System

Basic Recommendation System using TMDB 5000 movie dataset 


There are 3 main types of Recommendation System

    1. Content based system 
    2. Collaborative Recommender system
    3. Hybrid system

This is a content based system 

Step 1: Collect dataset from keggle

    https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Step 2: Load data and clean / preprocess data 

Step 3: Now based on the keywords present in the dataset based on each movie find the most used 5000(user defined) keywords. then check which keywords are avilabe for each movie

(5000,5000) , 5000 ->movies, 5000->keywords

Step 4: Apply Vectorization on that data .
    
Step 5: Find/Recommend 5 nearest vector for selected vector(movie)

Step 6: Use TMDB api key to fetch poster and rating

Here I use streamlit to make a website

🚀To run use Command
    streamlit run app.py


#I host this projet on Render here is the link, try it
https://movie-recommendation-system-ihui.onrender.com/

    streamlit run app.py
