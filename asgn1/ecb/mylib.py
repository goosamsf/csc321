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
		
def ecb_encrypt(imgfile, filesize):
	key = b'Sixteen byte key'
	aes_obj = AES.new(key, AES.MODE_ECB)
	frm = 0
	to = 16
	flag = 1 
	while flag :
		block = imgfile[frm : to]
		if len(block) < AES.block_size:
			block = pad_pkcs7(block)
			flag = 0
		file = open("encrypted","ab")
		file.write(aes_obj.encrypt(block))
		file.close()
		frm += 16
		to +=16
	print("encryption completed")


def ecb_decrypt(enfile, filesize):
	key = b'Sixteen byte key'
	aes_obj = AES.new(key, AES.MODE_ECB)
	frm = 0
	to = 16
	while to <= filesize :
		block = enfile[frm : to]
		block = aes_obj.decrypt(block)	
		if to == filesize :
			block = unpad_pkcs7(block)
		file = open("decrypted","ab")
		file.write(block)
		file.close()
		frm += 16
		to +=16
	
	print("decryption completed")
		
	




