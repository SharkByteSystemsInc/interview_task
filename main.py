import zmq
import json, os
import socket
import time
with open("config.json") as f:
    config = json.load(f)
def get_address(host, port):
    addr = f"tcp://{host}:{port}"
    print(addr)
    return addr

IS_FIRST = int(os.environ.get("INITIALIZER", "0"))

MAX = int(os.environ.get("MAX_VALUE", "256"))
HOSTNAME_PUB = config[socket.gethostname()]["PUB"]["HOST"]
HOSTNAME_SUB = config[socket.gethostname()]["SUB"]["HOST"]

PUB_PORT = config[socket.gethostname()]["PUB"]["PORT"]
SUB_PORT = config[socket.gethostname()]["SUB"]["PORT"]

context = zmq.Context()
pub_socket = context.socket(zmq.PUB)
print("Connecting publisher")

pub_socket.bind(get_address(HOSTNAME_PUB, PUB_PORT))
time.sleep(5)

sub_socket = context.socket(zmq.SUB)
sub_socket.setsockopt(zmq.SUBSCRIBE, b"")
print("Connecting subscriber to publisher")

sub_address = get_address(HOSTNAME_SUB, SUB_PORT)
sub_socket.connect(sub_address)

i = 0


while i < MAX:
    print(f"Sending {i}")
    pub_socket.send(bytes([i]))
    try:
        print(sub_socket.recv(zmq.DONTWAIT))
    except zmq.Again as a:
        time.sleep(0.1)
        continue
    i +=1
