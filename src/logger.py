import logging
import os 
from datetime import datetime

# Create log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define log directory and log file path
logs_directory = os.path.join(os.getcwd(), "log")
os.makedirs(logs_directory, exist_ok=True)  # Create the log directory if it doesn't exist
LOG_FILE_PATH = os.path.join(logs_directory, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Fixed format
    level=logging.INFO,
)

# Test logging
if __name__ == "__main__":
    logging.info("Logging has started")
