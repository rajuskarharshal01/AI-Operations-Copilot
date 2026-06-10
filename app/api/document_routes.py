from fastapi import APIRouter, UploadFile, File
from app.services.pdf_service import extract_pdf_text
from app.services.chunking_service import chunk_text
import os

router = APIRouter(prefix="/documents", tags=["documents"])

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    pdf_data = extract_pdf_text(file_path)
    chunks = chunk_text(pdf_data["text"])

    return {
        "filename": file.filename,
        "pages": pdf_data["pages"],
        "characters": pdf_data["characters"],
        "chunks": len(chunks),
        "status": "processed"
    }