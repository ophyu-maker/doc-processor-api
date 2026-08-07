from uuid import uuid4

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from document_processor.analyzer import TextAnalyzer
from document_processor.chunker import TextChunker
from document_processor.cleaner import TextCleaner
from document_processor.exceptions import (
    DocumentNotFoundError,
    DocumentProcessingError,
    EmptyDocumentError,
    UnsupportedFileError,
)
from document_processor.models import ProcessedDocument
from document_processor.processor import DocumentProcessor
from document_processor.repository import DocumentRepository
from document_processor.schemas import (
    ProcessedDocumentResponse,
    ProcessFileRequest,
    ProcessTextRequest,
    TextStatisticsResponse,
)
from document_processor.service import DocumentService

app = FastAPI(title="Document Processor API")


@app.exception_handler(DocumentProcessingError)
def document_processing_exception_handler(
    request: Request, exc: DocumentProcessingError
):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )


@app.exception_handler(EmptyDocumentError)
def document_empty_handler(request: Request, exc: EmptyDocumentError):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )


@app.exception_handler(UnsupportedFileError)
def unsupported_file_handler(request: Request, exc: UnsupportedFileError):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )


@app.exception_handler(DocumentNotFoundError)
def document_not_found_handler(request: Request, exc: DocumentNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"message": str(exc)},
    )


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


@app.get("/")
def root():
    return {"message": "Welcome to the Document Processor API!"}


@app.post("/documents/file", response_model=ProcessedDocumentResponse)
def process_document(request: ProcessFileRequest):

    processed_doc = service.process_file(
        doc_id=str(uuid4()), File_path=request.file_path
    )

    response = to_response(processed_doc)
    return response


@app.post("/documents/texts", response_model=ProcessedDocumentResponse)
def process_text(request: ProcessTextRequest):
    processed_doc = service.process_text(
        doc_id=str(uuid4()), text=request.text, title=request.title
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
