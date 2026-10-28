from pdf_reader import extract_text
from chunker import chunk_text
from embedder import create_embeddings
from vector_store import store_chunks

text = extract_text("../uploads/sample.pdf")

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

store_chunks(chunks, embeddings)

print("Data stored successfully!")