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

if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)
    print(f"Deleted existing index: {index_name}")

embeddings = model.encode(movies['combined_text'].tolist(), show_progress_bar=True)
embedding_dim = model.get_sentence_embedding_dimension()
print(embedding_dim)

if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body={
        "mappings": {
            "properties": {
                "Series_Title": {"type": "text"},
                "Overview": {"type": "text"},
                "embedding": {
                    "type": "dense_vector",
                    "dims": 768,  # dims must match your model output
                    "index": True,
                    "similarity": "cosine"
                }
            }
        }
    })

# Index data into Elasticsearch
for idx, (i, row) in enumerate(tqdm(movies.iterrows(), total=len(movies))):
    doc = {
        "Series_Title": row['Series_Title'],
        "Overview": row['Overview'],
        "embedding": embeddings[idx]
    }
    es.index(index=index_name, id=i, body=doc)
