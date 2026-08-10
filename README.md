# Document Processor API

A small backend project built with **Python** and **FastAPI** that uses software engineering concepts such as modular design, service/repository architecture, validation, exception handling, logging, testing, and Git-based development.

The API accepts text or a local text file, cleans and analyzes the content, splits it into chunks, and stores the processed result as JSON.

## Tech Stack

- Python 3.12
- FastAPI
- Pydantic
- Pytest
- uv
- ruff
- Git / GitHub

## Features

- Process raw text
- Process `.txt` and `.md` files
- Normalize whitespace
- Analyze text statistics
  - character count
  - word count
  - sentence count
  - unique word count
- Split text into configurable word-based chunks
- Save processed documents as JSON
- Retrieve processed documents by ID
- Delete processed documents
- Pydantic request/response validation
- Custom exception handling
- Application logging
- Unit and integration testing

## Project Architecture

```text
API Request
    ↓
FastAPI Route
    ↓
Pydantic Schema
    ↓
DocumentService
    ↓
DocumentProcessor
    ├── TextCleaner
    ├── TextAnalyzer
    └── TextChunker
    ↓
DocumentRepository
    ↓
JSON Storage
```

# Learning Goal

This project was created to practice building a Python backend using a structured software-engineering approach rather than putting all application logic in one file.
Key concepts practiced include:
- Python modules and packages
- Dataclasses
- Object-oriented programming
- Dependency injection
- Separation of concerns
- Service and repository patterns
- JSON serialization
- Pydantic validation
- REST API development with FastAPI
- HTTP status codes and exception handling
- Logging
- Unit and integration testing
- Git branching and version control
