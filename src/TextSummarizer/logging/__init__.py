import os
import sys
import logging
from datetime import datetime

logging_str ="[%(asctime)s: %(levelname)s: %(module)s: %(lineno)s: %(message)s]"
LOGS_DIR = "logs"
LOG_FILENAME = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
log_filepath = os.path.join(LOGS_DIR,LOG_FILENAME)
os.makedirs(LOGS_DIR, exist_ok=True)

logging.basicConfig(level=logging.INFO, 
                    format=logging_str,
                    handlers=[logging.FileHandler(log_filepath),
                              logging.StreamHandler(sys.stdout)
                    ]
                    )
logger = logging.getLogger("TextSummarizationLogger")