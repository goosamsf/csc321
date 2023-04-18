from mylib import *




def submit(str1, str2, userdata):
	url_encode = str1 + userdata + str2
	url_encode = url_encode.replace("=", "%3D");
	url_encode = url_encode.replace(";", "%3B")
	url_encode = bytes(url_encode, 'utf-8')
	return cbc_encrypt(url_encode, len(url_encode))	

def main():
	print("Hello World!")
	str1 = "userid=456;userdata="
	str2 = ";session-id=31337"
	userdata = input("Please Enter Userdata : ")
	urlencode = submit(str1,str2, userdata) 
	print(urlencode)
			
	


if __name__ == "__main__":
    main()

