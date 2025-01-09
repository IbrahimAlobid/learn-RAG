from enum import Enum

class ResponseSignal(Enum):
    FILE_VALIDATED_SUCCESS = "fail_validate_successfully"
    FAILE_TYPE_NOT_SPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    PROCESSING_SUCCESS = "processing_success"
    PROCESSING_FAILED = "processing_failed"
    