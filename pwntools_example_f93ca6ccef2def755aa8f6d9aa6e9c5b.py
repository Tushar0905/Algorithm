from pwn import * # pip install pwntools
import json
from rt import *
r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv()
while(True):
    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    obj=Challenge(received["type"],received["encoded"])



    to_send = {
        "decoded": obj
    }
    json_send(to_send)

    received=json_recv()
