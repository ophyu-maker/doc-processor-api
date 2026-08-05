from pathlib import Path

from src.document_processor.models import Document, ProcessedDocument
from src.document_processor.processor import DocumentProcessor
from src.document_processor.repository import DocumentRepository


class DocumentService:
    def __init__(
        self, repository: DocumentRepository, processor: DocumentProcessor
    ) -> None:
        self.repository = repository
        self.processor = processor

    def process_file(self, doc_id: str, File_path: str | Path) -> ProcessedDocument:
        """Process a document from a file and save it to the repository."""
        doc = Document.from_file(doc_id=doc_id, file_path=File_path)
        processed_doc = self.processor.process(doc)
        self.repository.save_document(processed_doc)
        return processed_doc

    def get_processed_document(self, doc_id: str) -> ProcessedDocument:
        """Retrieve a processed document from the repository."""
        return self.repository.get_document(document_id=doc_id)

    def delete_processed_document(self, doc_id: str) -> None:
        """Delete a processed document from the repository."""
        self.repository.delete_document(document_id=doc_id)

    # to accept text directly instead of a file
    def process_text(self, doc_id: str, title: str, text: str) -> ProcessedDocument:
        """Process a document from text and save it to the repository."""
        doc = Document(doc_id=doc_id, title=title, text=text)
        processed_doc = self.processor.process(doc)
        self.repository.save_document(processed_doc)
        return processed_doc
