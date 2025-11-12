import logging
import logging.config
import os
from datetime import datetime

def logger_config_dict(log_file_name):

    """Function to return logging configuration dictionary"""
    log_config = {
        'version':1,
        'formatters':{
            'file_formatter':{
                'format': '%(asctime)s - %(name)s - %(levelname)s - location: %(pathname)s - line: %(lineno)d - %(message)s',
            },
            'console_formatter':{
                'format': '%(levelname)s - location: %(filename)s - line: %(lineno)d - %(message)s'
            },
            'exception_formatter':{
                'format': '%(message)s'
            }

        },
        'handlers':{
            'file':{
                'class':'logging.FileHandler',
                'formatter':'file_formatter',
                'level':'INFO',
                'filename': log_file_name
            },
            'console':{
                'class':'logging.StreamHandler',
                'formatter':'console_formatter',
                'level':'DEBUG'
            },
            'exception_file':{
                'class':'logging.FileHandler',
                'formatter':'exception_formatter',
                'level':'ERROR',
                'filename': log_file_name
            }

        },
        'loggers':{
            'custom_logger':{
                'handlers':['file','console'],
                'level':'DEBUG',
                'propagate':True
            },
            'exception_logger':{
                'handlers': ['exception_file'],
                'level':'INFO',
                'propagate':True
            }
        }
    }

    return log_config


class CustomLogger:
    def __init__(self, log_dir_name = 'logs'):

        ## Defining log directory and file paths        
        self.log_dir_path = os.path.join(os.getcwd(),log_dir_name)
        self.log_file_name = f'Log_{datetime.now().strftime('%H_%M_%S__%d_%m_%Y')}.log'
        self.log_file_path = os.path.join(self.log_dir_path, self.log_file_name)

        #creating log directory if it doesn't exist        
        os.makedirs(self.log_dir_path, exist_ok=True)
        logging.config.dictConfig(logger_config_dict(self.log_file_path))

    def get_logger(self, name):
        return logging.getLogger(name)


if __name__ == "__main__":
    logger = CustomLogger().get_logger('custom_logger')
    logger.info('this is working fine')
    print(os.getcwd())