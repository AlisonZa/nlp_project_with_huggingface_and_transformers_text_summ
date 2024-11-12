import os
import sys
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
logs_path = os.path.join(PROJECT_ROOT, "logs")

# Create the logs directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Set up logging
file_handler = logging.FileHandler(LOG_FILE_PATH)
console_handler = logging.StreamHandler(sys.stdout)

logging.basicConfig(
    format="[ %(asctime)s ] - %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[file_handler, console_handler]
)

logger = logging.getLogger("summarizerlogger")

if __name__ == "__main__":
    logger.info("Logging has started")
