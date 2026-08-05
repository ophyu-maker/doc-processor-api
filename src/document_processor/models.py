from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from src.document_processor.exceptions import (
    DocumentNotFoundError,
    DocumentProcessingError,
    UnsupportedFileError,
)


@dataclass
class Document:
    doc_id: str
    title: str
    text: str
    # created_at: datetime = field(default_factory=datetime.now)

    def __len__(self) -> int:
        return len(self.text)

    def __str__(self) -> str:
        return f" {self.title} ({len(self)} characters)"

    @classmethod
    def from_file(cls, doc_id: str, file_path: str) -> "Document":
        """Create a Document instance from a file."""
        with open(file_path, "r", encoding="utf-8") as f:
            path = Path(file_path)
            if path.suffix.lower() not in [".txt", ".md"]:
                raise UnsupportedFileError(f"Unsupported file type: {path.suffix}")

            if not path.exists():
                raise DocumentNotFoundError(f"Document not found: {file_path}")

            if not path.is_file():
                raise DocumentProcessingError(f"Path is not a file: {file_path}")

            text = f.read()
        title = path.name  # Use the filename as the title
        return cls(doc_id=doc_id, title=title, text=text)


@dataclass
class TextStatistics:
    char_count: int
    word_count: int
    sentence_count: int
    unique_words: int


@dataclass
class ProcessedDocument:
    document: Document
    cleaned_text: str
    analysis_results: TextStatistics
    text_chunks: list[str]
