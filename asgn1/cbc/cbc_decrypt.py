# decrypt
# xor
# write

from mylib import *

def main():
	print("Hello World!")

	with open("cbc_encrypted","rb") as f:
		enfile = f.read()
		
	cbc_decrypt(enfile, len(enfile))

def cbc_decrypt(enfile, filesize):
	key = b'Sixteen byte key'
	iv = b'Cixteen byte vec'
	aes_obj = AES.new(key, AES.MODE_ECB)
	frm = 0
	to = 16
	enc = first_computation(enfile[frm:to], iv, aes_obj)
	frm += 16
	to += 16
	while to <= filesize :
		block = enfile[frm : to]
		
		decrypted = aes_obj.decrypt(block)
		
		decrypted = bytes_xor(decrypted, enc)

		if to == filesize :
			decrypted = unpad_pkcs7(decrypted)
		file = open("cbc_decrypted.bmp","ab")
		file.write(decrypted)
		file.close()
		enc = block
		frm += 16
		to +=16
	
	print("decryption completed")

def first_computation(block, iv, aes_obj):
	temp = block
	block = aes_obj.decrypt(block)
	decrypted = bytes_xor(block, iv)
	with open ("cbc_decrypted.bmp", "wb") as f:
		f.write(decrypted)

	return temp 
	


if __name__ == "__main__":
    main()
