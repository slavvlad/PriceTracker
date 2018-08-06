import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

dir_path = os.path.dirname(os.path.realpath(__file__))
# create a file handler
handler = logging.FileHandler(dir_path +'\Log\Tracking.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

#logger.info('Hello baby')