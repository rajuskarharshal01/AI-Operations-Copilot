from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer



client = QdrantClient(path="./qdrant_data")
model = SentenceTransformer("all-MiniLM-L6-v2")

COLLECTION_NAME = "documents"

def create_collection():
    collections = client.get_collections()

    existing = [c.name for c in collections.collections]

    if COLLECTION_NAME not in existing:

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE)
        )


def store_embeddings(chunks, embeddings):

    points = []

    for idx, (chunk, embedding) in enumerate(
        zip(chunks, embeddings) ):

        points.append(
            PointStruct(
                id = idx,
                vector = embedding,
                payload = {
                    "text": chunk
                }
            )
        )
        

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    
    )

def search_embeddings(
    query_embedding,
    limit: int = 3
):
    create_collection()

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        limit=limit
    )

    return [
        point.payload["text"]
        for point in results.points
    ]


def retrieve_context(query: str):

    query_embedding = model.encode(query).tolist()

    results = search_embeddings(query_embedding)

    context = "\n\n".join(results)

    return context