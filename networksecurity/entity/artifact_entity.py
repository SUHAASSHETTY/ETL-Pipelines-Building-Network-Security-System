# The artifacts folder is a storage location inside your project where you keep intermediate or final outputs produced by your pipeline
# such as processed data, trained models, evaluation reports, etc. It helps in organizing and managing the results of your machine learning workflow.

from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str

@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str