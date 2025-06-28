## 🚀FilmFinderX: Smart Semantic Search App 
This project introduces a **semantic movie search engine** that combines the power of **Elasticsearch** and **Sentence Transformers** to deliver meaningful movie recommendations based on context rather than keyword matching.

## 🚀 Features

- **Semantic Embedding Search:** Converts movie descriptions into vector embeddings using `all-mpnet-base-v2` for contextual understanding.
- **Similarity-Based Matching:** Searches based on cosine similarity to return contextually relevant movie suggestions.
- **Genre/Concept Search:** Enables users to explore similar movies by entering themes or genres (e.g., “romantic space drama”).
- **Responsive Web App UI:** Built using **Streamlit** with custom design and real-time query interaction.


## 🔧 Project Workflow

### 1. 📦 Library Setup & Authentication
- Required libraries like `pandas`, `kaggle`, `sentence-transformers`, and `elasticsearch` are imported.
- Kaggle API is used to fetch the IMDb Top 1000 Movies dataset.

### 2. 🧹 Data Preprocessing
- Dataset is cleaned and relevant columns (`Series_Title`, `Overview`) are merged into a single searchable text field.

### 3. 🧠 Embedding & Indexing
- Each movie description is embedded using a pre-trained model.
- Embeddings are indexed into **Elasticsearch** using a dense vector field with cosine similarity.

### 4. 🔍 Semantic Search Function
- A custom query retrieves the most semantically similar movies to the user input.
- The output is formatted and returned as a ranked table of results.

### 5. 💻 Streamlit App
- A user-friendly app built with Streamlit to enter search queries and display movie matches.
- Includes custom background and style enhancements.



## 💻 Execution Instructions

## ▶️ `script.py` (Indexing and Embedding)

1. Make sure Elasticsearch is running locally on:
http://localhost:9200

2. Install required libraries:
```bash
pip install pandas kaggle tqdm sentence-transformers elasticsearch
Run the script:

python script.py
This will download the dataset, generate embeddings, and index them to Elasticsearch.

Note: Replace the default Elasticsearch **username=elastic** and **password=QniIJli3-hIugmvXGNtS** with you own credentials in the code.

## ▶️ app.py (Streamlit App)
Ensure script.py has been run and the index is created.

Launch the app:
streamlit run app.py
Enter a genre or keyword like "thrilling sci-fi" or "family comedy" to receive matching movies.

🛠️ Tech Stack
Python – Core programming

Elasticsearch – Semantic indexing and retrieval

Streamlit – Web app interface

Sentence Transformers – Embedding generation

Kaggle API – Dataset access

📄 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Made by Vraj
