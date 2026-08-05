from src.document_processor.analyzer import TextAnalyzer
from src.document_processor.chunker import TextChunker
from src.document_processor.cleaner import TextCleaner
from src.document_processor.processor import DocumentProcessor
from src.document_processor.repository import DocumentRepository
from src.document_processor.service import DocumentService


def main() -> None:
    processor = DocumentProcessor(
        cleaner=TextCleaner(),
        analyzer=TextAnalyzer(),
        chunker=TextChunker(chunk_size=5),
    )
    repository = DocumentRepository(storage_dir="data/processed")

    service = DocumentService(repository=repository, processor=processor)
    processed_doc = service.process_file(
        doc_id="doc1", File_path="data/input/sample.txt"
    )
    print("Processed Document:")
    print("------")
    print(processed_doc)

    loaded_doc = service.get_processed_document(doc_id="doc1")
    print("Loaded Document:")
    print("------")
    print(loaded_doc)


if __name__ == "__main__":
    main()
