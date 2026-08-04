class TextChunker:
    def __init__(self, chunk_size: int = 100) -> None:
        self.chunk_size = chunk_size

    def chunk_text(self, text: str) -> list[str]:
        word = text.split()
        chunks: list[str] = []

        for i in range(0, len(word), self.chunk_size):
            chunk = " ".join(word[i : i + self.chunk_size])
            chunks.append(chunk)

        return chunks
