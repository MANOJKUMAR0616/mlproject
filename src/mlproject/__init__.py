import os
import sys
import logging

# Define logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define log directory and file path
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it does not exist
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Save logs to a file
        logging.StreamHandler(sys.stdout)   # Print logs to console
    ]
)

# Create a logger instance
logger = logging.getLogger("mlProjectLogger")
