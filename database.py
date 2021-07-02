import pandas as pd

metadata = pd.read_csv('C:/Users/aksha/OneDrive/Desktop/Movie Recommender py/movies_metadata.csv', low_memory=False)
metadata = metadata.head(5000)

def Top_List():
    C = metadata['vote_average'].mean()
    #print(round(float(C), 3))

    m = metadata['vote_count'].quantile(0.93)
    #print(m)

    def weighted_rating(x, m=m, C=C):
        v = x['vote_count']
        R = x['vote_average']
        # Calculation based on the IMDB formula
        return (v/(v+m) * R) + (m/(m+v) * C)

    q_movies = metadata.copy().loc[metadata['vote_count'] >= m]
    #print(q_movies.shape)

    q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

    q_movies = q_movies.sort_values('score', ascending=False)

    return q_movies

    print(q_movies[['title', 'vote_count', 'vote_average', 'score']].head(5))
#------------------print(q_movies[['title', 'vote_count', 'vote_average', 'score']].head(5))
#################################################################################################################
#################################################################################################################

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

#Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
tfidf = TfidfVectorizer(stop_words='english')

#Replace NaN with an empty string
metadata['overview'] = metadata['overview'].fillna('')
#print(metadata['overview'].head(3))

#Construct the required TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(metadata['overview'])

#Output the shape of tfidf_matrix
#print(tfidf_matrix.shape)
#print(tfidf_matrix[0][0])

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices[title]
    print(idx)
    print(cosine_sim[idx])
    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return metadata['title'].iloc[movie_indices]

#----------print(get_recommendations('The Godfather'))

####################################################################################################################
####################################################################################################################

# Load keywords and credits
credits = pd.read_csv('C:/Users/aksha/OneDrive/Desktop/Movie Recommender py/credits.csv')
keywords = pd.read_csv('C:/Users/aksha/OneDrive/Desktop/Movie Recommender py/keywords.csv')

# Remove rows with bad IDs.
#metadata = metadata.drop([19730, 29503, 35587])

# Convert IDs to int. Required for merging
keywords['id'] = keywords['id'].astype('int')
credits['id'] = credits['id'].astype('int')
metadata['id'] = metadata['id'].astype('int')

# Merge keywords and credits into your main metadata dataframe
metadata = metadata.merge(credits, on='id')
metadata = metadata.merge(keywords, on='id')

from ast import literal_eval

features = ['cast', 'crew', 'keywords', 'genres']
for feature in features:
    metadata[feature] = metadata[feature].apply(literal_eval)

import numpy as np

def get_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
    return np.nan

def get_list(x):
    if isinstance(x, list):
        names = [i['name'] for i in x]
        #Check if more than 3 elements exist. If yes, return only first three. If no, return entire list.
        if len(names) > 5:
            names = names[:5]
        return names

    #Return empty list in case of missing/malformed data
    return []

# Define new director, cast, genres and keywords features that are in a suitable form.
metadata['director'] = metadata['crew'].apply(get_director)

features = ['cast', 'keywords', 'genres']
for feature in features:
    metadata[feature] = metadata[feature].apply(get_list)

#print(metadata[['title', 'cast', 'director', 'keywords', 'genres']].head(3))

def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        #Check if director exists. If not, return empty string
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''

features = ['cast', 'keywords', 'director', 'genres']

for feature in features:
    metadata[feature] = metadata[feature].apply(clean_data)
############################################################################
def Genre_Search():
    metadata['genres_new'] = metadata['genres']
    def genres_set(x):
        if isinstance(x, list):
            return {str.lower(i.replace(" ", "")) for i in x}
        else:
            #Check if director exists. If not, return empty string
            if isinstance(x, str):
                return str.lower(x.replace(" ", ""))
            else:
                return ''

    metadata['genres_new'] = metadata['genres_new'].apply(genres_set)
    #print(metadata[['genres','cast', 'genres_new']].head(10))
    print(metadata[metadata.genres_new == {'drama', 'family', 'adventure', 'action'}])
############################################################################
def create_soup(x):
    return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres'])

def create_soup2(x):
    return ' '.join(x['genres'])


metadata['soup'] = metadata.apply(create_soup, axis=1)
metadata['soup2'] = metadata.apply(create_soup2, axis=1)

from sklearn.feature_extraction.text import CountVectorizer

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(metadata['soup'])
count_matrix2 = count.fit_transform(metadata['soup2'])

#print(count_matrix2_user_select.shape)
#print(count_matrix2.shape)
#print(count_matrix.shape)

from sklearn.metrics.pairwise import cosine_similarity

cosine_sim2 = cosine_similarity(count_matrix, count_matrix) # return an ndarray

metadata = metadata.reset_index()
indices = pd.Series(metadata.index, index=metadata['title'])

#print(cosine_sim2)#.shape)
#----------print(get_recommendations('The Godfather', cosine_sim2))
