import chromadb

client = chromadb.PersistentClient(
    path="../chroma_db"
)

collection = client.get_or_create_collection(
    name="pdf_data"
)


def reset_collection():

    global collection

    try:

        client.delete_collection(
            name="pdf_data"
        )

    except:

        pass

    collection = client.get_or_create_collection(
        name="pdf_data"
    )


def store_chunks(
        chunks,
        embeddings
):

    ids = []

    for i in range(
            len(chunks)
    ):

        ids.append(
            str(i)
        )

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )


def search_chunks(
        query_embedding,
        n_results=5
):

    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=n_results
    )

    return results