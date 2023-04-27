BYTE=8
BINARY=2
def str2bin(string):
	retstr =""
	for i in string:
		retstr+=bin(ord(i))[BINARY:].zfill(BYTE)
	return retstr
