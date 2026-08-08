from document_processor.repository import DocumentRepository


def test_document_repository(tmp_path):
    repository = DocumentRepository(storage_dir=tmp_path)
