from person_detection.logger import logging
from person_detection.exception import SignException
import sys
logging.info("welcome to the project")

try:
    a = 7/'9'
except Exception as e:
    raise SignException(e, sys) from e