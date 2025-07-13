## faiss model 

#ann for fast candidate for more accurate 
import faiss
import numpy as np 
from sklearn.preprocessing import normalize
import torch as t
# Load a semantic embedding model
from sentence_transformers import utils
embeddings = np.load("../data/embeddings.npy")
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


