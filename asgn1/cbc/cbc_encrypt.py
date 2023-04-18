from mylib import *
#1. Read File
#2. Create AES object
#3. Steps of Encryption:
#	1.xor
#	2.encrypt
#	3.write

def main():
	print("Hello World!")

	with open("../cp-logo.bmp","rb") as f:
		imgfile = f.read()
		
	cbc_encrypt(imgfile, len(imgfile))

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



if __name__ == "__main__":
    main()









