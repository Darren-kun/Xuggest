import time

import logging
import sys

logger = logging.getLogger('analysis_log')

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

file_handler = logging.FileHandler('analysis_log.log')

file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler(sys.stdout)

console_handler.setFormatter(formatter)

logger.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


