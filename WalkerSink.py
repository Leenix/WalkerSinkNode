from SinkNode.Reader.WalkerReader import *
from SinkNode.Processor.ThingspeakProcessor import *
from SinkNode.Uploader.ThingspeakUploader import *
from SinkNode import *

from Queue import Queue

from sink_settings import *


class WalkerSink(object):
    def __init__(self, port=SERIAL_PORT):
        self.port = port


if __name__ == '__main__':
    start_logger()

    processor_queue = Queue()
    upload_queue = Queue()

    reader = WalkerReader(port=SERIAL_PORT, baud_rate=BAUD_RATE, logger_name=logger_name)
    reader.set_queue(processor_queue)

    processor = ThingspeakProcessor(channel_map=WALKER_CHANNEL_MAP, key_map=WALKER_KEY_MAP)
    processor.set_inbox(processor_queue)
    processor.set_outbox(upload_queue)

    uploader = ThingspeakUploader()
    uploader.set_queue(upload_queue)

    sink = SinkNode(reader, processor, uploader)
    sink.run()
