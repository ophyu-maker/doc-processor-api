from document_processor.service import DocumentService
from document_processor.analyzer import TextAnalyzer
from document_processor.chunker import TextChunker
from document_processor.cleaner import TextCleaner
from document_processor.models import Document
from document_processor.processor import DocumentProcessor
from document_processor.repository import DocumentRepository


def test_process_text(tmp_path):
    processor = DocumentProcessor(
        cleaner=TextCleaner(),
        analyzer=TextAnalyzer(),
        chunker=TextChunker(chunk_size=5),
    )

    repository = DocumentRepository(storage_dir=tmp_path)
    service = DocumentService(repository=repository, processor=processor)

    result = service.process_text(
        doc_id="123", title="test.txt", text=" Python is great "
    )

    assert result.cleaned_text == "Python is great"
    assert (tmp_path / "123.json").exists


def test_process_file(tmp_path):

    input_file = tmp_path / "test.txt"
    input_file.write_text(" Python is great ")

    storage_dir = tmp_path / "processed"

    processor = DocumentProcessor(
        cleaner=TextCleaner(),
        analyzer=TextAnalyzer(),
        chunker=TextChunker(chunk_size=5),
    )

    repository = DocumentRepository(storage_dir=storage_dir)
    service = DocumentService(repository=repository, processor=processor)

    result = service.process_file(doc_id="123", file_path=input_file)

    assert result.cleaned_text == "Python is great"
    assert result.document.doc_id == "123"
