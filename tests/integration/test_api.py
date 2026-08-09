from fastapi.testclient import TestClient
from document_processor.api import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Document Processor API!"}


def test_text():
    response = client.post(
        "/documents/texts",
        json={
            "title": "Test Document",
            "text": " Python is great. Python is easy to learn. ",
        },
    )

    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "Test Document"
    assert data["cleaned_text"] == "Python is great. Python is easy to learn."
    assert "doc_id" in data
    assert "analysis_results" in data
    assert "text_chunks" in data


def test_file(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text(
        "Python is great. FastAPI is useful.",
        encoding="utf-8",
    )

    response = client.post(
        "/documents/file",
        json={
            "file_path": str(test_file),
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "test.txt"
    assert data["cleaned_text"] == "Python is great. FastAPI is useful."
    assert "doc_id" in data
    assert "analysis_results" in data
    assert "text_chunks" in data


def test_create_and_get_document():
    create_response = client.post(
        "documents/texts",
        json={
            "title": "My Document",
            "text": " Python is great. Python is easy to learn. ",
        },
    )

    assert create_response.status_code == 200
    created_response = create_response.json()
    doc_id = created_response["doc_id"]

    get_document = client.get(f"/documents/{doc_id}")
    assert get_document.status_code == 200
    retrieved_document = get_document.json()
    assert retrieved_document["doc_id"] == doc_id
    assert retrieved_document["title"] == "My Document"


def test_delete_document():
    create_response = client.post(
        "documents/texts",
        json={
            "title": "My Document",
            "text": " Python is great. Python is easy to learn. ",
        },
    )

    assert create_response.status_code == 200
    created_response = create_response.json()
    doc_id = created_response["doc_id"]

    delete_document = client.delete(f"/documents/{doc_id}")
    assert delete_document.status_code == 200
    assert delete_document.json() == {
        "message": f"Processed document with ID '{doc_id}' has been deleted."
    }


def test_document_not_found():
    response = client.get("/documents/not_exists")
    assert response.status_code == 404


def test_empty_doc():
    create_response = client.post(
        "documents/texts",
        json={
            "title": "My Document",
            "text": "    ",
        },
    )

    assert create_response.status_code == 422


def test_file_not_found():
    response = client.post(
        "/documents/file",
        json={
            "file_path": "does_not_exist.txt",
        },
    )

    assert response.status_code == 404
