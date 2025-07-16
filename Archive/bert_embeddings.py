from sentence_transformers import SentenceTransformer
import numpy as np

# Load a semantic embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")
company_names = get_data()["companies_cleaned"].str.lower()
# Sample company names


# Encode into dense vectors
embeddings = model.encode(company_names, convert_to_numpy=True)



np.save("../data/embeddings.npy", embeddings)
