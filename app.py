import streamlit as st
import kaggle
import pandas as pd
import zipfile
from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch
from tqdm import tqdm

# Authenticate Kaggle API
kaggle.api.authenticate()

# Download dataset
dataset = "harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows"
kaggle.api.dataset_download_files(dataset)

with zipfile.ZipFile("imdb-dataset-of-top-1000-movies-and-tv-shows.zip", "r") as zip_ref:
    zip_ref.extractall(".")

# Load dataset into DataFrame
movies = pd.read_csv("imdb_top_1000.csv")

# Clean and concatenate text fields
movies['combined_text'] = movies['Series_Title'] + ' ' + movies['Overview']

# Connect to Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'https'}], http_auth=('elastic', 'QniIJli3-hIugmvXGNtS'),verify_certs=False,ssl_show_warn=False)

# Load Sentence Embedding Model
model = SentenceTransformer('all-mpnet-base-v2')

index_name = 'movie_embeddings_2'

# Function to search for similar movies
def search_similar_movies(query, top_n=5):
    query_embedding = model.encode(query)
    script_query = {
        "script_score": {
            "query": {"match_all": {}},
            "script": {
                "source": "cosineSimilarity(params.query_embedding, 'embedding') + 1.0",
                "params": {"query_embedding": query_embedding.tolist()}
            }
        }
    }

    search_results = es.search(index='movie_embeddings_2', body={
        "size": top_n,
        "query": script_query,
        "_source": True
    })

    similar_movies_ids = [result['_id'] for result in search_results['hits']['hits']]
    similar_movies = [(movies.iloc[int(movie_id)]['Series_Title'], movies.iloc[int(movie_id)]['Overview']) for movie_id in similar_movies_ids]
    return similar_movies

# Streamlit UI
st.set_page_config(
    page_title="Movie Search App",
    page_icon="🎥",
    layout="wide"
)

st.title('Movie Rec')

st.markdown(
    """
    <style>
        .main {
            background-image: url('https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            padding: 50px;
        }
        .title {
            color: #FFFFFF;
            text-shadow: 2px 2px #000000;
            text-align: center;
            font-size: 36px;
            margin-bottom: 30px;
        }
        .text {
            color: #FFFFFF;
            font-size: 18px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

search_query = st.text_input('What is your genre ? ', '')

if st.button('Search'):
    if search_query:
        similar_movies = search_similar_movies(search_query)

        # Create a DataFrame to hold the search results
        results_df = pd.DataFrame(similar_movies, columns=['Movie', 'Description'])

        st.markdown("<h2 class='title'>Top 5 movies similar to '{}' are:</h2>".format(search_query), unsafe_allow_html=True)

        # Display the search results in a table
        st.table(results_df)
