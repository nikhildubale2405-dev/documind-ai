from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import tempfile


def parse_document(file):
    # Save temp file
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(file.file.read())
        tmp_path = tmp.name

    reader = PdfReader(tmp_path)

    pages = []
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if text.strip():
            pages.append(f"[PAGE {i}]\n{text}")

    full_text = "\n".join(pages)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )

    chunks = splitter.split_text(full_text)

    return chunks