

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_tours(user_profile, all_tours):
    # Assuming `all_tours` is a pandas DataFrame with a 'Description' column
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(all_tours['Description'])

    # Calculate cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Logic to recommend tours based on user preferences
    recommendations = all_tours.iloc[cosine_sim.argsort()[0][-5:]]
    return recommendations
