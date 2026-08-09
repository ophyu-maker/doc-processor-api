from document_processor.repository import DocumentRepository
from document_processor.models import Document, TextStatistics, ProcessedDocument


def test_save_document(tmp_path):
    repository = DocumentRepository(storage_dir=tmp_path)

    document = Document(doc_id="123", title="test.txt", text=" Python is great ")

    processed_document = ProcessedDocument(
        document=document,
        cleaned_text="Python is great",
        analysis_results=TextStatistics(
            char_count=15,
            word_count=3,
            sentence_count=1,
            unique_words=3,
        ),
        text_chunks=["Python", "is", "great"],
    )

    repository.save_document(processed_document)

    saved_file = tmp_path / "123.json"
    assert saved_file.exists()


def test_get_document(tmp_path):
    repository = DocumentRepository(storage_dir=tmp_path)

    document = Document(doc_id="123", title="test.txt", text=" Python is great ")

    processed_document = ProcessedDocument(
        document=document,
        cleaned_text="Python is great",
        analysis_results=TextStatistics(
            char_count=15,
            word_count=3,
            sentence_count=1,
            unique_words=3,
        ),
        text_chunks=["Python", "is", "great"],
    )

    repository.save_document(processed_document)

    loaded_document = repository.get_document(document.doc_id)

    assert loaded_document.document.doc_id == "123"
    assert len(loaded_document.text_chunks) == 3
    assert loaded_document.cleaned_text == "Python is great"


def test_delete_document(tmp_path):
    repository = DocumentRepository(storage_dir=tmp_path)

    document = Document(doc_id="123", title="test.txt", text=" Python is great ")

    processed_document = ProcessedDocument(
        document=document,
        cleaned_text="Python is great",
        analysis_results=TextStatistics(
            char_count=15,
            word_count=3,
            sentence_count=1,
            unique_words=3,
        ),
        text_chunks=["Python", "is", "great"],
    )

    repository.save_document(processed_document)
    saved_file = tmp_path / "123.json"

    repository.delete_document(document.doc_id)
    assert not saved_file.exists()
