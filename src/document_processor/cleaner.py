from document_processor.exceptions import EmptyDocumentError


class TextCleaner:
    def __init__(self):
        pass

    def clean_text(self, text: str) -> str:
        """
        Cleans the input text by removing unwanted characters and formatting.

        Args:
            text (str): The input text to be cleaned."""
        cleaned_text = " ".join(text.split())  # remove spaces.

        if not cleaned_text:
            raise EmptyDocumentError("The document contains no usable text.")

        return cleaned_text
