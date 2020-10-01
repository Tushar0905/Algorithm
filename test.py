import crypto
import Crypto.Util

l= 0x0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
# print(l[2:])
# res=bin("{0:08b}".format(int(l[2:], 16)))
print(l)
# print(type(l))
z=2**2
hex_string = hex(l)
#print(type(hex_string))
# hex_string = hex_string[2:]
# print(len(hex_string))
bytes_object = bytes.fromhex(str(l))
al = bytes_object.decode("ASCII","ignore")
print(al)
for i in range(z):
    no=(l^i)
    hex_string = hex(no)
    #print(type(hex_string))
    # hex_string = hex_string[2:]
    # print(len(hex_string))
    bytes_object = bytes.fromhex(str(no))
    ascii_string = bytes_object.decode("ASCII","ignore")
    #print(ascii_string)
    if ascii_string[:7]=='crypto{':
        print(ascii_string)
        break
    if i==(z-1):
        print(ascii_string)
