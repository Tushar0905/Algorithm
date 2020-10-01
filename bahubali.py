from pwn import * # pip install pwntools
import json
from qw import *
r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

received = json_recv()
for i in range(100):
    print(i)

    print("Received type: ")
    print(received["type"])
    if type == 'flag':
        print(received["encoded"])
    else :
        print("Received encoded value: ")
        print(received["encoded"])
        #print("type ",received["type"])
        obj=Challenge(received["type"],received["encoded"])

        inputji=obj.c_level(received["type"],received["encoded"])
        print(inputji)

        to_send = {
            "decoded": inputji
        }
        json_send(to_send)
        received = json_recv()
