from fastapi import FastAPI
from document_processor.schemas import (
    ProcessFileRequest,
    ProcessTextRequest,
    ProcessedDocumentResponse,
    TextStatisticsResponse,
)
from document_processor.models import Document, ProcessedDocument
from document_processor.service import DocumentService
from document_processor.processor import DocumentProcessor
from document_processor.repository import DocumentRepository

from document_processor.analyzer import TextAnalyzer
from document_processor.chunker import TextChunker
from document_processor.cleaner import TextCleaner


# Initialize the DocumentProcessor and DocumentService. Reduce repetition
processor = DocumentProcessor(
    cleaner=TextCleaner(),
    analyzer=TextAnalyzer(),
    chunker=TextChunker(chunk_size=5),
)
repository = DocumentRepository(storage_dir="data/processed")
service = DocumentService(repository=repository, processor=processor)


# Helper function to convert ProcessedDocument to ProcessedDocumentResponse.
def to_response(processed_doc: ProcessedDocument) -> ProcessedDocumentResponse:
    return ProcessedDocumentResponse(
        doc_id=processed_doc.document.doc_id,
        title=processed_doc.document.title,
        cleaned_text=processed_doc.cleaned_text,
        analysis_results=TextStatisticsResponse(
            char_count=processed_doc.analysis_results.char_count,
            word_count=processed_doc.analysis_results.word_count,
            sentence_count=processed_doc.analysis_results.sentence_count,
            unique_words=processed_doc.analysis_results.unique_words,
        ),
        text_chunks=processed_doc.text_chunks,
    )


app = FastAPI(title="Document Processor API")


@app.get("/")
def root():
    return {"message": "Welcome to the Document Processor API!"}


@app.post("/documents/file", response_model=ProcessedDocumentResponse)
def process_document(request: ProcessFileRequest):

    processed_doc = service.process_file(doc_id="doc2", File_path=request.file_path)

    response = to_response(processed_doc)
    return response


@app.post("/documents/texts", response_model=ProcessedDocumentResponse)
def process_text(request: ProcessTextRequest):
    processed_doc = service.process_text(
        doc_id="doc1", text=request.text, title=request.title
    )

    response = to_response(processed_doc)
    return response


@app.get("/documents/{doc_id}", response_model=ProcessedDocumentResponse)
def get_processed_document(doc_id: str):

    processed_doc = service.get_processed_document(doc_id=doc_id)

    response = to_response(processed_doc)
    return response


@app.delete("/documents/{doc_id}")
def delete_processed_document(doc_id: str):

    service.delete_processed_document(doc_id=doc_id)

    return {"message": f"Processed document with ID '{doc_id}' has been deleted."}
