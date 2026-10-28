from pdf_reader import extract_text
from chunker import chunk_text

text = extract_text("../uploads/bhargav lettter.pdf")

chunks = chunk_text(text)

print("Total Chunks:", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0])