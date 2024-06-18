import sys
from Poker_Hand_Detector.Configuration.s3_operation import s3operation
from Poker_Hand_Detector.entity.config_entity import DataIngestionConfig
from Poker_Hand_Detector.entity.artifact_entity import DataIngestionArtifact
from Poker_Hand_Detector.exception import pokerException
from Poker_Hand_Detector.logger import logging



class DataIngestion:
    def __init__(self,data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        self.s3 = s3operation()


    def get_data_from_s3(self):
        try:
            self.s3.sync_s3_to_folder(folder = self.data_ingestion_config.data_path,
                                      bucket_name= self.data_ingestion_config.bucket_name,
                                      bucket_folder_name= self.data_ingestion_config.s3_data_folder)
            
            logging.info("S3 Bucket has been synced to folder")
        except Exception as e:
            raise pokerException(e,sys)

    def initiate_data_ingestion(self):
        logging.info("Data ingestion has been initiated")
        try:
            self.get_data_from_s3()
            data_ingestion_artifact: DataIngestionArtifact = DataIngestionArtifact(
                train_file_path=self.data_ingestion_config.train_data_path,
                val_file_path= self.data_ingestion_config.val_data_path,
                test_file_path= self.data_ingestion_config.test_data_path)
            
            logging.info("Data ingestion completed successfully")
            return data_ingestion_artifact
        except Exception as e:
            raise pokerException(e,sys)