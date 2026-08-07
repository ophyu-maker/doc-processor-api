from document_processor.analyzer import TextAnalyzer
from document_processor.chunker import TextChunker
from document_processor.cleaner import TextCleaner
from document_processor.models import Document, ProcessedDocument


class DocumentProcessor:
    def __init__(
        self, cleaner: TextCleaner, analyzer: TextAnalyzer, chunker: TextChunker
    ) -> None:
        self.cleaner = cleaner
        self.analyzer = analyzer
        self.chunker = chunker

    def process(self, doc: Document) -> ProcessedDocument:
        cleaned_text = self.cleaner.clean_text(doc.text)
        analysis_results = self.analyzer.analyze(cleaned_text)
        text_chunks = self.chunker.chunk_text(cleaned_text)

        return ProcessedDocument(
            document=doc,
            cleaned_text=cleaned_text,
            analysis_results=analysis_results,
            text_chunks=text_chunks,
        )
