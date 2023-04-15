from Crypto.Cipher import AES

def pad_pkcs7(block : bytes) -> bytes:
	blocksize = len(block)
	padbytes = 16 - blocksize
	multiple = padbytes
	padbytes = padbytes.to_bytes()
	padbytes = block + (padbytes * multiple)

	return padbytes





