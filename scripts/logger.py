import logging
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

error_handler = logging.FileHandler(f'{script_dir}/../logs/error.log')
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

info_handler = logging.FileHandler(f'{script_dir}/../logs/info.log')
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(error_handler)
logger.addHandler(info_handler)
logger.addHandler(stream_handler)
