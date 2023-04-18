#1. Read Encrypted File
#2. Create AES object
from mylib import *

def main():
	print("Hello World!")

	with open("encrypted","rb") as f:
		enfile = f.read()
		
	ecb_decrypt(enfile, len(enfile))

	


if __name__ == "__main__":
    main()
