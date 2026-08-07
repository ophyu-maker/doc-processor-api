from pydantic import BaseModel, field_validator


class ProcessTextRequest(BaseModel):
    title: str
    text: str

    @field_validator("title", "text")
    @classmethod
    def validate_fields(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Field must not be empty.")
        return v


class TextStatisticsResponse(BaseModel):
    char_count: int
    word_count: int
    sentence_count: int
    unique_words: int


class ProcessedDocumentResponse(BaseModel):
    doc_id: str
    title: str
    cleaned_text: str
    analysis_results: TextStatisticsResponse
    text_chunks: list[str]
