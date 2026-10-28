from sentence_transformers import SentenceTransformer
from vector_store import search_chunks

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

question = "When is goldman sachs summer internship program?"

query_embedding = model.encode(question)

results = search_chunks(query_embedding)

print("\nRetrieved Chunks:\n")

for i, doc in enumerate(results["documents"][0]):
    print(f"\nChunk {i+1}:")
    print(doc)
    print("-" * 50)