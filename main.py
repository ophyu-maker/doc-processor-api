from src.document_processor.analyzer import TextAnalyzer
from src.document_processor.chunker import TextChunker
from src.document_processor.cleaner import TextCleaner
from src.document_processor.models import Document
from src.document_processor.processor import DocumentProcessor
from src.document_processor.repository import DocumentRepository


def main():
    doc = Document.from_file(doc_id="1", file_path="data/input/sample.txt")
    document_processor = DocumentProcessor(
        cleaner=TextCleaner(),
        analyzer=TextAnalyzer(),
        chunker=TextChunker(chunk_size=5),
    )
    processed_doc = document_processor.process(doc)

    repository = DocumentRepository(storage_dir="data/processed")
    repository.save_document(processed_doc)

    loaded_doc = repository.get_document(document_id="1")

    print(loaded_doc)


if __name__ == "__main__":
    main()
