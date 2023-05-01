from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os, hashlib


BINARY=2
BYTE=8

#modified_sha256 : takes string and generate sha256 hexadecimal digest. truncate parameter control the number of bytes. if truncate is not specified, go its default value, 32bytes(256bits)
def modified_sha256(str_in , truncate=256):
    #str_in = str_in.encode()
    if truncate == 256:
        return hashlib.sha256(str_in).hexdigest()
    else:
        return hashlib.sha256(str_in).hexdigest()[:int(truncate/4)]
    
def str2bin(string):
	retstr =""
	for i in string:
		retstr+=bin(ord(i))[BINARY:].zfill(BYTE)
	return retstr

def check_collide(numbits):
    table = {}
    val_range = pow(2,numbits)

    ran_approx = int(pow(val_range, 0.5))
    print(f"search range is about 0 to {ran_approx}")
    for i in range(ran_approx):
        bindata = os.urandom(16)
        digest = modified_sha256(bindata,numbits)
        if(digest in table):
            print("collide")
        else:
            table[digest] = True


