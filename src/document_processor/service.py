import logging
from pathlib import Path

from document_processor.models import Document, ProcessedDocument
from document_processor.processor import DocumentProcessor
from document_processor.repository import DocumentRepository

logger = logging.getLogger(__name__)


class DocumentService:
    def __init__(
        self, repository: DocumentRepository, processor: DocumentProcessor
    ) -> None:
        self.repository = repository
        self.processor = processor

    def process_file(self, doc_id: str, file_path: str | Path) -> ProcessedDocument:
        """Process a document from a file and save it to the repository."""
        logger.info("Processing document from file: %s", doc_id)

        doc = Document.from_file(doc_id=doc_id, file_path=file_path)
        processed_doc = self.processor.process(doc)
        self.repository.save_document(processed_doc)

        logger.info("Processed and saved document from file: %s", doc_id)
        return processed_doc

        # to accept text directly instead of a file

    def process_text(self, doc_id: str, title: str, text: str) -> ProcessedDocument:
        """Process a document from text and save it to the repository."""

        logger.info("Processing document from text: %s", doc_id)

        doc = Document(doc_id=doc_id, title=title, text=text)
        processed_doc = self.processor.process(doc)
        self.repository.save_document(processed_doc)

        logger.info("Processed and saved document from text: %s", doc_id)
        return processed_doc

    def get_processed_document(self, doc_id: str) -> ProcessedDocument:
        """Retrieve a processed document from the repository."""

        logger.info("Retrieving processed document: %s", doc_id)
        return self.repository.get_document(document_id=doc_id)

    def delete_processed_document(self, doc_id: str) -> None:
        """Delete a processed document from the repository."""

        logger.info("Deleting processed document: %s", doc_id)
        self.repository.delete_document(document_id=doc_id)
