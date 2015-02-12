import logging
from logging.handlers import TimedRotatingFileHandler

__author__ = 'Leenix'

"""
Logger settings
"""
logger_level = logging.INFO
logger_name = "Walker"
log_filename = "Walker.log"
log_format = "%(asctime)s - %(levelname)s - %(message)s"

def start_logger():
    logger = logging.getLogger(logger_name)
    logger.setLevel(logger_level)

    # Console Logging
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(console_handler)

    # File Logging
    if log_filename:
        file_handler = TimedRotatingFileHandler()
        file_handler.setFormatter(logging.Formatter(log_format))
        file_handler.setLevel(logging.INFO)
        logger.addHandler(file_handler)

"""
Reader settings
"""
SERIAL_PORT = "COM3"
BAUD_RATE = 57600


"""
Processor settings
"""

WALKER_KEY_MAP = {
    "air_temp": "field1",
    "wall_temp": "field2",
    "surface_temp": "field3",
    "case_temp": "field4",
    "humidity": "field5",
    "illuminance": "field6",
    "sound": "field7",
    "battery": "field8"
}

WALKER_CHANNEL_MAP = {
    "stalker8": "GKNS6EINCZ9T5YOU",
    "stalker9": "VTIXOT8ZHPV3IUL0",
    "stalker11": "NEFBTRTQPAGILRQW",
    "stalker12": "EGH6V54E93K7YBWU"
}