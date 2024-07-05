import os
import sys
from Poker_Hand_Detector.logger import logging 
from Poker_Hand_Detector.exception import pokerException
from ultralytics import YOLO 
import numpy as np
from Poker_Hand_Detector.constant.training_pipeline import *
from Poker_Hand_Detector.entity.config_entity import DataIngestionConfig, CardRecognizerConfig
from Poker_Hand_Detector.entity.artifact_entity import DataIngestionArtifact, CardRecognizerArtifact
from Poker_Hand_Detector.utils.main_utils import write_yaml_file
import shutil

class CardRecognizer:
    def __init__(self, config: CardRecognizerConfig, artifact: DataIngestionArtifact):
        self.config = config
        self.artifact = artifact
        self.DIconfig = DataIngestionConfig()


    def create_data_yaml(self):
        data_yaml = {
            "train": os.path.join(self.DIconfig.train_data_path, "images"),
            "val": os.path.join(self.DIconfig.val_data_path, "images"),
            "test": os.path.join(self.DIconfig.test_data_path, "images"),
            "nc": self.config.num_classes,
            "names": self.config.names
        }

        write_yaml_file(self.config.yaml_file, data_yaml)

    def model_training(self):
        try:
            logging.info("Training the model")
            self.create_data_yaml()

            # Initialize the model
            model = YOLO(self.config.weights)

            # Train the model
            model.train(data=self.config.yaml_file, epochs=self.config.epochs, batch=self.config.batch_size, imgsz=self.config.image_size, plots=self.config.plots)
            logging.info("Model trained successfully")
            # Save the model
            os.makedirs(self.config.output_dir, exist_ok=True)
            model_best_weight_path = os.path.join(self.config.output_dir, "hand_detector.pt")
            CRartifacts: CardRecognizerArtifact = CardRecognizerArtifact(model_best_weights="Poker_Hand_Detection/runs/detect/train2/weights/best.pt")
            model.save(model_best_weight_path)
            logging.info("Model saved successfully")
            return CRartifacts
        
        except Exception as e:
            raise pokerException(e, sys) from e