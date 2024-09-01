import os 
import logging
from datetime import datetime
from from_root import from_root


LOG_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(from_root(), 'log', LOG_file)

os.makedirs(log_path, exist_ok = True)

LOG_FILE_PATH = os.path.join(log_path, LOG_file)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)