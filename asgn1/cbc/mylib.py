from Crypto.Cipher import AES

def pad_pkcs7(block : bytes) -> bytes:
	blocksize = len(block)
	padbytes = 16 - blocksize
	multiple = padbytes
	padbytes = padbytes.to_bytes()
	padbytes = block + (padbytes * multiple)

	return padbytes

def unpad_pkcs7(block : bytes) -> bytes:
	padbytes = ord(block[-1:])
	if padbytes == 0 or padbytes > 16:
		raise Exception("Padding Error")
		return ""
	for i in block[16-padbytes : 16]:
		if i != padbytes:
			raise Exception("Padding Error")
			return ""
	strip = block[:-padbytes]

	return strip

def bytes_xor(byte1: bytes , byte2: bytes) -> bytes:
	ret = bytearray(b'')
	if(len(byte1) != 16 or len(byte2) != 16):
		raise Exception("Something Wrong in length of bytes")
		return ""

	for i in range(16):
		ret.append(byte1[i] ^ byte2[i])
	return bytes(ret)	


