import logging
import os
from datetime import datetime

LOG_DIR = 'logs'
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, f'unsafe_interactions_{datetime.now().strftime("%Y%m%d")}.log'),
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def log_unsafe_input(input_text, reason):
    logger.warning(f'Unsafe input detected: {input_text} - Reason: {reason}')

def log_unsafe_output(output_text, reason):
    logger.warning(f'Unsafe output detected: {output_text} - Reason: {reason}')