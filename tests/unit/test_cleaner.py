import pytest
from document_processor.cleaner import TextCleaner
from document_processor.exceptions import EmptyDocumentError


def test_text_cleaner():
    cleaner = TextCleaner()
    text = "This is a sample text with   extra spaces.  "
    cleaned_text = cleaner.clean_text(text)
    assert cleaned_text == "This is a sample text with extra spaces."


def test_empty_document_error():
    cleaner = TextCleaner()
    with pytest.raises(EmptyDocumentError):
        cleaner.clean_text("   ")  # Input with only spaces should raise an error
