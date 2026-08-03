"""
parser.py
---------
Handles PDF resume parsing using PyMuPDF (fitz).
Extracts raw text from uploaded PDF files.
"""

import fitz  # PyMuPDF
import io


def extract_text_from_pdf(file) -> str:
    """
    Extract plain text from a PDF file.

    Args:
        file: A file-like object (bytes) or a file path string.

    Returns:
        A single string containing all extracted text from the PDF.
    """
    try:
        # Handle both file-path strings and in-memory bytes (from Streamlit uploader)
        if isinstance(file, (str, bytes)):
            pdf_bytes = file if isinstance(file, bytes) else open(file, "rb").read()
        else:
            pdf_bytes = file.read()

        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        full_text = []

        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text("text")  # Extract plain text
            full_text.append(text)

        doc.close()
        return "\n".join(full_text).strip()

    except Exception as e:
        return f"[ERROR] Failed to parse PDF: {str(e)}"


def get_pdf_metadata(file) -> dict:
    """
    Extract basic metadata from a PDF file.

    Args:
        file: A file-like object or file path.

    Returns:
        A dict with metadata fields (title, author, page count, etc.)
    """
    try:
        if isinstance(file, (str, bytes)):
            pdf_bytes = file if isinstance(file, bytes) else open(file, "rb").read()
        else:
            file.seek(0)  # Reset stream position
            pdf_bytes = file.read()

        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        meta = doc.metadata
        page_count = len(doc)
        doc.close()

        return {
            "title": meta.get("title", ""),
            "author": meta.get("author", ""),
            "page_count": page_count,
        }

    except Exception:
        return {"title": "", "author": "", "page_count": 0}
