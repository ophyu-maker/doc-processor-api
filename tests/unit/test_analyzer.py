from document_processor.analyzer import TextAnalyzer


def test_text_analyzer():
    analyzer = TextAnalyzer()
    result = analyzer.analyze("This is a test sentence.")
    assert result.word_count == 5
    assert result.sentence_count == 1
    assert result.char_count == 24
    assert result.unique_words == 5
