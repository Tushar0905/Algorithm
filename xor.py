from pwn import xor
import codecs


# sys.setdefaultencoding('utf8')
word = "label"
h = bin(13)
a = [ord(b) for b in word]
for i in a :
    # bin(i)
    i = chr(i^13)
    print(i)

# res = 0

def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)

    return reduce(lambda x,y:x+y, lst)
def toStr(s):
    return s and chr(atoi(s[:2], base=16)) + toStr(s[2:]) or ''

def fun(a,res):
    # bytes_object = bytes.fromhex(a)
    # return bytes_object
    a = toHex(a)
    res = toHex(res)
    answ = a^res
    return toStr(answ)

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

# lis =
# print(hex(0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313 ^ 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e ^ 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e  ^ 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1 ^ 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf)
a = ((((0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313 ^ 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e)^ 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e)^0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1)^0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf)
# b = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
#print(a)
hex_string = hex(a)
hex_string = hex_string[2:]
bytes_object = bytes.fromhex(hex_string)
ascii_string = bytes_object.decode("ASCII")
print(ascii_string)
#
# a = (int(hex(0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e ^ 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1),16) + 0x200)
# a = (int(hex(0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313 ^ 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e),16) + 0x200)
# print(a)
# print((hex(0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313 ^ 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e),16))
# ans = hex(hex(hex(
#             int(hex(0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313 ^ 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e),16) ^
#             0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e) ^
#             0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1)^
#             0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf)
# # ans = 0
# # print(type(ans))
# # for i in lis :
# #     ans = hex(i^ans)
# # print(ans)
def single_char_xor(input_bytes, char_value):
    """Returns the result of each byte being XOR'd with a single value.
    """
    output_bytes = b''
    for byte in input_bytes:
        output_bytes += bytes([byte ^ char_value])
    return output_bytes

b = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
#print("============")
b = bytes.fromhex(b)
for i in range(256):
    c=single_char_xor(b, i)
    p = c.decode("ASCII","ignore")
    # print(p)
    if p[:7] == 'crypto{':
        print(p)


# hex_string = hex(b)
# hex_string = hex_string[2:]
# bytes_object = bytes.fromhex(hex_string)
# ascii_string = bytes_object.decode("ASCII")
# print(ascii_string)
def binaryToDecimal(binary):

    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)

def decimalToBinary(n):
    i= ''
    if(n > 1):
        decimalToBinary(n//2)
        i= i + 'n%2'



# l= '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
# res="{0:08b}".format(int(l, 16))
# res=(int(res))
# # print(res)
# # print(type(res))
# #
# for i in range(2**8):
#     j="{0:08b}".format(int(str(i), 16))
#     c=int(res)^int(j)
#     c=str(c)
#     print(c)
#     if(c[0:7]=="crypto{"):
#         print(c)



# for i  in range
#print(l)
# bytes_object = bytes.fromhex(l)
# ascii_string = bytes_object.decode("ASCII")
# print(ascii_string)
#m= bytes.fromhex(l)
# print(m)
# m=decimalToBinary(l)
# print(decimalToBinary(l))
# print(binaryToDecimal(m))
# for i in range(2**32):
#     c=decimalToBinary(l)^decimalToBinary(i)
#     d=binaryToDecimal(c)
#     hex_string = hex(d)
#     hex_string = hex_string[2:]
#     bytes_object = bytes.fromhex(hex_string)
#     q = bytes_object.decode("ASCII")
#     print(q)

    #print(q)
    # if q[:7] == 'crypto{':
    #     print(q)
