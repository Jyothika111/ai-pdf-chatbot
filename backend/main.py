from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil

from pdf_reader import extract_text
from chunker import chunk_text
from embedder import create_embeddings
from vector_store import (
    store_chunks,
    search_chunks,
    reset_collection
)

from vector_store import (
    store_chunks,
    search_chunks,
    reset_collection
)

from models import QuestionRequest

from sentence_transformers import SentenceTransformer

from llm import generate_answer


# --------------------------------------------------
# APP
# --------------------------------------------------

app = FastAPI()


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


# --------------------------------------------------
# EMBEDDING MODEL
# --------------------------------------------------

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# --------------------------------------------------
# HOME
# --------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "AI PDF Chatbot Running"
    }


# --------------------------------------------------
# UPLOAD PDF
# --------------------------------------------------

@app.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    uploads_folder = "../uploads"

    for old_file in os.listdir(uploads_folder):

        old_file_path = os.path.join(
            uploads_folder,
            old_file
        )

        if os.path.isfile(old_file_path):

            os.remove(old_file_path)

    # Save new PDF

    file_path = f"../uploads/{file.filename}"

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    # Extract text

    text = extract_text(
        file_path
    )

    # Create chunks

    chunks = chunk_text(
        text
    )

    # Create embeddings

    embeddings = create_embeddings(
        chunks
    )

    # Clear old ChromaDB data

    reset_collection()

    # Store new chunks

    store_chunks(
        chunks,
        embeddings
    )

    return {
        "message": "PDF processed successfully",
        "filename": file.filename,
        "chunks_created": len(chunks)
    }

# --------------------------------------------------
# ASK QUESTION
# --------------------------------------------------

@app.post("/ask")
def ask_question(
        request: QuestionRequest
):

    query_embedding = embedding_model.encode(
        request.question
    )

    results = search_chunks(
        query_embedding
    )

    context = "\n".join(
        results["documents"][0]
    )

    answer = generate_answer(
        request.question,
        context
    )

    return {
        "question": request.question,
        "answer": str(answer)
    }