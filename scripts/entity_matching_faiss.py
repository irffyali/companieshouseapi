## faiss model 

#ann for fast candidate for more accurate 
import faiss
import numpy as np 
from sklearn.preprocessing import normalize
import torch as t
# Load a semantic embedding model
from sentence_transformers import SentenceTransformer,util
import jellyfish



embeddings = np.load("embeddings.npy")
embeddings = normalize(embeddings, axis=1)

# Define index (L2 distance, 384-dim vectors)
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add vectors to index
index.add(embeddings)


def faiss_candiates(company,model):

    company_vec = model.encode([company], convert_to_numpy=True)
    k=5
    distances, indices = index.search(company_vec, k)

    return distances, indices


def jaro_similarity(company,model,company_names):

    distances,indeces = faiss_candiates(company,model)
    candidates = company_names.iloc[indeces[0]].str.lower()


    best_match, best_score = max(((c, jellyfish.jaro_winkler_similarity(company, c)) for c in candidates),key=lambda x: x[1])
    best_index = candidates[candidates == best_match].index[0]


    return best_match,best_score,best_index

