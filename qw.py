from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
import random

class Challenge():
    def __init__(self, type , encoded):
        self.type = type
        self.encoded = encoded

    def c_level(self,type,encoded):
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
