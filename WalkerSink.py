from Reader.WalkerReader import *
from Processor.ThingspeakProcessor import *
from Uploader.ThingspeakUploader import *
from SinkNode import *

from Queue import Queue

from sink_settings import *

class WalkerSink(object):
    def __init__(self, port=SERIAL_PORT):
        self.port = port


if __name__ == '__main__':
    reader = WalkerReader(port=SERIAL_PORT, baud=BAUD_RATE, logger_name=logger_name)
    processor = ThingspeakProcessor(channel_map=WALKER_CHANNEL_MAP, key_map=WALKER_KEY_MAP, logger_name=logger_name)
    uploader = ThingspeakUploader(logger_name=logger_name)

    sink = SinkNode
