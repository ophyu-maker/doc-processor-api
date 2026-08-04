from src.document_processor.models import TextStatistics


class TextAnalyzer:
    def analyze(self, text: str) -> TextStatistics:
        # Perform text analysis here
        char_count = len(text)
        word_count = len(text.split())
        sentence_count = text.count(".") + text.count("!") + text.count("?")
        unique_words = len(set(text.lower().split()))
        return TextStatistics(
            char_count=char_count,
            word_count=word_count,
            sentence_count=sentence_count,
            unique_words=unique_words,
        )
