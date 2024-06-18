import sys
from Poker_Hand_Detector.Components.data_ingestion import DataIngestion
from Poker_Hand_Detector.Components.card_recognition import CardRecognizer
from Poker_Hand_Detector.Components.Displayer import Display
from Poker_Hand_Detector.entity.artifact_entity import DataIngestionArtifact,CardRecognizerArtifact
from Poker_Hand_Detector.entity.config_entity import DataIngestionConfig,CardRecognizerConfig,HandDetectorConfig
from Poker_Hand_Detector.exception import pokerException
from Poker_Hand_Detector.logger import logging

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config= DataIngestionConfig()
    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Starting data ingestion")

        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Train, valid and test dataset retrieved from s3")

            logging.info("data ingestion has completed")

            return data_ingestion_artifact
        
        except Exception as e:
            raise pokerException(e,sys)
        
    def start_model_training(self):
        try:
        
            logging.info("Starting model training")
            train = CardRecognizer(config=CardRecognizerConfig, artifact=DataIngestionArtifact)
            train.model_training()
            logging.info("Model training has completed")

        except Exception as e:
            raise pokerException(e,sys)
        
    def start_Displaying(self):
        try:
            logging.info("Camera started")
            display = Display(CR_artifact=CardRecognizerArtifact,config=HandDetectorConfig) 
            display.display_Video()
            logging.info("Stopping Display")

        except Exception as e:
            raise pokerException(e,sys)


if __name__ == "__main__":
    train_pipeline = TrainPipeline()
    #train_pipeline.start_data_ingestion()
    #train_pipeline.start_model_training()
    train_pipeline.start_Displaying()