import logging
import os
from pathlib import Path
class Logger:
    def __init__(self, log_file_path='logs/app.log'):        
        # path = Path(log_file_path)
        logging.basicConfig(
            filename=log_file_path,
            level=logging.DEBUG,
            format='%(asctime)s [%(levelname)s]: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    
    def log_event(self, message, level=logging.INFO):
        """Log an event with the specified log level."""
        logging.log(level, message)
        
    def log_exception(self, message):
        """Log an exception with traceback."""
        logging.exception(message)

if __name__ == "__main__":
    # Create an instance of FileLogger
    logger = Logger()
    try:
        # Simulate an exception
        raise ValueError("An example exception.")
    except ValueError as e:
        # Log the exception
        logger.log_exception("An exception occurred:")

    # Log an event
    logger.log_event("This is a sample log message.", level=logging.INFO)
        