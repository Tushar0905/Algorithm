#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, long_to_bytes
# from utils import listener # this is cryptohack's server-side module and not part of python
import base64
import codecs
import random

FLAG = "crypto{????????????????????}"
ENCODINGS = [
    "base64",
    "hex",
    "rot13",
    "bigint",
    "utf-8",
]
with open('/usr/share/dict/words') as f:
    WORDS = [line.strip().replace("'", "") for line in f.readlines()]


class Challenge():
    def __init__(self,type,encoded):
        self.type = type
        self.encoded = encoded
        self.stage = 0

    def create_level(self,type,encoded):
        self.stage += 1
        decoded=''
        if type == "base64":
            decoded = base64.b64decode(encoded)
            decoded = str(decoded).split("'")[1]
            print(decoded)
        elif type == "hex":
            decode_hex = codecs.getdecoder("hex_codec")
            decoded =  decode_hex(encoded)[0]
            decoded = str(decoded).split("'")[1]
        elif type == "rot13":
            decoded = codecs.decode(encoded, 'rot_13')
        elif type == "bigint":
            encoded = encoded[2:]
            bytes_object = bytes.fromhex(encoded)
            decoded = bytes_object.decode("ASCII")
        elif type == "utf-8":
            for b in encoded :
                decoded += chr(b)
        return decoded

    #
    # This challenge function is called on your input, which must be JSON
    # encoded
    #
    def challenge(self,type,encoded):
        if self.stage == 0:
            return self.create_level(type,encoded)
        elif self.stage == 100:
            self.exit = True
            return {"flag": FLAG}

        if self.challenge_words == your_input["decoded"]:
            return self.create_level()

        return {"error": "Decoding fail"}


# listener.start_server(port=13377)
