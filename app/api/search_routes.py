from fastapi import APIRouter
from app.services.embedding_service import (generate_query_embedding)
from app.services.vector_service import (search_embeddings)

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.get("/")
async def search(query: str):

    query_embedding = generate_query_embedding(query)

    results = search_embeddings(
        query_embedding
    )

    return {
        "query": query,
        "results": results
    }