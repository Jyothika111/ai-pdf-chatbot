from sentence_transformers import SentenceTransformer

from vector_store import search_chunks
from llm import generate_answer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

question = input("Ask Question: ")

query_embedding = model.encode(question)

results = search_chunks(query_embedding)

context = "\n".join(
    results["documents"][0]
)

answer = generate_answer(
    question,
    context
)

print("\nAnswer:\n")
print(answer)