from os import getenv as env
from socket import gethostname
from time import sleep
from typing import Optional

from logger import logger

import zmq


IS_FIRST: bool = bool(int(env('INITIALIZER', 0)))
MAX: int = int(env('MAX_VALUE', 10))
HOST: str = gethostname()
PUB_SERVER: str = env('PUB_SERVER', 'tcp://*:5555')
SUB_CLIENT: Optional[str] = env('SUB_CLIENT')
context = zmq.Context()

logger.info(
    f'Creating publisher server `{PUB_SERVER}` socket '
    'type: ZMQ.PUB'
)
pub_socket = context.socket(zmq.PUB)
pub_socket.bind(PUB_SERVER)

logger.info(
    f'Connecting subscriber client `{HOST}` to {SUB_CLIENT} '
    f'max: {MAX} socket type: ZMQ.SUB'
)
sub_socket = context.socket(zmq.SUB)
sub_socket.setsockopt(zmq.SUBSCRIBE, b'')
sub_socket.connect(SUB_CLIENT)

message: int = 0

sleep(0.11)

while message < MAX:

    if IS_FIRST:
        pub_socket.send(message.to_bytes(2, 'big'))
        logger.debug(f'Sent {message}')
        IS_FIRST = False

    try:
        resp = sub_socket.recv()
        message = int.from_bytes(resp, 'big')
        log_msg = f'Received: {message}'
        message += 1

        if message and message <= MAX:
            pub_socket.send(message.to_bytes(2, 'big'))
            log_msg += f' Sent {message}'

    except zmq.Again:
        continue
    except Exception as e:
        logger.error(e)

    logger.debug(log_msg)
