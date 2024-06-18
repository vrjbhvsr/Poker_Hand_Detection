import os
from dataclasses import dataclass
from typing import List


@dataclass
class DataIngestionArtifact:
    train_file_path: str
    val_file_path: str
    test_file_path: str

@dataclass
class CardRecognizerArtifact:
    model_best_weights: str

