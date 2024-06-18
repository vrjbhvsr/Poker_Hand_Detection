import os
import sys
from Poker_Hand_Detector.exception import pokerException
from Poker_Hand_Detector.logger import logging

class s3operation:

    def sync_folder_to_s3(self, folder:str, bucket_name: str, bucket_folder_name:str)->None:
        """
        This function will sync the folder to s3 bucket
        """
        try:
            command: str = (f" aws s3 cp sync {folder} s3://{bucket_name}/{bucket_folder_name}")
            os.system(command)
        except Exception as e:
            raise pokerException(e,sys)
        


    def sync_s3_to_folder(self, folder:str, bucket_name: str, bucket_folder_name:str)->None:
        """
        This function will sync the folder to s3 bucket
        """
        try:
            command:str = f"aws s3 sync s3://{bucket_name}/{bucket_folder_name}/ {folder}"
            logging.info(folder)
            os.system(command)
        except Exception as e:
            raise pokerException(e,sys)