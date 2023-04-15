from mylib import *

#1. Read File
#2. Create AES object
#3. Steps of Encryption:
#	1. Fetch 16 bytes
#	2. Check if padding is needed
#	3. Encrypt
#	4. write it to encrypting file
#	5. Repeat endindex gets greater than length of the file



def main():
	print("Hello World!")

	with open("../cp-logo.bmp","rb") as f:
		imgfile = f.read()
		
	ecb_encrypt(imgfile, len(imgfile))

def ecb_encrypt(imgfile, filesize):
	key = b'Sixteen byte key'
	aes_obj = AES.new(key, AES.MODE_ECB)
	frm = 0
	to = 16
	while to <= filesize :
		block = imgfile[frm : to]
		if len(block) < AES.block_size:
			block = pad_pkcs7(block)
		file = open("encrypted","ab")
		file.write(aes_obj.encrypt(block))
		file.close()
		frm += 16
		to +=16
	
	print("encryption completed")
		
	


if __name__ == "__main__":
    main()
