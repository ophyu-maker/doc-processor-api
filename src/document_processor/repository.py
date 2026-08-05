import json
from dataclasses import asdict
from pathlib import Path

from src.document_processor.exceptions import DocumentNotFoundError
from src.document_processor.models import Document, ProcessedDocument, TextStatistics


class DocumentRepository:
    def __init__(self, storage_dir: str | Path) -> None:
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)

    def get_document(self, document_id: str):
        file_path = self.storage_dir / f"{document_id}.json"
        if not file_path.exists():
            raise DocumentNotFoundError(f"Document not found: {document_id}")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        document = Document(**data["document"])

        analysis_results = TextStatistics(**data["analysis_results"])

        return ProcessedDocument(
            document=document,
            cleaned_text=data["cleaned_text"],
            analysis_results=analysis_results,
            text_chunks=data["text_chunks"],
        )

    def save_document(self, document: ProcessedDocument):
        file_path = self.storage_dir / f"{document.document.doc_id}.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(asdict(document), f, ensure_ascii=False, indent=4)

    def delete_document(self, document_id):
        file_path = self.storage_dir / f"{document_id}.json"
        if not file_path.exists():
            raise DocumentNotFoundError(f"Document not found: {document_id}")
        file_path.unlink()
