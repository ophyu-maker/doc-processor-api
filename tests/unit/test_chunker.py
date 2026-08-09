from document_processor.chunker import TextChunker


def test_text_chunker():
    chunker = TextChunker(chunk_size=3)
    result = chunker.chunk_text("one two three four five six seven")
    assert result == [
        "one two three",
        "four five six",
        "seven",
    ]
