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

def cbc_encrypt(imgfile, filesize):
	key = b'Sixteen byte key'
	iv = b'Cixteen byte vec'
	aes_obj = AES.new(key, AES.MODE_ECB)
	frm = 0
	to = 16
	flag = 1
	enc = first_computation(imgfile[frm:to],iv,aes_obj) 
	frm +=16
	to += 16
	while flag :
		block = imgfile[frm : to]
		if len(block) < AES.block_size:
			block = pad_pkcs7(block)
			flag = 0
		block = bytes_xor(block, enc)
		with open("cbc_encrypted", "ab") as f:
			enc = aes_obj.encrypt(block)
			f.write(enc)
		frm += 16
		to +=16
	print("encryption completed")
		
	
def first_computation(block, iv, aes_obj):
	block = bytes_xor(block, iv)
	block = aes_obj.encrypt(block)
	with open("cbc_encrypted", "wb") as f:
		f.write(block)
	
	return block 



def cbc_decrypt(enfile, filesize):
	key = b'Sixteen byte key'
	iv = b'Cixteen byte vec'
	aes_obj = AES.new(key, AES.MODE_ECB)
	frm = 0
	to = 16
	enc = first_computation_d(enfile[frm:to], iv, aes_obj)
	frm += 16
	to += 16
	while to <= filesize :

		block = enfile[frm : to]
		
		decrypted = aes_obj.decrypt(block)
		
		decrypted = bytes_xor(decrypted, enc)

		if to == filesize :
			decrypted = unpad_pkcs7(decrypted)
		file = open("cbc_decrypted","ab")
		file.write(decrypted)
		file.close()
		enc = block
		frm += 16
		to +=16
	
	print("decryption completed")

def first_computation_d(block, iv, aes_obj):
	temp = block
	block = aes_obj.decrypt(block)
	decrypted = bytes_xor(block, iv)
	with open ("cbc_decrypted", "wb") as f:
		f.write(decrypted)

	return temp 

def sneak_in():
	with open("cbc_encrypted","rb") as f:
		contents = f.read()
	secondblock = contents[16:32]
	


if __name__ == "__main__":
    main()

