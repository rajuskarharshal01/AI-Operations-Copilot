from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct


client = QdrantClient(":memory:")

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