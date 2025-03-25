import json, faiss, pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
with open('kb_articles.json') as f:
    kb = json.load(f)

corpus = [article['issue'] for article in kb]
embeddings = model.encode(corpus)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, 'vector.index')
with open('kb_data.pkl', 'wb') as f:
    pickle.dump(kb, f)