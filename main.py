from src.document_processor.cleaner import TextCleaner
from src.document_processor.models import Document


def main():
    doc = Document.from_file(doc_id="1", file_path="data/input/sample.txt")
    cleaner = TextCleaner()
    cleaned_text = cleaner.clean_text(doc.text)

    print(f"Original Text: {doc.text}")
    print(f"Cleaned Text: {cleaned_text}")


if __name__ == "__main__":
    main()
