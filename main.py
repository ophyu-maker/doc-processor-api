from src.document_processor.analyzer import TextAnalyzer
from src.document_processor.chunker import TextChunker
from src.document_processor.cleaner import TextCleaner
from src.document_processor.models import Document
from src.document_processor.processor import DocumentProcessor


def main():
    doc = Document.from_file(doc_id="1", file_path="data/input/sample.txt")
    document_processor = DocumentProcessor(
        cleaner=TextCleaner(),
        analyzer=TextAnalyzer(),
        chunker=TextChunker(chunk_size=5),
    )
    processed_doc = document_processor.process(doc)

    print(f"Document Title: {processed_doc.document.title}")
    print(f"Cleaned Text: {processed_doc.cleaned_text}")
    print(f"Analyzed: {processed_doc.analysis_results}")
    print(f"Text Chunks: {processed_doc.text_chunks}")


if __name__ == "__main__":
    main()
