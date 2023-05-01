from task2lib import *

print("Hello world")
PASSLEN = 6



wl = [x for x in words.words() if len(x) >= 6 and len(x) <= 10]
reffile = readfile()
print(reffile)
print(len(wl))
count = 0 
everythousands = 1000

for i in wl:
    if count == everythousands:
        print(everythousands)
        everythousands += 1000
    bcword = bcrypt.hashpw(i.encode(), reffile[0])
    hashed = bcword[-31:]
    count+=1
    if if_existed(reffile[1], hashed):
        print(f"found pw, {i}")
        writetoit(i)
    
