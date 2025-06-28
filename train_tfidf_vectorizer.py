import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Load the dataset
print('Loading dataset...')
df = pd.read_csv('cleaned_jira_dataset.csv')
df['clean_summary'] = df['clean_summary'].fillna('')

# Train TF-IDF Vectorizer
print('Training TF-IDF Vectorizer...')
tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
tfidf.fit(df['clean_summary'])

# Save the vectorizer
print('Saving vectorizer as tfidf_vectorizer.pkl...')
joblib.dump(tfidf, 'tfidf_vectorizer.pkl')
print('TF-IDF Vectorizer saved as tfidf_vectorizer.pkl') 