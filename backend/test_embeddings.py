from pdf_reader import extract_text
from chunker import chunk_text
from embedder import create_embeddings

text = extract_text("../uploads/sample.pdf")

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

print("Number of Chunks:",
      len(chunks))

print("Embedding Shape:",
      embeddings.shape)

print("\nFirst Embedding:")

print(embeddings[0][:10])