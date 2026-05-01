from fastapi import APIRouter, UploadFile, File
from app.services.parser import parse_document
from app.services.store import add_chunks

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    chunks = parse_document(file)
    add_chunks(file.filename, chunks)
    return {"message": f"File '{file.filename}' uploaded successfully"}