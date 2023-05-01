from nltk.corpus import words
import time, bcrypt

def measure_bywf(wf = 12):
    s_t = time.time()
    i = bcrypt.hashpw(b'testing',bcrypt.gensalt(wf))
    e_t = time.time()
    return e_t - s_t

def readfile():
    lst = [] 
    hshlst = []
    saltflag = True
    with open("wf13.txt", "r") as f:
        while ((i := f.readline()) != '') :
            if saltflag :
                lst.append(get_salt(i))
                saltflag = False
            get_hash(i,hshlst)
    lst.append(hshlst)
    return lst 
def get_salt(s):

    for i in range(len(s)):
        if s[i] == ":":
            return s[i+1:i+30].encode() 

def get_hash(s,hshlst):
    for i in range(len(s)):
        if s[i] == ":":
            hshlst.append(s[i+30:-1].encode())
            return ""

def if_existed(lst, hashed):
    return hashed in lst

def writetoit(word):
    with open("found.txt", "a") as f:
        f.write(word)
        f.write('\n')

