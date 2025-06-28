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


