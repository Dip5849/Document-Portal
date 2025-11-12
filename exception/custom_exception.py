import sys
import traceback
from logger.custom_logger import CustomLogger


class CustomException(Exception):
    def __init__(self, message, error_detail: sys):
        _,_,exc_tb = error_detail.exc_info()
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.line_no = exc_tb.tb_lineno
        self.message = message
        self.traceback_str = ''.join(traceback.format_exception(*error_detail.exc_info()))
    def __str__(self):
        return f"""
        Error occurred in script: {self.file_name}
        Line number: {self.line_no}
        Message: {self.message}
        Traceback: {self.traceback_str}
        """
    

if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        raise CustomException('Division by zero error occured', sys)