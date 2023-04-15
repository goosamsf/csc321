def create_crypto_cookie(user, userid, role, key):
    #Create the cookie contents
    cookie = "user=" + user + "&uid=" + str(userid) + "&role=" + role
    
    arr = bytes(cookie, 'utf-8')
    print(f"cookie plaintext length is {len(arr)}")
    #Use strong crypto so cookie can't be read or changed.
    aes_obj = AES.new(bytes(key),AES.MODE_ECB)
    k =aes_obj.encrypt(bytes(ansix923_pad(cookie, AES.block_size), "UTF-8"))
#    breakpoint()
    print(f"cookie cipertext length is {len(k)}")
    return k

def verify_crypto_cookie(enc_cookie, key):

    aes_obj = AES.new(bytes(key),AES.MODE_ECB)
    cookie_pad = aes_obj.decrypt(enc_cookie)
    cookie = ansix923_strip(cookie_pad, AES.block_size)
    query = urllib.parse.parse_qs(cookie)
    
    return query["user"][0], query["uid"][0], query["role"][0]


def main():
	print("Hello World!")

	with open("../cp-logo.bmp","rb") as f:
		imgfile = f.read()
		
	filesize =len(imgfile)
	block = imgfile[:16]
	print(filesize)
	print(type(imgfile))
	print(block)
	print(block[0])
	
	
if __name__ == "__main__":
    main()

