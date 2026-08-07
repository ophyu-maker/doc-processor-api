from uuid import uuid4

from src.document_processor.analyzer import TextAnalyzer
from src.document_processor.chunker import TextChunker
from src.document_processor.cleaner import TextCleaner
from src.document_processor.processor import DocumentProcessor
from src.document_processor.repository import DocumentRepository
from src.document_processor.schemas import (
    ProcessedDocumentResponse,
    TextStatisticsResponse,
)
from src.document_processor.service import DocumentService

# def main() -> None:
#     processor = DocumentProcessor(
#         cleaner=TextCleaner(),
#         analyzer=TextAnalyzer(),
#         chunker=TextChunker(chunk_size=5),
#     )
#     repository = DocumentRepository(storage_dir="data/processed")

#     service = DocumentService(repository=repository, processor=processor)
#     processed_doc = service.process_file(
#         doc_id="doc1", File_path="data/input/sample.txt"
#     )
#     print("Processed Document:")
#     print("------")
#     print(processed_doc)

#     loaded_doc = service.get_processed_document(doc_id="doc1")
#     print("Loaded Document:")
#     print("------")
#     print(loaded_doc)


def main() -> None:
    processor = DocumentProcessor(
        cleaner=TextCleaner(),
        analyzer=TextAnalyzer(),
        chunker=TextChunker(chunk_size=5),
    )
    repository = DocumentRepository(storage_dir="data/processed")
    service = DocumentService(repository=repository, processor=processor)
    doc_id = str(uuid4())  # Generate a unique document ID for each request
    processed = service.process_file(doc_id=doc_id, File_path="data/input/sample.txt")

    response = ProcessedDocumentResponse(
        doc_id=processed.document.doc_id,
        title=processed.document.title,
        cleaned_text=processed.cleaned_text,
        analysis_results=TextStatisticsResponse(
            char_count=processed.analysis_results.char_count,
            word_count=processed.analysis_results.word_count,
            sentence_count=processed.analysis_results.sentence_count,
            unique_words=processed.analysis_results.unique_words,
        ),
        text_chunks=processed.text_chunks,
    )

    print(response.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
