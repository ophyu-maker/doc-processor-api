class DocumentProcessingError(Exception):
    """Base exception for document-processing errors."""


class EmptyDocumentError(DocumentProcessingError):
    """Raised when a document contains no usable text."""


class UnsupportedFileError(DocumentProcessingError):
    """Raised when a file type is unsupported."""


class DocumentNotFoundError(DocumentProcessingError):
    """Raised when a document cannot be found."""
