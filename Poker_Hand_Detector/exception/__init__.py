import sys
from Poker_Hand_Detector.logger import logging

def error_meassage_detail(error, error_detail: sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = f"Error in script: {file_name}/n line number: {exc_tb.tb_lineno}: {str(error)}"

    return error_message

class pokerException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)

        self.error_message = error_meassage_detail(error_message, 
                                                   error_detail=error_detail)
        
    def __str__(self):
        return logging.error(self.error_message)
