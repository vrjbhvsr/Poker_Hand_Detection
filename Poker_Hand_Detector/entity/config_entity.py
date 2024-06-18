import os
from dataclasses import dataclass
from Poker_Hand_Detector.constant.training_pipeline import *

@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.s3_data_folder: str= S3_DATA_FOLDER
        self.bucket_name: str = BUCKET_NAME
        self.artifact_dir: str = os.path.join(ARTIFACT_DIR)
        self.data_path: str = os.path.join(self.artifact_dir, self.s3_data_folder)
        self.train_data_path: str = os.path.join(self.data_path,"train")
        self.val_data_path: str = os.path.join(self.data_path,"valid")
        self.test_data_path: str = os.path.join(self.data_path,"test")

@dataclass
class CardRecognizerConfig:
        project_dir: str = os.getcwd()
        yaml_file: str = os.path.join(project_dir,"data.yaml")
        output_dir: str = os.path.join(OUTPUT_DIR)
        weights = WEIGHTS
        num_classes = NUM_CLASSES
        batch_size = BATCH_SIZE
        epochs = EPOCHS
        plots = PLOT
        names = NAMES
        image_size = IMAGE_SIZE

@dataclass
class HandDetectorConfig:
    confidence: float = CONFIDENCE
    classnames= NAMES
