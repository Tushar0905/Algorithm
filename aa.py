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

count=0
received = json_recv()
while(True):
    print("Received type: ")
    print(type)
    print("Received encoded value: ")
    try:
        print(received["encoded"])
    except Exception as e:
        if type=='flag':
            return

    print(count)
    count+=1
    obj=Challenge(received["type"],received["encoded"])
    inputji=obj.challenge(received["type"],received["encoded"])
    print(inputji)


    to_send = {
        "decoded": inputji
    }
    json_send(to_send)

    received=json_recv()
