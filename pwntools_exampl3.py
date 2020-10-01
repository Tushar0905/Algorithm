from pwn import * # pip install pwntools
import json
from abc import *

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv()

print("Received type: ")
print(received["type"])
print("Received encoded value: ")
print(received["encoded"])

def cause_a_to_do_something():
    import abc
    obj=abc.Challenge()
    inputji= {"Received encoded value":received["encoded"]}
    decodedvalue =obj.challenge(inputji)
cause_a_to_do_something()

to_send = {
    "decoded": decodedvalue
}
json_send(to_send)

json_recv()
