from document_processor.analyzer import TextAnalyzer
from document_processor.chunker import TextChunker
from document_processor.cleaner import TextCleaner
from document_processor.models import Document
from document_processor.processor import DocumentProcessor


def test_document_processor():
    processor = DocumentProcessor(
        cleaner=TextCleaner(),
        analyzer=TextAnalyzer(),
        chunker=TextChunker(chunk_size=2),
    )

    document = Document(doc_id="1", title="This is title", text=" This is text ")

    result = processor.process(document)

    assert result.document.doc_id == "1"
    assert result.document.text == " This is text "
    assert result.cleaned_text == "This is text"
    assert result.analysis_results.word_count == 3
    assert len(result.text_chunks) == 2
