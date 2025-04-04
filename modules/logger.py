
import logging
import os
from datetime import datetime

def setup_logger():
    """Sets up the logger with a structured folder system."""
    # Ensure base 'logs' folder exists
    logs_folder = "logs"
    os.makedirs(logs_folder, exist_ok=True)

    # Creating subfolder with current date and time
    time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_subfolder = os.path.join(logs_folder, time_stamp)
    os.makedirs(log_subfolder, exist_ok=True)

    # Log file path inside the new subfolder
    log_file = os.path.join(log_subfolder, "file.log")

    # Setup logging
    logging.basicConfig(
        filename=log_file,
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    return logging.getLogger()

# Initializing logger
logger = setup_logger()

if __name__ == "__main__":
    logger.info("Logger initialized successfully.")
