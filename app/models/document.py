from pydantic import BaseModel

class DocumentMetadata(BaseModel):
    filename: str
    pages: int
    characters: int
    chunks: int