from mylib import *
# 1. without line 7 and line10
# 2. without line6 , should be started from no files .

def verify(file, filesize ):
#	cbc_decrypt(file, filesize) 
	cbc_decrypt(get_craftedCP(),filesize)
	with open("cbc_decrypted","rb") as f:
		contents = f.read()
	contents = contents[16:]
	contents = contents.decode()	
	contents = contents.replace("%3D", "=")
	contents = contents.replace("%3B", ";")
	is_admin(contents)

def is_admin(contents):
	pattern = ";admin=true"
	if pattern in contents:
		print("Yes, you are admin!")
	else:
		print("No you are not admin!")

def get_craftedCP():
	with open("cbc_encrypted","rb") as f:
		contents = f.read()
	crafted= b';admin=true00000'
	with open("cbc_decrypted","rb") as k:
		pt = k.read()
	ciphertext = contents[0:16]
	print(len(ciphertext))
	plaintext = pt[16:32]
	print(len(plaintext))
	plaintext = bytes_xor(plaintext,ciphertext )
	crafted = bytes_xor(crafted, plaintext)
	crafted = crafted + contents[16:]
	return crafted

def main():
	print("Hello World!")
	with open("cbc_encrypted", "rb") as f:
		file = f.read()
	
	verify(file, len(file))

if __name__ == "__main__":
    main()

